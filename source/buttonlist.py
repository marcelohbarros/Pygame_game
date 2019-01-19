import pygame
import config as cfg
from image import Image
from button import Button

class ButtonList:
    def __init__ (self):
        self.PLAY = 0
        self.SETTINGS = 1
        self.QUIT = 2

        selectedImage = Image("media/selectedbutton.png", alpha=True)

        playButton = Button("media/playbutton.png", selectedImage, 272, 96)
        settingsButton = Button("media/settingsbutton.png", selectedImage, 272, 160)
        quitButton = Button("media/quitbutton.png", selectedImage, 272, 224)

        self.button = [playButton, settingsButton, quitButton]
        self.button[self.PLAY].select()

    def selected(self):
        if self.button[self.PLAY].isSelected():
            return self.PLAY
        elif self.button[self.SETTINGS].isSelected():
            return self.SETTINGS
        else:
            return self.QUIT

    def selectNext(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected + 1) % len(self.button)].select()

    def selectPrevious(self):
        selected = self.selected()
        self.button[selected].unselect()
        self.button[(selected - 1) % len(self.button)].select()

    def render(self, bufferSurface):
        [x.render(bufferSurface) for x in self.button]
