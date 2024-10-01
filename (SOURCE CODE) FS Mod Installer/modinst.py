#Import stuff
import os
import shutil
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from customtkinter import * 

set_default_color_theme("blue")

modpath = str()

#FUNCTIONS

def browsebut(self):
        global modpath
        modselect = filedialog.askdirectory()
        modpath = str(modselect)
        t2 = CTkLabel(win1, text = modpath, font=('Arial',15))
        t2.grid(column=0, row=2)

def instbut(self):
    ismodder = os.path.exists(os.path.join(modpath,'Floating Sandbox'))
    isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
    #Checks
    if ismodder == False:
            messagebox.showwarning('Error', 'The mod file does not exist or is in inavlid format!')
    elif isfsder == False:
        messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
    else:
        shutil.copytree(os.path.join(modpath,'Floating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
        global t3
        t3 = CTkLabel(win1, text ="Installed!", font=('Arial',15))
        t3.grid(column=0, row=3)
        #print(os.path.join(str(modpath),'Floating Sandbox'))

def uninstbut(self):
        ismodder = os.path.exists(os.path.join(modpath,'Floating Sandbox'))
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        ismodpathsder = os.path.exists(os.path.join(modpath,'modpaths.txt'))
        isfsoldder = os.path.exists(os.path.join(modpath,'FSold'))
        #Checks
        if ismodder == False:
            messagebox.showwarning('Error', 'The mod file does not exist or is in inavlid format!')
        elif isfsder == False:
                messagebox.showwarning('Error', "'Floating' Sandbox folder does not exist!")
        elif ismodpathsder == False:
                messagebox.showwarning('Error', "'modpaths.txt' does not exist, try Load Backup method.")
        elif isfsoldder == False:
                messagebox.showwarning('Error', "'Fsold folder' does not exist!")
        else:
                with open(os.path.join(modpath,'modpaths.txt')) as f:
                        lines1 = [line1.rstrip() for line1 in f]
                        for line1 in lines1:
                                if os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), line1)):
                                        os.remove(os.path.join(os.environ.get('LOCALAPPDATA'), line1))
                                        shutil.copytree(os.path.join(os.path.join(modpath,'FSold'), 'Floating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
                                else:
                                        messagebox.showwarning('Error', 'The mod is already uninstalled!')
                t4 = CTkLabel(win1, text ="Uninstalled!", font=('Arial',15))
                t4.grid(column=0, row=4)

def backup(self):
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        isbackupder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
        #Checks
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
        elif isbackupder == True:
                messagebox.showwarning('Error', 'Backup already exists!')
        else:
                shutil.copytree(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
                t5 = CTkLabel(win1, text ="Backed Up!", font=('Arial',15))
                t5.grid(column=0, row=5)

def loadbackup(self):
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        isbackupder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
        #Checks
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
        elif isbackupder == False:
                messagebox.showwarning('Error', 'Backup does not exists!')
        else:
                shutil.copytree(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
                t6 = CTkLabel(win1, text ="Loaded!", font=('Arial',15))
                t6.grid(column=0, row=6)

#Window system

win1 = CTk()
win1.title(os.getcwd() + ' - FS MOD INSTALLER BY SPLAYER v0.2 (ALPHA)')
win1.iconbitmap('icon.ico')
win1.geometry()

t0 = CTkLabel(win1, text= "Floating Sandbox Mod installer v0.2", font=('Arial',20), text_color="blue")
t0.grid(column=0, rows=1)

t1 = CTkLabel(win1, text ="Please insert the mod folder location through the button below.", font=('Arial',15))
t1.grid(column=0, row=1)


browse = CTkButton(win1, text="Browse")
browse.bind("<Button-1>", browsebut)
browse.grid(column=2, row=2)

instbutton = CTkButton(win1, text="Install!")
instbutton.grid(column=0, row=3)
instbutton.bind("<Button-1>", instbut)

uninstbutton = CTkButton(win1, text="Uninstall")
uninstbutton.grid(column=0, row=4)
uninstbutton.bind("<Button-1>", uninstbut)

backupbutton = CTkButton(win1, text="Backup (Recommended before mod installation)")
backupbutton.grid(column=0, row=5)
backupbutton.bind("<Button-1>", backup)

LoadBbutton = CTkButton(win1, text="Load Backup (If Uninstall does not work)")
LoadBbutton.grid(column=0, row=6)
LoadBbutton.bind("<Button-1>", loadbackup)

win1.mainloop()
 