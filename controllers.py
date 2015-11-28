import pygame
from pygame.locals import *

from consts import *
from object_manager import ObjectManagerMixin
from characters import *

class BaseController(object):
  pass

class Controller(BaseController, ObjectManagerMixin):
  EVENT_BINDINGS = [] # Empty bindings

  def __init__(self, engine):
    self.engine = engine
    self.create() # Use create in sub-classes for any init stuff

  # Method stubs

  def create(self):
    pass

  def tick(self):
    self.tick_objects()

  def destroy(self):
    self.purge_objects()

class MenuController(Controller):
  def create(self):
    bg = pygame.image.load('images/menu.png')
    self.engine.clear_background()
    self.engine.background_blit(bg, ORIGIN)


  def start_game(self):
    self.engine.setup_state('game')

  EVENT_BINDINGS = {
    K_RETURN: start_game
  }

class GameController(Controller):
  level = 0
  score = 0
  lives = LIVES

  def create(self):
    self.engine.clear_background()

  def win(self, event):
    """Handle game state changes for win"""
    self.add_score(POINTS_WIN)
    self.level += 1
    self.engine.post_event(E_SOFT_RESET, level=self.level, lives=self.lives)

  def die(self, event):
    """Handle game state changes for die"""
    self.lives -= 1

    if self.lives < 1:
      self.gameover()

    self.engine.post_event(E_SOFT_RESET, level=self.level, lives=self.lives)

  def gameover(self):
    self.engine.setup_state('gameover')

  def player_moved(self, event):
    if event.progress:
      self.add_score(POINTS_PROGRESSION)

  def add_score(self, addition):
    self.score += addition
    self.engine.post_event(E_SCORE_CHANGED, score=self.score)

  EVENT_BINDINGS = {
    E_WIN: win,
    E_DIE: die,
    E_HOP: player_moved,
  }

class PlayerController(Controller):
  max_height = 0
  current_height = 0

  def create(self):
    self.player_object = self.create_object(Frog, self)

  def move(self, rel_pos):
    cp = self.player_object.pos
    self.player_object.pos = (cp[0] + rel_pos[0], cp[1] + rel_pos[1])

  def move_left(self):
    self.move((-32, 0))
    self.engine.post_event(E_HOP, direction=LEFT, progress=False)

  def move_right(self):
    self.move((32, 0))
    self.engine.post_event(E_HOP, direction=RIGHT, progress=False)

  def move_up(self):
    self.move((0, -32))

    self.current_height += 1
    progressed = self.max_height < self.current_height

    self.engine.post_event(E_HOP, direction=LEFT, progress=progressed)

    if progressed:
      self.max_height = self.current_height

  def move_down(self):
    self.current_height -= 1
    self.move((0, 32))
    self.engine.post_event(E_HOP, direction=DOWN, progress=False)

  def reset(self, event):
    self.player_object.move_to_start()

  EVENT_BINDINGS = {
    KM_LEFT: move_left,
    KM_RIGHT:  move_right,
    KM_UP: move_up,
    KM_DOWN: move_down,
    KM_LEFT1: move_left,
    KM_RIGHT1:  move_right,
    KM_UP1: move_up,
    KM_DOWN1: move_down,
    E_SOFT_RESET: reset,
  }


class LevelController(Controller):
  def create(self):
    self.cars = [
      self.create_object(Car, self, lane=0, delay=0),
      self.create_object(Car, self, lane=0, delay=3),
      self.create_object(Car, self, lane=0, delay=6),
      self.create_object(Car, self, lane=0, delay=8),
      self.create_object(Car, self, lane=1, delay=2),
      self.create_object(Car, self, lane=1, delay=4),
      self.create_object(Car, self, lane=1, delay=7),
      self.create_object(Car, self, lane=1, delay=9),
      self.create_object(Car, self, lane=2, delay=0),
      self.create_object(Car, self, lane=2, delay=4),
      self.create_object(Car, self, lane=3, delay=6),
      self.create_object(Car, self, lane=3, delay=2),
      self.create_object(Car, self, lane=3, delay=6),
      self.create_object(Car, self, lane=4, delay=0),
      self.create_object(Car, self, lane=4, delay=3),
      self.create_object(Car, self, lane=4, delay=6),
      self.create_object(Car, self, lane=4, delay=8),
    ]

  def speed_up_cars(self, event):
    for car in self.cars:
      car.change_speed(event.level)

  EVENT_BINDINGS = {
    E_SOFT_RESET: speed_up_cars
  }

class GameOverController(Controller):
  def restart(self):
    self.engine.setup_state('game')

  EVENT_BINDINGS = {
    K_RETURN: restart
  }

class FPSCounterController(Controller):

  def create(self):
    self.font = pygame.font.SysFont("Arial", 16)

  def tick(self):
    text = self.font.render(str(self.engine.get_fps()), True, YELLOW)
    self.engine.foreground_blit(text, (0, 0))


class ScoreTextController(Controller):
  score = 0
  lives = LIVES

  def create(self):
    self.font = pygame.font.SysFont("verdana", 20, bold = True, italic = False)

  def update_score(self, event):
    self.score = event.score

  def update_lives(self, event):
    self.lives = event.lives

  def tick(self):
    text = self.font.render("Score: {} Lives: {}".format(self.score, self.lives), 1 , (0, 0, 255))
    self.engine.foreground_blit(text, (0,0))

  EVENT_BINDINGS = {
    E_SCORE_CHANGED: update_score,
    E_SOFT_RESET: update_lives,
  }

