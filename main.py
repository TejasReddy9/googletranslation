from json import loads
from tkinter import Tk, Label, Button, Entry, Text, PhotoImage, END, OptionMenu, StringVar
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from googletrans import Translator

languages_f = open('./languages.json', 'r')
languages = loads(languages_f.read())
languages_f.close()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Text translation app')
        icon_photo = PhotoImage(file='app_icon.png')
        self.root.iconphoto(False, icon_photo)
        width = 510
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.ft = tkFont.Font(family='Franklin', size=10)

        self.app_title = Label(root)
        self.app_title['font'] = tkFont.Font(family='Franklin', size=16)
        self.app_title['fg'] = '#000000'
        self.app_title['justify'] = 'left'
        self.app_title['text'] = 'Text translation'
        self.app_title.place(x=10, y=10, width=320, height=44)

        self.translate_from_var = StringVar(root)
        self.translate_from_var.set('Auto')  # default value
        self.translate_from_entry = OptionMenu(
            root, self.translate_from_var, *list(languages.keys()))
        self.translate_from_entry['bg'] = '#f6e0b5'
        self.translate_from_entry['font'] = self.ft
        self.translate_from_entry['justify'] = 'left'
        self.translate_from_entry.place(x=10, y=100, width=179, height=30)

        self.translate_from_label = Label(root)
        self.translate_from_label['font'] = self.ft
        self.translate_from_label['fg'] = '#000000'
        self.translate_from_label['justify'] = 'left'
        self.translate_from_label['text'] = 'Translate from:'
        self.translate_from_label.place(x=10, y=70, width=98, height=30)

        self.translate_to_var = StringVar(root)
        self.translate_to_var.set('English')  # default value
        self.translate_to_entry = OptionMenu(
            root, self.translate_to_var, *list(languages.keys())[:-1])
        self.translate_to_entry['bg'] = '#f6e0b5'
        self.translate_to_entry['font'] = self.ft
        self.translate_to_entry['justify'] = 'left'
        self.translate_to_entry.place(x=240, y=100, width=175, height=30)

        self.translate_to_label = Label(root)
        self.translate_to_label['font'] = self.ft
        self.translate_to_label['fg'] = '#000000'
        self.translate_to_label['justify'] = 'left'
        self.translate_to_label['text'] = 'Translate to:'
        self.translate_to_label.place(x=240, y=70, width=70, height=25)

        self.translate_text = Text(root)
        self.translate_text['bg'] = '#a39193'
        self.translate_text['borderwidth'] = '4px'
        self.translate_text['font'] = self.ft
        self.translate_text['fg'] = '#000000'
        self.translate_text.place(x=10, y=160, width=182, height=294)

        self.translated_text = Text(root)
        self.translated_text['bg'] = '#aa6f73'
        self.translated_text['borderwidth'] = '4px'
        self.translated_text['font'] = self.ft
        self.translated_text['fg'] = '#000000'
        self.translated_text['state'] = 'disabled'
        self.translated_text.place(x=240, y=160, width=173, height=295)

        self.translate_button = Button(root)
        self.translate_button['bg'] = '#eea990'
        self.translate_button['font'] = self.ft
        self.translate_button['fg'] = '#000000'
        self.translate_button['justify'] = 'center'
        self.translate_button['text'] = 'Translate!'
        self.translate_button.place(x=430, y=100, width=67, height=30)
        self.translate_button['command'] = self.translate_button_command

    def translate_button_command(self):
        language_from = languages[self.translate_from_var.get()]
        language_to = languages[self.translate_to_var.get()]
        translate_str = self.translate_text.get('1.0', END)
        translated_text = ''
        try:
            translator = Translator()
            translated_text = str(translator.translate(translate_str,
                                                       src=language_from, dest=language_to).text)
        except:
            showinfo('An error occurred',
                     'An error occurred. Please check the input, try again later.')

        # translated_text = ''

        # for sentence in loads(html)[0]:
        #    translated_text += sentence[0]

        self.translated_text['state'] = 'normal'
        self.translated_text.delete('1.0', END)
        self.translated_text.insert('1.0', translated_text)
        self.translated_text['state'] = 'disabled'


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
