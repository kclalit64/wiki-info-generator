import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import pyttsx3
from tkinter import *
from PIL import ImageTk,Image
import random

interface=Tk()
interface.title("Wikipedia Article Generator")
interface.iconbitmap('wikipedia_globe_icon.ico')
interface.configure(background='black')
color_codes=['#90eeed','#d681ff','#faf1ae','#57b1f4','#e5dcd4']

''' color codes::
    cyan:#90eeed
    light putple:#d681ff
    light yellow:#faf1ae
    light blue:#57b1f4
    light grey:#e5dcd4'''

Label(interface,text="                                        ",bg="black",font='arial 30 bold').grid(row=0,column=0)
Label(interface,text="   Wikipedia Article Generator  ",bg="black",fg="white",font=('Times New Roman','40','bold')).grid(row=0,column=1)
wiki_img= ImageTk.PhotoImage(Image.open("wiki_logo.ico"))
wiki_img_label= Label(image=wiki_img,bg="black").grid(row=0,column=3)

custom_entry=Entry(interface,width=43,font=('Comic Sans MS','20'),borderwidth=4)
custom_entry.grid(row=5,column=1,pady=40)
custom_entry.insert(0,"*Enter custom topic here*")

def redirectx():
    webbrowser.open(url_x)
    
def deletex():
    topic_name.destroy()
    abstract.destroy()

def textx():
    deletex()
    global topic_name
    topic_name=Label(interface,text="Topic  >>  "+title.upper(),font=('Cinzel Black',25),bg="black",fg=random.choice(color_codes))
    topic_name.grid(row=15,column=1)
    topic_name.update()
    Label(interface,text="\n",bg='black').grid(row=16,column=0)
    global abstract
    abstract = Message(interface,text=abr,font=('Century',15),aspect=350,bg=random.choice(color_codes),justify=CENTER)
    
    abstract.grid(row=200,column=1)
    abstract.update()
    custom_entry.delete(0,END)

def speechx():
    engine = pyttsx3.init()
    engine.setProperty("rate",140)
    engine.say(abr)
    engine.runAndWait()
    
def intro():
    soup = BeautifulSoup(url.content, "html.parser")
    etr=soup.find('div',class_='mw-parser-output')
    global abr
    abr = etr.find_next("p", class_=None)
    if abr:
        for sup in abr.select("sup"):
            sup.extract()
    abr=abr.text
    abr=abr[:400]+"....\nTo know more, visit the wikipedia page"
    textx()
    speechx()
    
    
def customx():
    global title    
    title=custom_entry.get()
    title_x=title.replace(" ","_")
    global url
    url = requests.get("https://en.wikipedia.org/wiki/%s" % title_x)
    intro()
    global url_x
    url_x = "https://en.wikipedia.org/wiki/%s" % title_x
    Label(interface,text="\n",bg='black').grid(row=202,column=1)
    redirect_=Button(interface,text="Wikipedia Page",font=('Comic Sans MS',10),command=redirectx,pady=3,padx=38,bg="grey")
    redirect_.grid(row=205,column=1)   

def randomx():
    custom_entry.delete(0,END)
    global url
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    global soup
    soup = BeautifulSoup(url.content, "html.parser")
    global title
    title = soup.find(class_="firstHeading").text                            
    intro()
    title_x=title.replace(" ","_")
    global url_x
    url_x = "https://en.wikipedia.org/wiki/%s" % title_x
    Label(interface,text="\n",bg='black').grid(row=202,column=1)
    redirect_=Button(interface,text="Wikipedia Page",font=('Comic Sans MS',10),command=redirectx,pady=3,padx=38,bg="grey")
    redirect_.grid(row=205,column=1)
        
button_custom=Button(interface,text="Enter",command=customx,padx=20,pady=6,width=10,font=('arial','13'),borderwidth=4).grid(row=5,column=2)
Label(interface,text="\n",bg='black').grid(row=6,column=0)
button_random=Button(interface,text="GENERATE RANDOM ARTICLE",font=('Times New Roman','20','bold'),command=randomx,padx=20,pady=5,bg='yellow').grid(row=10,column=1)
Label(interface,text="\n\n\n",bg='black').grid(row=11,column=0)
topic_name=Label(interface,text="     ",font=('Bradely Hand ITC',25),bg='black')
topic_name.grid(row=15,column=1)
abstract = Message(interface,text="    ",bg='black')
abstract.grid(row=200,column=1)

interface.mainloop()