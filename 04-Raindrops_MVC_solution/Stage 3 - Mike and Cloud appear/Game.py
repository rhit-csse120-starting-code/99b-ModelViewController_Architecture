"""
The  Game (model)  file for the Model-View-Controller architecture for our game.
1. It constructs all the objects specific to this game.
2. Its   draw_game   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to draw themselves.
3. Its   run_one_cycle   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to do whatever needs to happen
   independently of events / user-input.

Team members: SOLUTION by David Mutchler.
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame
# DONE: Put each class in its own module, using the same name for both.
from Cloud import Cloud
from Hero import Hero
from Raindrop import Raindrop


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # DONE: Store whatever YOUR game needs, perhaps something like this:
        self.mike = Hero(screen, 300, 400,
                         "../media/Mike_umbrella.png", "../media/Mike.png")
        self.cloud = Cloud(screen, 300, 50, "../media/cloud.png")

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # DONE: Use something like the following, but for objects in YOUR game:
        self.mike.draw()
        self.cloud.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.enemies.move()
        #     self.missiles.handle_explosions(self.enemies)
