#Group #2 GUI
#Causey, Dalferes, Vaurigaud

from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from pygame_menu.baseimage import BaseImage

from Sensor import *
HEIGHT = 820
WIDTH = 1536

class MenuManager:

    # Constructor
    def __init__(self, capacity, free_rooms):
        pygame.init()
        self.capacity = capacity
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.main_menu = self.create_main_menu()
        self.building_menu = self.create_building_menu(self.capacity)
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
        '''Note by August; made capacity const for all but first room'''
        rooms.add.label(f"Floor 1, Room 1; Capacity: {capacity}/6")
        rooms.add.label(f"Floor 1, Room 2; Capacity: {6}/6")
        rooms.add.label(f"Floor 1, Room 3; Capacity: {6}/6")
        rooms.add.label(f"Floor 2, Room 1; Capacity: {6}/6")
        rooms.add.label(f"Floor 2, Room 2; Capacity: {6}/6")
        rooms.add.label(f"Floor 2, Room 3; Capacity: {6}/6")
        rooms.add.label(f"Floor 3, Room 1; Capacity: {6}/6")
        rooms.add.label(f"Floor 3, Room 2; Capacity: {6}/6")
        rooms.add.label(f"Floor 3, Room 3; Capacity: {6}/6")
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
        self.main_menu.mainloop(loop_over())
        #self.main_menu.mainloop(self.surface) 
            #in which self.surface could go into the main function and then the main
            #function would go into mainloop
            #also we sould import GUI into main.py and mainrun in main.py too. 

'''Note by August; capacity/free_rooms to be modified in main
    free_rooms will be const for our purpose'''
main = MenuManager(capacity = 0, free_rooms = 0)        
main.run()


#/////////MAIN////////(restructured, no need to import)

from Sensor import *

sonic1 = Sensor("sonic1", [23,24])
sonic2 = Sensor("sonic2", [6,5])
sonic1.calibrate()
sonic2.calibrate()

print(f"sonic1 gap = {sonic1.gap}")
print(f"sonic2 gap = {sonic2.gap}")

people = 0

def loop_over():
    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    
    global people

    count = 0   
    list1 = []
    list2 = []

    while count <= 3:
        list1 = sonic1.sensor_tripped(list1)
        list2 = sonic2.sensor_tripped(list2)
        count += 1

    #oldval = main.capacity?

    if len(list1) != 0:
        people = sonic1.in_or_out(sonic2, people, list1, list2)
    
    print(people)
    main.__init__((6-people), 0)
    