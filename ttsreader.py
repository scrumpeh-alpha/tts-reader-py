import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import pyttsx3
import json

#TTS Engine: Loading it first
engine = pyttsx3.init()

#FUNCTIONS ON STARTUP

#JSON
#Load Properties for settings in the JSON
def loadJSONProperties():
    with open('settings.json') as f:
        data = json.load(f)
        
        #CHECKING COLOR SCHEME
        colorscheme = data["preferences"]["colorscheme"]
        if colorscheme == "light":
            changeLight()
        elif colorscheme == "dark":
            changeDark()
        elif colorscheme == "darker":
            changeDarker()

#Change the color property in JSON
def changeJSONPropertyColor(value):

    jsonData = {
        "preferences": {
            "colorscheme": value
        }   
    }
    
    with open('settings.json', 'w') as f:
        json.dump(jsonData, f, indent=4, sort_keys=True)

#TTS
#Function for removing new lines, and replacing them with spaces
def removeReturns(s):
    result = ""
    strings = s.split("\n")
    for i in strings:
        result += i + " "
    return result

#Main part, talking TTS
def talkTTS():

    text = textarea1.get("1.0","end-1c")
    text = removeReturns(text)
    
    wpm = textarea2.get("1.0", "end-1c")
    
    if not wpm:
        wpm = 140
    
    try:
        wpm = int(wpm)
    except:
        messagebox.showerror("Type Error", "Value is not an integer")
    
    engine.setProperty('rate', wpm)
    engine.say(text)
    engine.runAndWait()
    

def pasteText():
    try:
        text = root.clipboard_get()
        textarea1.delete(1.0,"end")
        textarea1.insert(1.0, text)
    except:
        messagebox.showerror("Incorrect Type", "The value you pasted is not text")
    
    
#SETTINGS
#Color Schemes
#Light
def changeLight():
    background = 'white'
    secondary = '#2e2e2e'
    #accent = 'red'
    fontColor = 'black'
    
    root.configure(bg=background)
    title.configure(bg=background)
    components = [L1, L2, textarea1, textarea2]
    buttons = [button1, pasteButton1]
    
    for i in components:
        i.configure(bg = background, fg=fontColor)
    
    for i in buttons:
        i.configure(bg=secondary)
    
    changeJSONPropertyColor("light")

#Dark
def changeDark():
    
    background = '#2e2e2e'
    secondary = 'black'
    #accent = 'red'
    fontColor = 'white'
    
    components = [L1, L2]
    textareas = [textarea1, textarea2]
    buttons = [button1, pasteButton1]
    title.configure(bg=background)
    root.configure(bg=background)
    
    for i in textareas:
        i.configure(bg=secondary, fg=fontColor)
    
    for i in components:
        i.configure(bg = background, fg=fontColor)
    
    for i in buttons:
        i.configure(bg=secondary)
    
    changeJSONPropertyColor("dark")

#Darker   
def changeDarker():
    background = 'black'
    secondary = '#2e2e2e'
    #accent = 'red'
    fontColor = 'white'
    
    components = [L1, L2, textarea1, textarea2]
    buttons = [button1, pasteButton1]
    
    root.configure(bg=background)
    title.configure(bg=background)
    
    for i in components:
        i.configure(bg = background, fg=fontColor)
    
    for i in buttons:
        i.configure(bg=secondary)
    
    changeJSONPropertyColor("darker")

