# -*- coding: utf-8 -*-
from Tkconstants import LEFT, RIGHT, E, W, BOTH, END
from Tkinter import Frame, Button, Tk, Listbox, Entry, StringVar, Label
from subprocess import Popen, PIPE, check_call, CalledProcessError
from tkFileDialog import askdirectory
from os.path import expanduser

try:
    check_call('which pep8', shell=True, stdout=PIPE, stderr=PIPE)
except CalledProcessError as e:
    print('PEP8 not found.')
    exit(1)

class Window(object):
    def __init__(self, master):

        self.master = master
        self.master.wm_title('PEP8 checker')
        self.master.resizable(False, True)

        self.frame = Frame(master)
        self.frame.pack(fill=BOTH, expand=1)

        home_dir = expanduser("~")
        self.directory = StringVar(value=home_dir)

        directory_frame = Frame(self.frame)
        directory_frame.grid()
        self.frame.grid_rowconfigure(2, weight=1)

        self.entry_directory = Entry(directory_frame, textvariable=self.directory)
        self.entry_directory.pack(anchor=W, side=LEFT)

        self.select_directory = Button(directory_frame, text="Select directory to scan", command=self.select_directory)
        self.select_directory.pack(anchor=E, side=RIGHT)

        self.run_button = Button(self.frame, text='Run PEP8!', command=self.run_pep)
        self.run_button.grid(sticky=W + E)

        self.errors_list = Listbox(self.frame)
        self.errors_list.grid(sticky=W + E)

        self.status_label = Label(self.frame)

    def select_directory(self):
        directory = askdirectory(initialdir=self.directory.get())
        if directory:
            self.directory.set(directory)

    def run_pep(self):
        self.errors_list.delete(0, END)
        process = Popen('$(which pep8) {}'.format(self.directory.get()), shell=True, stderr=PIPE, stdout=PIPE)
        output = process.communicate()[0]
        selected_dir = ''.join((self.directory.get(), '/'))
        if output:
            self.errors_list.configure(background='red')
            for i, error in enumerate(output.split('\n')):
                self.errors_list.insert(i, error.replace(selected_dir, ''))
        else:
            self.errors_list.configure(background='green')
            self.errors_list.insert(0, 'Directory is OK!')


root = Tk()
setattr(root, 'run', lambda *args, **kwargs: root.mainloop(*args, **kwargs))

app = Window(root)
root.run()