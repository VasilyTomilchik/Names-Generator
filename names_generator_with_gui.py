import random
import codecs
# from names_gui import GUI
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import os


class GUI(Tk):
    def __init__(self):
        # tkinter.Tk.__init__(self)
        super(GUI, self).__init__()
        # self.parent = parent
        self.geometry("365x200+650+150")
        # self.minsize(width=365, height=200)
        self.resizable(False, False)
        self.title('Names Generator')
        bg_image = ImageTk.PhotoImage(Image.open('Paper-Texture.jpg'))
        # bg_image = tkinter.PhotoImage(file='old-paper.gif')
        self.label = Label(self, image=bg_image)
        self.label.im = bg_image # keep reference to image file
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.Button1 = Button(self.label)
        self.Button2 = Button(self.label)
        self.Button3 = Button(self.label)
        self.Button4 = Button(self.label)
        self.Label1 = Label(self.label)
        self.Label2 = Label(self.label)

        self.initialize()

    def initialize(self):
        self.Button1.place(relx=0.33, rely=0.65, height=54, width=117)
        # self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Generate!''')
        self.Button1.configure(width=117)
        self.Button1.configure(relief=GROOVE)
        self.Button1.configure(cursor='hand2')

        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.place(x=18, y=154, height=30, width=80)
        self.Button2.configure(text='To file')
        self.Button2.configure(relief=GROOVE)
        self.Button2.configure(cursor='hand2')

        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.place(x=267, y=154, height=30, width=80)
        self.Button3.configure(text='Exit')
        self.Button3.configure(relief=GROOVE)
        self.Button3.configure(cursor='hand2')
        self.Button3.configure(command=exit)

        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.place(x=18, y=117, height=30, width=80)
        self.Button4.configure(text='To favorites')
        self.Button4.configure(relief=GROOVE)
        self.Button4.configure(cursor='hand2')

        label_font = "-family {Segoe UI} -size 12 -weight normal -slant " \
                     "roman -underline 0 -overstrike 0"

        self.Label1.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)
        self.Label1.configure(background="#9698e0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=label_font)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(relief=GROOVE)
        self.Label1.configure(width=314)

        self.Label2.place(relx=0.05, rely=0.35, relheight=0.2, relwidth=0.9)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=label_font)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(relief=GROOVE)
        self.Label2.configure(width=314)

    def write_question(self):
        return messagebox.askyesno(title='Write names?',
                                   message='This will create a file and write 10k cool names.\n'
                                           'Do you want to continue?',
                                   icon='info')

    def save_window(self):
        types = [('textfiles', '*.csv'), ('all files', '*.*')]
        return filedialog.asksaveasfile('w', initialdir=os.getcwd(), filetypes=types, defaultextension='csv')

    def start(self):
        pass


class GeneratorLogic:
    def __init__(self):
        gui.Button1.configure(command=self.show_names)
        gui.Button2.configure(command=self.write_names_to_file)
        gui.Button3.configure(command=exit)
        gui.Button4.configure(command=self.favorites, state='disabled')
        gui.mainloop()

    def name_gen(self):
        a = 'aeiouy'
        b = 'bcdfghjklmnpqrstvwxz'
        z = random.randint(0, 1)
        name = ''
        for i in range(random.randint(2, 5)):
            name += str(random.choice(a if z else b)) + str(random.choice(b if z else a))
        final_name = name.replace(name[0], name[0].upper(), 1)
        return final_name[:-1] if random.randint(0, 1) else final_name

    def full_name_gen(self):
        return self.name_gen(), self.name_gen()

    def transliterator(self, item):
        name = ''
        letters_en = u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letters_ru = u'абцдефгхижклмнопкрстуввхызАБЦДЕФГХИЖКЛМНОПКРСТУВВХЫЗ'
        for i in item:
            ind = letters_en.index(i)
            if i == 'x':
                name += 'кс'
            elif i == 'X':
                name += 'Кв'
            elif i == 'j':
                name += 'дж'
            elif i == 'J':
                name += 'Дж'
            elif i == 'Y' and item.index(i) == 0:
                name += 'И'
            elif i == 'y' and item[(item.index(i) - 1)] == 'j':
                name += 'и'
            elif i == 'q' and item.index(i) == (len(item) - 1):
                name += 'к'
            elif i == 'h' and item.index(i) == (len(item) - 1):
                name += ''
            elif i == 'q':
                name += 'кв'
            elif i == 'Q':
                name += 'Кв'
            elif i == 'U':
                name += 'Ю'
            elif i == 'E':
                name += 'Э'
            else:
                name += letters_ru[ind]
        return name

    def show_names(self):
        gui.Button4.configure(state='normal')
        self.en_name, self.en_last = self.full_name_gen()
        if not random.randint(0, 40):
            self.en_name = self.en_last
        self.ru_name = self.transliterator(self.en_name)
        self.ru_last = self.transliterator(self.en_last)
        # print(('{} {}, {} {}'.format(self.en_name, self.en_last, self.ru_name, self.ru_last)))
        gui.Label1.configure(text='{} {}'.format(self.en_name, self.en_last))
        gui.Label2.configure(text='{} {}'.format(self.ru_name, self.ru_last))

    def write_names_to_file(self):
        y_n = self.yes_no()
        if y_n:  # check if yes button pressed
            file_name = self.save_file()
            if file_name:  # check if file is chosen
                with codecs.open(file_name, 'w', encoding='utf-8') as file:
                    file.write('en_name,en_last,ru_name,ru_last\n')
                    for i in range(10000):
                        en_name, en_last = self.full_name_gen()
                        if not random.randint(0, 40):
                            en_name = en_last
                        ru_name = self.transliterator(en_name)
                        ru_last = self.transliterator(en_last)
                        file.write('{},{},{},{}\n'.format(en_name, en_last, ru_name, ru_last))
            else:
                gui.Label1.configure(text='Think twice next time!')
                gui.Label2.configure(text='')
        else:
            gui.Label1.configure(text='As you wish:)')
            gui.Label2.configure(text='')

    def yes_no(self):
        return gui.write_question()

    def save_file(self):
        file = gui.save_window()
        if file:
            file = file.name
        gui.Label1.configure(text='File saved!')
        gui.Label2.configure(text=file)
        return file

    def favorites(self):
        with codecs.open('favorites.csv', 'a+', encoding='utf-8') as fav:
            fav.write('{} {}, {} {}\n'.format(self.en_name, self.en_last, self.ru_name, self.ru_last))


if __name__ == '__main__':
    gui = GUI()
    app = GeneratorLogic()
