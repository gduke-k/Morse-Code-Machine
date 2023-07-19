from tkinter import *
from playsound import playsound
import time

#Project by Gaurav Kumar

root = Tk()
root.title("MORSE CODE MACHINE")
width = 600 
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height-(height/4))
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.config(bg='grey30')

MORSE_DICT = { 'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----',' ':'/'}

def start_enryption():
    message = messagebox.get("1.0", "end-1c")
    message=message.upper()
    message= " ".join(MORSE_DICT[i] for i in message)
    morsebox.delete("1.0","end")
    morsebox.insert(INSERT,message)

def start_deryption():
    message = morsebox.get("1.0", "end-1c")
    REV_DICT={i:j for j,i in MORSE_DICT.items()}
    rev_message= " ".join(REV_DICT[i] for i in message.split(" "))
    messagebox.delete("1.0","end")
    messagebox.insert(INSERT,rev_message)

def play_morse():
    message = morsebox.get("1.0", "end-1c")
    for i in message:
        if i ==".":
            playsound("short.mp3")
            time.sleep(0.3)
        elif i =="-":
            playsound("long.mp3")
            time.sleep(0.3)
        elif i=="/" or i == " ":
            time.sleep(0.5)
        else:
            print("Invilid Character!")

#GUI Parts
leftframe=Frame(root,height=300,width=150,bg='grey30')
leftframe.grid(row=0,column=0,sticky=NW)
rightframe=Frame(root,height=300,width=450,bg='grey30')
rightframe.grid(row=0,column=1,sticky=NE)

encrypt=Button(leftframe,height=4,width=15,text="Encrypt",bg='grey95',relief=FLAT, command=start_enryption)
encrypt.grid(row=0,column=0,padx=20,pady=10)
decrypt=Button(leftframe,height=4,width=15,text="Decrypt",bg='grey95',relief=FLAT, command=start_deryption)
decrypt.grid(row=1,column=0,padx=20,pady=10)
play=Button(leftframe,height=4,width=15,text="Play",bg='grey95',relief=FLAT,command=play_morse)
play.grid(row=2,column=0,padx=20,pady=10)

messagebox=Text(rightframe, height = 7, width = 50)
messagebox.grid(row=0,column=0,padx=10,pady=10)
morsebox=Text(rightframe, height = 7, width = 50)
morsebox.grid(row=1,column=0,padx=10,pady=10)

root.wm_attributes('-toolwindow', 'True')
root.resizable(False,False)
root.mainloop()
