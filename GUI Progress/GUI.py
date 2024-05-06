# Name: Joseph Dalferes
# Initial GUI implementation for the StudySensor Project

from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from pygame_menu.baseimage import BaseImage

HEIGHT = 768
WIDTH = 1366

class MenuManager:

    # Constructor
    def __init__(self, capacity, free_rooms):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.main_menu = self.create_main_menu()
        self.building_menu = self.create_building_menu(capacity)
        self.map_menu = self.create_map(free_rooms)
        self.help_menu = self.create_help_menu()

    # Main menu screen
    def create_main_menu(self):
        main_menu = pygame_menu.Menu('Welcome to the StudySensor', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        main_menu.add.button('Building Menu', self.show_building_menu)
        main_menu.add.button('Map', self.show_map)
        main_menu.add.button('Help', self.show_help_menu)
        main_menu.add.button('Quit', pygame_menu.events.EXIT)
        return main_menu
    
    # Creates and displays all integrated buildings
    def create_building_menu(self, capacity):
        building_menu = pygame_menu.Menu('Buildings', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        building_menu.add.button('IESB', self.show_IESB_rooms(capacity))
        building_menu.add.button('Wyly (Unimplemented)', self.show_wyly_rooms())
        building_menu.add.button('Library (Unimplemented)', self.show_library_rooms())
        return building_menu
    
    def show_building_menu(self):
        self.main_menu._open(self.building_menu)
    
    # Creates and displays the map of integrated buildings
    def create_map(self, free_rooms):
        bg_image = BaseImage(image_path = "background_image.png", drawing_offset = (0, 0))
        map_theme = pygame_menu.themes.Theme(background_color=bg_image)
        map_menu = pygame_menu.Menu(f'IESB (29): {free_rooms}/9', WIDTH, HEIGHT, theme = map_theme)
        return map_menu

    def show_map(self):
        self.main_menu._open(self.map_menu)

    def show_IESB_rooms(self, capacity):
        rooms = pygame_menu.Menu('Rooms', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        rooms.add.label(f"Floor 1, Room 1; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 1, Room 2; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 1, Room 3; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 2, Room 1; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 2, Room 2; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 2, Room 3; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 3, Room 1; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 3, Room 2; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 3, Room 3; Capacity: {capacity}/6")
        return rooms

    # Filled with unknowns because sensors are limited
    def show_wyly_rooms(self):
        rooms = pygame_menu.Menu('Rooms', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        rooms.add.label("Undetermined; Capacity: Unknown")
        return rooms

    # Filled with unknowns because sensors are limited
    def show_library_rooms(self):
        rooms = pygame_menu.Menu('Rooms', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        rooms.add.label("Undetermined; Capacity: Unknown")
        return rooms
    
    # Creates and displays the functionality of the GUI (Map is a real time map of building occupancy, 
    # building menu is a general menu of buildings, clicking on building takes you to a lisy of rooms 
    # in that building, etc)
    def create_help_menu(self):
        help_menu = pygame_menu.Menu('Help Menu', WIDTH, HEIGHT, theme = themes.THEME_DARK)
        help_menu.add.label('The building menu lets you see each outfitted building and each of their rooms. \n'
                            'Each room has been named based on a counterclockwise numerical \n'
                            'system from the front door. \n')

        help_menu.add.label('The map button you see shows a campus map, as well as the general current capacity \n'
                            ' of each building currently outfitted with sensors. Currently this is only the IESB \n'
                            'because of time and spending constraints. Because of this, the capacity and designation \n'
                            ' of the IESB is in the title. The lower the capacity, the more room there is. \n')
    
        help_menu.add.label('I hope you enjoy the StudySensor!')

        return help_menu

    def show_help_menu(self):
        self.main_menu._open(self.help_menu)

    # Runs the menu system
    def run(self):
        self.main_menu.mainloop(self.surface)

main = MenuManager(capacity = 0, free_rooms = 0)
main.run()