#!/usr/bin/env python3

from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
import os

from argos_translate import translate

class GUI:
    def __init__(self):
        self.output_scrolledtext = None
        self.input_scrolledtext = None
        
        self.window = Tk()
        self.window.title("Argos Translate")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=0)

        language_names = tuple([language.name for language in translate.languages])

        self.input_combo = Combobox(self.window)
        self.input_combo['values'] = language_names
        self.input_combo.current(0) 
        self.input_combo.grid(column=0, row=0, sticky=N)

        self.output_combo = Combobox(self.window)
        self.output_combo['values'] = language_names
        self.output_combo.current(1) 
        self.output_combo.grid(column=1, row=0, sticky=N)

        self.input_scrolledtext = scrolledtext.ScrolledText(self.window,width=80,height=50)
        self.input_scrolledtext.grid(column=0, row=1, sticky='NSEW')
        self.input_scrolledtext.insert(INSERT, 'Text to translate from')
        self.input_scrolledtext.columnconfigure(0, weight=1)
        self.input_scrolledtext.rowconfigure(2, weight=1)

        self.output_scrolledtext = scrolledtext.ScrolledText(self.window,width=80,height=50)
        self.output_scrolledtext.grid(column=1, row=1, sticky='NSEW')
        self.output_scrolledtext.insert(INSERT, 'Text to translate to')
        self.output_scrolledtext.columnconfigure(1, weight=1)
        self.input_scrolledtext.rowconfigure(2, weight=1)


        # Enable Ctrl-A
        def select_all_input(event):
            event.widget.tag_add(SEL, "1.0", END) 
            event.widget.mark_set(INSERT, "1.0")
            return "break"
        self.input_scrolledtext.bind("<Control-Key-a>", select_all_input)
        self.output_scrolledtext.bind("<Control-Key-a>", select_all_input)

        # Enable <Enter> to translate
        def enter_clicked(event):
            self.translate_button_clicked()
        def enter_clicked_back(event):
            self.translate_button_clicked_back()
        self.input_scrolledtext.bind('<Return>', enter_clicked)
        self.output_scrolledtext.bind('<Return>', enter_clicked_back)

        translate_button = Button(self.window, text='→', command=self.translate_button_clicked)
        translate_button.grid(column=0, row=2)

        translate_button_back = Button(self.window, text='←', command=self.translate_button_clicked_back)
        translate_button_back.grid(column=1, row=2)

        self.translate_button_clicked()
        self.window.mainloop()

    def translate_button_clicked(self):
        input_text = self.input_scrolledtext.get("1.0",END)
        input_combo_value = self.input_combo.current()
        input_language = translate.languages[input_combo_value]
        output_combo_value = self.output_combo.current()
        output_language = translate.languages[output_combo_value]
        translation = input_language.get_translation(output_language)
        result = translation.translate_function(input_text)
        self.output_scrolledtext.delete(1.0,END)
        self.output_scrolledtext.insert(INSERT,result)

    def translate_button_clicked_back(self):
        input_text = self.output_scrolledtext.get("1.0",END)
        input_combo_value = self.output_combo.current()
        input_language = translate.languages[input_combo_value]
        output_combo_value = self.input_combo.current()
        output_language = translate.languages[output_combo_value]
        translation = input_language.get_translation(output_language)
        result = translation.translate_function(input_text)
        self.input_scrolledtext.delete(1.0,END)
        self.input_scrolledtext.insert(INSERT,result)

def main():
    gui = GUI()
