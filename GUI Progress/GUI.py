# Name: Joseph Dalferes
# Initial GUI implementation for the StudySensor Project

from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

class MenuManager:

    # Constructor
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
        self.main_menu = self.create_main_menu()
        self.building_menu = self.create_building_menu()
        self.map_menu = self.create_map()
        self.help_menu = self.create_help_menu()

    # Main menu screen
    def create_main_menu(self):
        main_menu = pygame_menu.Menu('Welcome to the StudySensor', 1366, 768, theme = themes.THEME_DARK)
        main_menu.add.button('Building Menu', self.show_building_menu)
        main_menu.add.button('Map', self.show_map)
        main_menu.add.button('Help', self.show_help_menu)
        main_menu.add.button('Quit', pygame_menu.events.EXIT)
        return main_menu
    
    # Creates and displays all integrated buildings
    def create_building_menu(self):
        building_menu = pygame_menu.Menu('Buildings', 1366, 768, theme = themes.THEME_DARK)
        building_menu.add.button('IESB', self.show_IESB_rooms(3))
        building_menu.add.button('Wyly', self.show_wyly_rooms)
        building_menu.add.button('Library', self.show_library_rooms)
        return building_menu
    
    def show_building_menu(self):
        self.main_menu._open(self.building_menu)
    
    # Creates and displays the map of integrated buildings
    def create_map(self):
        map_menu = pygame_menu.Menu('Real-Time Map', 1366, 768, theme = themes.THEME_DARK)
        return map_menu

    def show_map(self):
        self.main_menu._open(self.map_menu)

    def show_IESB_rooms(self, capacity):
        rooms = pygame_menu.Menu('Rooms', 1366, 768, theme = themes.THEME_DARK)
        rooms.add.text_input("Floor 3, Room 1:", default = f'Capacity: {capacity}/6')
        rooms.add.text_input("Floor 3, Room 2:", default = f'Capacity: {capacity}/6')
        rooms.add.text_input("Floor 3, Room 3:", default = f'Capacity: {capacity}/6')
        return rooms


    # Passed because of lack of implementation in this building
    def show_wyly_rooms(self):
        pass

    # Passed because of lack of implementation in this building
    def show_library_rooms(self):
        pass
    
    # Creates and displays the functionality of the GUI (Map is a real time map of building occupancy, 
    # building menu is a general menu of buildings, clicking on building takes you to a lisy of rooms 
    # in that building, etc)
    def create_help_menu(self):
        help_menu = pygame_menu.Menu('Help Menu', 1366, 768, theme = themes.THEME_DARK)
        help_menu.add.label('The colors you see in this program mean as follows: \n '
                            'Red = Full Room \n '
                            'Yellow = Half-full Room \n'
                            'Green = Empty Room \n')

        help_menu.add.label('The map button you see shows a real time map of the campus, \n'
                            'as well as the general current capacity of each building currently outfitted with sensors. \n')
        
        help_menu.add.label('The building menu lets you see each outfitted building and each of their rooms. \n'
                            'Each room has been named based on distance from front door and location within building. \n')

        help_menu.add.label('I hope you enjoy the StudySensor!')

        return help_menu

    def show_help_menu(self):
        self.main_menu._open(self.help_menu)

    # Runs the menu system
    def run(self):
        self.main_menu.mainloop(self.surface)

main = MenuManager()
main.run()