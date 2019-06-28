class Constants:
    
    BLACK_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    RED_COLOR = (255, 0, 0)
    GREEN_COLOR = (0, 255, 0)
    BLUE_COLOR = (0, 0, 255)
    YELLOW_COLOR = (255, 255, 0)
    MAGENTA_COLOR = (255, 0, 255)
    CYAN_COLOR = (0, 255, 255)


    # PHYSICS
    G = 6.67e-1


    # PYGAME
    RUNNING = True
    WIDTH = 1000
    HEIGHT = 700
    FPS = 45
    DT = 0.015 #1/FPS


    # MENU
    MENU_WIDTH = 600
    MENU_HEIGHT = 500
    MENU_COLOR = (190, 190, 190, 100)
    MENU_CLOSED_POSITION = [WIDTH-30, 100]
    MENU_OPENED_POSITION = [WIDTH-MENU_WIDTH, 100]

    # BUTTON
    BUTTON_COLOR_DANGER = (220, 53, 69)
    BUTTON_COLOR_SUCCESS = (40, 167, 69)
    BUTTON_COLOR_PRIMARY = (0, 123, 255)

    # INITIAL MESSAGE
    GAME_MESSAGE = "                            .__  __                 \n"
    GAME_MESSAGE += "   ____________________  __|__|/  |____ __  ______ \n"
    GAME_MESSAGE += "  / ___\_  __ \__   \  \/  /  \   __\  |  \/  ___/ \n"
    GAME_MESSAGE += " / /_/  >  | \// __  \   / |  ||  | |  |  /\___ \  \n"
    GAME_MESSAGE += " \___  /|__|  (____  /\_/  |__||__| |____//___   > \n"
    GAME_MESSAGE += "/_____/            \/                         \/  \n"