#Main Settings Window
def createSettingsWindow():

    #secondary = '#2e2e2e'
    #accent = 'red'
    #settingsFont = tkFont.Font(family="Segoe UI", size=12)
    background = 'white'
    fontColor = 'black'
    
    settingsWindow = tk.Toplevel(root)
    settingsWindow.configure(bg=background)
    
    colorSchemeText = tk.Label(
                        settingsWindow, 
                        text="Color Scheme", 
                        bg=background, 
                        fg=fontColor)
                        
    lightButton = tk.Button(
                        settingsWindow, 
                        text="Light", 
                        command=changeLight, 
                        relief="solid", 
                        bd=1, 
                        padx=15, pady=2)
                        
    darkButton = tk.Button(
                        settingsWindow, 
                        text="Dark", 
                        command=changeDark, 
                        relief="solid", 
                        bd=1, 
                        padx=15, pady=2)
                        
    darkerButton = tk.Button(
                        settingsWindow, 
                        text="Darker", 
                        command=changeDarker, 
                        relief="solid", 
                        bd=1, 
                        padx=15, pady=2)
    
    settingsWindow.title("Settings")
    settingsWindow.minsize(200, 230)
    
    colorSchemeText.grid(row=0, column=0, padx=25, pady=4)
    
    lightButton.grid(row=0, column=1, padx=5, pady=4)
    darkButton.grid(row=1, column=1, padx=5, pady=4)
    darkerButton.grid(row=2, column=1, padx=5, pady=4)
    
    root.eval(f'tk::PlaceWindow {str(settingsWindow)} center')

#Main Frame Creation
root = tk.Tk()

#Defining Colors
background = 'black'
secondary = '#2e2e2e'
accent = 'red'
fontColor = 'white'

#Defining Font Styles
fontStyle = tkFont.Font(family="Segoe UI", size=14)
titleFont = tkFont.Font(family="Segoe UI", size=24, weight='bold')
textAreaFont = tkFont.Font(family="Segoe UI", size=12)

#Main Frame
frame = tk.Frame(root)
root.configure(bg=background)

#Defining Row Numbers
titleRow = 0
firstRow = 1
secondRow = 2
thirdRow = 3

#MENUBAR
menuBar = tk.Menu()
root.config(menu=menuBar)
#Settings Menu
settingsMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Settings", menu=settingsMenu)
settingsMenu.add_command(label="Preferences...", command=createSettingsWindow)

#FORMAT:
#(Component)
#(Grid Placement)

title = tk.Label(text="TTS Reader", bg=background, fg=accent, font=titleFont)
title.grid(row=titleRow, column=1, padx=2, pady=5)

L1 = tk.Label(text="Enter text here:", bg=background, fg=fontColor, font=fontStyle)
L1.grid(row=firstRow, column=1, padx=5, pady=10)

textarea1 = tk.Text(
                    bd=1, 
                    height=5, width=22, 
                    font=textAreaFont, 
                    bg=background, fg='white', 
                    highlightcolor=accent, 
                    highlightthickness=1, 
                    relief="solid",
                    wrap="word" )

textarea1.grid(row=firstRow, column=2, padx=10, pady=10)

button1 = tk.Button(
                    command=talkTTS, 
                    bg=secondary, fg=fontColor, 
                    activebackground='red', activeforeground='white', 
                    padx=25, pady=4, 
                    font=fontStyle, 
                    relief="solid" )

button1["text"] = "Speak"
button1.grid(row=firstRow, column=3, padx=10, pady=10)

pasteIco = tk.PhotoImage(file = "pasteIco.png")

pasteButton1 = tk.Button(
                        command=pasteText, 
                        bg=secondary, fg=fontColor, 
                        activebackground='red', activeforeground=fontColor, 
                        padx=16, pady=8, 
                        font=fontStyle, 
                        image=pasteIco, 
                        relief="solid" )
   
pasteButton1.grid(row=secondRow, column=2)

L2 = tk.Label(text="Enter WPM:", bg=background, fg=fontColor, font=fontStyle)
L2.grid(row=secondRow, column=3, padx=1, pady=1)

textarea2 = tk.Text(
                    bd=1, 
                    height=1, width=4, 
                    font=fontStyle, 
                    bg=secondary, fg=fontColor, 
                    highlightcolor=accent, highlightthickness=1,
                    relief="solid" )
  
textarea2.grid(row=thirdRow, column=3, padx=10, pady=10)

#Loading Color Preference
try:
    loadJSONProperties()
except Exception as e:
    messagebox.showerror("Error", e)

frame.master.title("TTS Reader")
frame.master.minsize(450, 110)

root.eval('tk::PlaceWindow . center') #Places Window in the center
root.mainloop()