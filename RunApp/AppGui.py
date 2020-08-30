from tkinter import *
from tkinter import ttk
import win32gui
import pywintypes


class Gui:
    def __init__(self):
        self.elements = {'root': None, 'main_frame': None, 'data_frame': None, 'buttons_frame': None}
        self.gui_structure = {
            'elements': ({'widget': ttk.Frame, 'parent': self.elements['root'], 'name': 'main_frame', 'position': (1, 1)}, {'widget': ttk.Frame, 'parent': self.elements['main_frame'], 'name': 'data_frame', 'position': (1, 1)}, {'widget': ttk.Frame, 'parent': self.elements['main_frame'], 'name': 'buttons_frame', 'position': (2, 1)}, {'widget': ttk.Entry, 'parent': self.elements['data_frame'], 'name': 'url_entry', 'position': (1, 1)},),
            'buttons': ({'parent': self.elements['buttons_frame'], 'name': "add_page_button", 'command': self.addPage, "text": 'AddPage', "position": (2, 1)}, {'parent': self.elements['buttons_frame'], 'name': "add_program_button", 'command': self.addProgram, "text": 'AddProgram', "position": (2, 2)}, {'parent': self.elements['buttons_frame'], 'name': "exit_button", 'command': self.exitGui, "text": "Run", "position": (2, 3)})}
        self.root = Tk()
        self.elements['root'] = self.root
        self.root.title("Run")
        self.root.columnconfigure(0, weight=1)

        for element in self.gui_structure['elements']:
            self.createGuiElement(element['widget'], element['parent'], element['name'], position=element['position'])
        for button in self.gui_structure['buttons']:
            self.createButton(button['parent'], button['name'], button['command'], text=button['text'], position=button['position'])
        self.createGui()

    def createGuiElement(self, widget_type, parent, element_name, position=(0, 0)):
        element = widget_type(parent)
        element.grid(column=position[0], row=position[1])
        self.elements[element_name] = element

    def createButton(self, parent, button_name, command, text=str(), position=(0, 0)):
        element = ttk.Button(parent, command=command, text=text)
        element.grid(column=position[0], row=position[1])
        self.elements[button_name] = element

    def createGui(self):
        self.root.mainloop()

    def addProgram(self):
        try:
            path = win32gui.GetOpenFileNameW()
        except pywintypes.error:
            path = ''
        finally:
            return path

    def addPage(self):
        url = self.elements['url_entry'].get()
        self.elements['url_entry'].delete(0, END)
        if url:
            if not url.startswith('http://' or 'https://'):
                url = 'http://' + url
            return url
        return

    def exitGui(self):
        self.root.destroy()


a = Gui()

