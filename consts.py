
ORIGIN = (0, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
COLORKEY = (255, 0, 255)

# Fonts
FONT_ACTION_MAN = "fonts/Action_Man.ttf"
FONT_ACTION_MAN = "fonts/Action_Man_Bold.ttf"

# Backgrounds
BG_MENU = "intro.png"
BG_GAME = "background.png"
BG_GAME_OVER = "end.png"
BG_SCORE_BOARD = "scoreboard.png"

# Images
BLUELORRY = "bluelorry.png"
GREENLORRY = "greenlorry.png"
LORRIES = [BLUELORRY, GREENLORRY]
LORRY_WIDTH = 60

REDTRUCK = "redtruck.png"
PURPLETRUCK = "purpletruck.png"
TRUCKS = [REDTRUCK, PURPLETRUCK]
TRUCK_WIDTH = 65

ORANGECAR = "orangecar.png"
PINKCAR = "pinkcar.png"
REDCAR = "redcar.png"
BLUECAR = "bluecar.png"
CARS = [ORANGECAR, PINKCAR, REDCAR, BLUECAR]
CAR_WIDTH = 46

CHICKEN = "chicken.png"

HUT = "hut.png"
EGG = "egg.png"

INTRO = "intro.png"
END = "end.png"

DEAD_CHICKEN = "dead_chicken.png"
ALIVE_CHICKEN = "alive_chicken.png"


# Keymap controls

from pygame.locals import *

KM_LEFT = K_LEFT
KM_RIGHT = K_RIGHT
KM_UP = K_UP
KM_DOWN = K_DOWN
KM_LEFT1 = K_a
KM_RIGHT1 = K_d
KM_UP1 = K_w
KM_DOWN1 = K_s


# Controller events

E_WIN = 5001
E_DIE = 5002
E_SOFT_RESET = 5003
E_HOP = 5004
E_SCORE_CHANGED = 5005
E_DISABLE_MOVEMENT = 5006
E_ENABLE_MOVEMENT = 5007
E_TEXT_CAPTURE = 5008
E_SCORE_SAVED = 5009
E_LEVEL_CHANGED = 5010 #

# Directions

LEFT = 1
UP = 2
RIGHT = 3
DOWN = 4

# Scoring

LIVES = 5 # Number of lives a player starts with
POINTS_PROGRESSION = 1 # Points for a 'progression', a non repeatable hop up
POINTS_WIN = 10 # Points for completing a level

# Screen dimensions, we're using a 32x32 grid

GRID = 32

SCREEN_WIDTH = 30 * GRID
SCREEN_HEIGHT = 22 * GRID






