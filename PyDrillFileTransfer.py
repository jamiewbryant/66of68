"""
Jamie W Bryant
File Movement
"""

#Tkinter,sytem,shutil,time,os,sqlite3,datetime
import shutil, sys, time, os
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import sqlite3
from datetime import datetime, timedelta

#Box of GUI
myGUI=Tk()
myGUI.geometry("250x200+100+200")
myGUI.title('FILE MOVE')

#Set blank variables until paths are chosen
source=StringVar()
pathFrom=StringVar()
pathFrom.set("Leaving")
pathTo=StringVar()
pathTo.set("Arriving")
#source.set(filedialog.askdirectory())
destination=StringVar()
#destination.set(filedialog.askdirectory())
today=StringVar()
today.set("Last Update")

#Create or connection to database
conn = sqlite3.connect('pythontime.db', isolation_level=None)
c = conn.cursor()

#Create new table
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS updateTime(lastUpdated TEXT)')
    
#Insert the movee time into table
def insertTime():
    c.execute("INSERT INTO updateTime VALUES(datetime())") 
    
#Start createTable()    
createTable()

#Moving File Function
def movee():
    #Setting user chosen paths to variables
    source=filedialog.askdirectory()
    destination=filedialog.askdirectory()
    #Setting files inside path to variable
    files = os.listdir(source)
    #Current time for update
    today.set(datetime.now())
    #Set paths
    pathFrom.set(source)
    pathTo.set(destination)
    #Set current time to variable
    now = time.time()
    #Update table time
    insertTime()   

    #For loop to move new files
    for f in files:
        src = source + "/" + f
        dst = destination + "/" + f
        if os.stat(src).st_mtime > now - 1 * 86400:
            if os.path.isfile(src):
                shutil.move(src, dst)
                print("Last update is", datetime.now())
                
#Labels            
label1=Label(myGUI, textvariable=pathFrom, fg='Blue').grid(row=1,column=3)
label2=Label(myGUI, textvariable=pathTo, fg='Green').grid(row=2,column=3)
label3=Label(myGUI, textvariable=today,   fg='Red').grid(row=3,column=3)

#Button for movee
button2=Button(myGUI, text="  Move  ", command=movee).grid(row=5, column=3)


myGUI.mainloop()
createTable()
