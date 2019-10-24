# Created by Kieran Jerry Jonathon
from TIGr import AbstractInterface
from FrontEnd import GuiInterface
from DrawerTKinter import Drawer
from Parser import Parser


class MainTIGr(AbstractInterface):

    def __init__(self, parser):
        super().__init__(parser)

    def create_interface(self):
        self.interface = GuiInterface(self)
        self.interface.start()

    def go(self):
        self.create_interface()


if __name__ == '__main__':
    main = MainTIGr(Parser(Drawer()))
    main.go()
