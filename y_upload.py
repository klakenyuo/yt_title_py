# Exercice utilisant la bibliothèque graphique tkinter et le module math
from youtube import *
from tkinter import *
from math import *
global v
global title_video
global link

# show the titile of the yt video
def show_title():
    global title_video
    try : 
        get_link("<Return>")
        v = Video(link)
        title_video = str(v.title)
        chaine.configure(text = title_video)
    except :
        title_video = "Erreur surevenue lors de l'affichage du titre de la vidéo"
        chaine.configure(text = title_video)
    return

# get the link in a variable
def get_link(event):
    global link
    link = str(entree.get())
    return

# reset the entry
def reset():
    entree.delete(0,END)

# ----- Main -----
title_video="Aucun titre pour l'instant"
link=""
text_edit =""
fenetre = Tk()
entree = Entry(fenetre,textvariable=text_edit)
entree.bind("<Return>", get_link)
chaine = Label(fenetre)
b0 = Button(fenetre,text='Titre de la Video',command=show_title)
b_exit = Button(fenetre,text='Exit',command=fenetre.quit)
b_reset = Button(fenetre,text='reset',command=reset)
chaine.pack()
entree.pack()
b0.pack()
b_exit.pack()
b_reset.pack()
fenetre.mainloop()