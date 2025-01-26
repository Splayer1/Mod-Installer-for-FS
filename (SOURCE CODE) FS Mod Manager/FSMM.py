#Import stuff
import os
import shutil
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from customtkinter import * 

set_default_color_theme("blue")

modpath = str()

#FUNCTIONS
global mod
mod = 'no-way.html' 
#Function for the browse button
def browsebut(self):
        global modpath
        modselect = filedialog.askdirectory()
        modpath = str(modselect)
        t2 = CTkLabel(win1, text = modpath, font=('Arial',15), bg_color='yellow')
        t2.place(x=150 ,y=50)

#Function for the install button
def instbut(self):
    ismodder = os.path.exists(os.path.join(modpath,'Floating Sandbox'))
    isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
    #Checks
    if ismodder == False:
            messagebox.showwarning('Error', 'The mod file does not exist or is in inavlid format!')
    elif isfsder == False:
        messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
    else:
        global mod
        mod = str(os.listdir(os.path.join(modpath, 'src'))[0])
        shutil.copytree(os.path.join(modpath,'Floating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
        shutil.copytree(os.path.join(modpath,'src'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox/Mods'), dirs_exist_ok = True)
        global t3
        t3 = CTkLabel(win1, text ="Installed!", font=('Arial',15))
        t3.place(x=150 ,y=75)
        refresh(self)
        win1.after(4000, t3.destroy)
        #FUNCTION TO DESTROY T3 AND SIMILAR LABEL AFTER FEW SECONDS OF EXECTUION!!!

#Function for the uninstall button 
def uninstbut(self):
        global mod
        ismodder = os.path.exists(os.path.join(modpath,'Floating Sandbox'))
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        isfsoldder = os.path.exists(os.path.join(modpath,'FSold'))
        ismodmodder = os.path.exists(os.path.join((os.path.join(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), 'Mods')), mod))
        #Checks
        if ismodder == False:
               messagebox.showwarning('Error', 'The mod file does not exist or is in inavlid format!')
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating' Sandbox folder does not exist!")
        elif isfsoldder == False:
                messagebox.showwarning('Error', "'FSold folder' does not exist!")
        elif ismodmodder == False:
                messagebox.showwarning('Error', "Mod does not exist!")
        else:
                with open(os.path.join((os.path.join(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), 'Mods')), mod)) as f:
                        lines1 = [line1.rstrip() for line1 in f]
                        for line1 in lines1:
                                if os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), line1)):
                                        os.remove(os.path.join(os.environ.get('LOCALAPPDATA'), line1)) 
                                        shutil.copytree(os.path.join(os.path.join(modpath,'FSold'), 'Floating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
                                else:
                                        messagebox.showwarning('Error', 'The mod is already uninstalled!')
                                        StopIteration()
                t4 = CTkLabel(win1, text ="Uninstalled!", font=('Arial',15))
                t4.place(x=150 ,y=100)
                os.remove(os.path.join((os.path.join(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), 'Mods')), mod))
                mod='no-way.html'
                refresh(self)
                win1.after(4000, t4.destroy)

#Function for the backup button
def backup(self):
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        isbackupder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
        #Checks
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
        elif isbackupder == True:
                messagebox.showwarning('Error', 'Backup already exists!')
        else:
                sure = messagebox.askyesno('Are you sure?', 'Do you want to create a backup?')
                if sure == True:
                        shutil.copytree(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
                        t5 = CTkLabel(win1, text ="Backed Up!", font=('Arial',15))
                        t5.place(x=300 ,y=125)
                        win1.after(4000, t5.destroy)
                else:
                       pass

#Function of the load backup button
def loadbackup(self):
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'))
        isbackupder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
        #Checks
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating Sandbox' file does not exist!")
        elif isbackupder == False:
                messagebox.showwarning('Error', 'Backup does not exists!')
        else:
                sure = messagebox.askyesno('Are you sure?', 'Do you want to load backup? This will revert all the changes until the backup!')
                if sure == True:
                        shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Floating Sandbox'))
                        shutil.copytree(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'), os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), dirs_exist_ok = True)
                        t6 = CTkLabel(win1, text ="Backup Loaded!", font=('Arial',15))
                        t6.place(x=300 ,y=150)
                        refresh(self)
                        win1.after(4000, t6.destroy)
                else:
                       pass

#Function for the delete backup button
def delbackup(self):
        isbackupder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
        #Checks
        if isbackupder==False:
               messagebox.showwarning('Error', 'There are no backups!')
        else:
                sure = messagebox.askyesno('Are you sure?', 'Do you want to delete the backup? This cannot be reverted!')
                if sure == True:
                       shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'FSBackup'))
                       t7 = CTkLabel(win1, text ="Backup Deleted!", font=('Arial',15))
                       t7.place(x=300 ,y=175)
                       win1.after(4000, t7.destroy)
                else:
                       pass

#Function for launch game button
def launch(self):
        isfsder = os.path.exists(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox/FloatingSandbox.exe'))
        #Checks
        if isfsder == False:
                messagebox.showwarning('Error', "'Floating Sandbox' does not exist!")
        else:
                os.startfile(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox/FloatingSandbox.exe'))

#Function for help button
def help(self):
        #MAKE FUNCTION TO OPEN HELP YT OR GITHUB DOCUMENTATION
        #WORK IN PROGRESS, COMING IN LATER VERSIONS
        pass

#Windows and buttons system

win1 = CTk()
win1.title('FLOATING SANDBOX MOD MANAGER BY SPLAYER v0.3 (ALPHA) - ' + os.getcwd())
win1.geometry('1000x500')

t0 = CTkLabel(win1, text= "Floating Sandbox Mod Manager v0.3", font=('Arial',20), text_color="blue")
t0.pack(anchor=N)

t1 = CTkLabel(win1, text ="Please insert the mod folder location through the browse button below.", font=('Arial',15))
t1.place(x=0 ,y=25)

browse = CTkButton(win1, text="Browse")
browse.bind("<Button-1>", browsebut)
browse.place(x=0 ,y=50)

instbutton = CTkButton(win1, text="Install!")
instbutton.place(x=0 ,y=75)
instbutton.bind("<Button-1>", instbut)

uninstbutton = CTkButton(win1, text="Uninstall")
uninstbutton.place(x=0 ,y=100)
uninstbutton.bind("<Button-1>", uninstbut)

backupbutton = CTkButton(win1, text="Backup (Recommended before mod installation)")
backupbutton.place(x=0 ,y=125)
backupbutton.bind("<Button-1>", backup)

LoadBbutton = CTkButton(win1, text="Load Backup (If Uninstall does not work)")
LoadBbutton.place(x=0 ,y=150)
LoadBbutton.bind("<Button-1>", loadbackup)

DelBbutton = CTkButton(win1, text="Delete Backup")
DelBbutton.place(x=0 ,y=175)
DelBbutton.bind("<Button-1>", delbackup)

launchbutton = CTkButton(win1, text="Launch Floating Sandbox")
launchbutton.place(x=0, y=200)
launchbutton.bind("<Button-1>", launch)

#Help button coming in later versions.
# Help = CTkButton(win1, text="Help")
# Help.place(x=0, y=225)
# Help.bind("<Button-1>", help)

#Stuff for refresh and displaying mods stuff
t8 = CTkLabel(win1, text= "Installed Mods", font=('Arial',17), bg_color='yellow')
t8.place(x=725, y=25)

global frm
frm = CTkFrame(win1, 200, 100, fg_color=None)
frm.place(x=725, y=55)

global label
label = CTkLabel(frm, text="", font=('Arial',15))
label.pack(anchor=SW)

def refresh(self):
       global frm
       global label
       global mods
       global mod
       frm.destroy
       frm = CTkFrame(win1, 200, 100, fg_color=None)
       frm.place(x=725, y=55)
       modlist = os.listdir(os.path.join(os.path.join(os.environ.get('LOCALAPPDATA'), 'FLoating Sandbox'), 'Mods'))
       mods = [os.path.splitext(x)[0] for x in modlist]

       for item in mods:
                label = CTkLabel(frm, text="● " + item, font=('Arial',15))
                label.pack(anchor=SW)

refreshbutton = CTkButton(win1, text="Refresh")
refreshbutton.place(x=850, y=25)
refreshbutton.bind("<Button-1>", refresh)

sep = ttk.Separator(win1, orient='vertical')
sep.place(x=700, y=25, width=10, height=800)

win1.mainloop()
