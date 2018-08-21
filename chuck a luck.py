from tkinter import *
from random import randint


def creating_label(text, fontsize= 15):
    #erzeugen von labels
    text = text
    fontsize = fontsize
    label = Label(mainFenster, text=text, bg="grey", font=('Calibri',fontsize))
    return label

def creating_radiobutton(image, value):
    #erzeugen von radiobuttons
    image = image
    value = value
    radiobutton = Radiobutton(mainFenster, image=image, variable = v, value=value, indicatoron=0, command=radioactive, state=NORMAL)
    return radiobutton

def creating_button(text, fontsize, command, state=NORMAL):
    #erzeugen von buttons
    text=text
    command=command
    fontsize=fontsize
    state=state
    button = Button(mainFenster, text=text, font=('Calibri',fontsize), command=command, state=state)
    return button

def place(name, x, y, width, height):
    #setzen der Elemente
    name = name
    x = x
    y = y
    width = width
    height = height
    place = name.place(x=x, y=y, width=width, height=height)
    return place

def wurfeln():
    #wuerfeln
    global wurfel1, wurfel2, wurfel3
    wurfel1 = randint(0,6)
    wurfel2 = randint(0,6)
    wurfel3 = randint(0,6)

    if wurfel1 == 1:
        randomWurfel1.config(image=imageeWurfel[0])
    elif wurfel1 == 2:
        randomWurfel1.config(image=imageeWurfel[1])
    elif wurfel1 == 3:
        randomWurfel1.config(image=imageeWurfel[2])
    elif wurfel1 == 4:
        randomWurfel1.config(image=imageeWurfel[3])
    elif wurfel1 == 5:
        randomWurfel1.config(image=imageeWurfel[4])
    elif wurfel1 == 6:
        randomWurfel1.config(image=imageeWurfel[5])
    randomWurfel1.after(500)
    randomWurfel1.update()

    if wurfel2 == 1:
        randomWurfel2.config(image=imageeWurfel[0])
    elif wurfel2 == 2:
        randomWurfel2.config(image=imageeWurfel[1])
    elif wurfel2 == 3:
        randomWurfel2.config(image=imageeWurfel[2])
    elif wurfel2 == 4:
        randomWurfel2.config(image=imageeWurfel[3])
    elif wurfel2 == 5:
        randomWurfel2.config(image=imageeWurfel[4])
    elif wurfel2 == 6:
        randomWurfel2.config(image=imageeWurfel[5])
    randomWurfel2.after(500)
    randomWurfel2.update()

    if wurfel3 == 1:
        randomWurfel3.config(image=imageeWurfel[0])
    elif wurfel3 == 2:
        randomWurfel3.config(image=imageeWurfel[1])
    elif wurfel3 == 3:
        randomWurfel3.config(image=imageeWurfel[2])
    elif wurfel3 == 4:
        randomWurfel3.config(image=imageeWurfel[3])
    elif wurfel3 == 5:
        randomWurfel3.config(image=imageeWurfel[4])
    elif wurfel3 == 6:
        randomWurfel3.config(image=imageeWurfel[5])
    randomWurfel3.after(500)
    randomWurfel3.update()
        
    buttonWerfen.config(state=DISABLED)
    buttonAuszahlen.config(state=NORMAL)


def setzen():
    #Zum Spielen einer weiteren Runde wird ein 'Cent' abgezogen vom Konto und falls kein 'Cent' mehr übrig ist,
    #dann öffnet sich ein neues Fenster und berichtet davon
    stand = int(labelGuthaben.cget('text'))
    if stand == 0:
        keinGuthaben = Toplevel()
        keinGuthaben.title('Kein Guthaben')
        labelFehler = Label(keinGuthaben, text='Sie haben leider kein Guthaben mehr und somit haben Sie das Spiel verloren', font=('Calibri',15))
        labelFehler.pack()
    else:    
        stand = stand - 1
        labelGuthaben.config(text=str(stand))
        buttonSetzen.config(state=DISABLED)
        buttoneWurfel1.config(state=NORMAL)
        buttoneWurfel2.config(state=NORMAL)
        buttoneWurfel3.config(state=NORMAL)
        buttoneWurfel4.config(state=NORMAL)
        buttoneWurfel5.config(state=NORMAL)
        buttoneWurfel6.config(state=NORMAL)
    
def radioactive():
    #Nach dem Wählen eines Feldes, auf das man sein 'Cent' legen möchte, kann man nichts mehr ändern
    buttonWerfen.config(state=NORMAL)
    buttoneWurfel1.config(state=DISABLED)
    buttoneWurfel2.config(state=DISABLED)
    buttoneWurfel3.config(state=DISABLED)
    buttoneWurfel4.config(state=DISABLED)
    buttoneWurfel5.config(state=DISABLED)
    buttoneWurfel6.config(state=DISABLED)

def auszahlen():
    #Gewinn wird ausgezahlt
    buttonSetzen.config(state=NORMAL)
    buttonAuszahlen.config(state=DISABLED)
    stand = int(labelGuthaben.cget('text'))
    
    gewaehlterWuerfel = v.get()
    if gewaehlterWuerfel == wurfel1:
        labelGuthaben.config(text=str(stand + 1))
    if gewaehlterWuerfel == wurfel2:
        labelGuthaben.config(text=str(stand + 1))
    if gewaehlterWuerfel == wurfel3:
        labelGuthaben.config(text=str(stand + 1))

def cheat():
    #Erzeugen vom Fenster mit dem Cheat
    global cheatFenster
    cheatFenster = Tk()
    cheatFenster.title("CHEAT")
    cheatFenster.geometry("310x105")
    cheatFenster.config(bg="white")
    #Konto auffuellen     
    buttonAufladen = Button(cheatFenster, text="Konto auffüllen", font=('Calibri', 15), command=KontoAuffullen)
    buttonAufladen.place(x=20, y=20, width=200, height=25) #später umändern
    global entryAuffullen 
    entryAuffullen = Entry(cheatFenster, font=('Calibri', 15))
    entryAuffullen.place(x=240, y=20, width=50, height=25)
    #OK Button 
    buttonOK = Button(cheatFenster, text="OK", font=('Calibri', 15), command=okClick)
    buttonOK.place(x=240, y=60, width=50, height=25)
    
def KontoAuffullen():
    #Konto wird aufgefuellt mit der gewuenschten Summe 
    try:
        stand = int(labelGuthaben.cget('text'))
        aufladen = int(entryAuffullen.get())
        Ergebnis = stand + aufladen
        labelGuthaben.config(text=str(Ergebnis))
    except:
        pass

def okClick():
    #Fenster wird geschlossen durch Betätigen vom 'OK'-Button
    #cheatFenster.quit()
    cheatFenster.destroy()

def buttonOkClick():
    #Fenster wird geschlossen durch Betätigen vom 'OK'-Button
    tkFensterSpielregeln.quit()
    tkFensterSpielregeln.destroy()

def spielregeln():
    #Erzeugen des Fensters mit den Spielregeln
    global tkFensterSpielregeln
    tkFensterSpielregeln = Toplevel()
    tkFensterSpielregeln.title('Spielregeln')
    tkFensterSpielregeln.geometry('700x400')
    tkFensterSpielregeln.config(bg="white")
    #Erklärung der Spielregeln
    labelSpielregeln = Label(tkFensterSpielregeln, bg="white",
                        text='Der Spieler zuerst einen Dollar (Cent) als Einsatz. \nDiesen setzt er / sie auf eine Zahl des Spielfeldes. \nAnschließend wirft er / sie drei Würfel.\n Jetzt wird bestimmt, wie viele Würfel mit der gesetzten Spielzahl übereinstimmen.\nGibt es keine Übereinstimmungen, ist der Einsatz verloren,\nansonsten erhält der Spieler den Einsatz zurück und zusätzlich für jede Übereinstimmung einen Dollar (Cent).')
    labelSpielregeln.place(x=20, y=20, width=660, height=350)
    #Schließen des Fensters
    buttonOk = Button(tkFensterSpielregeln, text='Ok', font=('Calibri',15), command=buttonOkClick)
    buttonOk.place(x=500, y=350, width=150, height=20)

#Erzeugung vom Hauptfenster
mainFenster = Tk()
mainFenster.title("chuck a luck")
mainFenster.geometry("600x250")
mainFenster.config(bg="white")

#Öffnen vom Fenster mit den Spielregeln
spielregeln()

#Bilder der einzelen Wuerfel
imageeWurfel = [PhotoImage(file="w1.gif"),
                PhotoImage(file="w2.gif"),
                PhotoImage(file="w3.gif"),
                PhotoImage(file="w4.gif"),
                PhotoImage(file="w5.gif"),
                PhotoImage(file="w6.gif")]

#Ueberschrift - Chuck a luck
labelUberschrift = creating_label("Chuck a luck", 25)
place(labelUberschrift, 10, 10, 580, 50)

#Grid1
#Unterüberschrift - Konto
labelKonto = creating_label("Konto")
place(labelKonto, 10, 70, 180, 25)
#Anzeige vom Guthaben
labelGuthaben = creating_label("10")
labelGuthaben.place(x=85, y=135, width=45, height=30)
#Button zum Setzen vom Einsatz
buttonSetzen = creating_button("Einsatz zahlen", 15, setzen)
place(buttonSetzen, 10, 210, 180, 25)

#Grid2
#Unterueberschrift - Muenze setzen
labelZahl = creating_label("Münze setzen")
place(labelZahl, 210, 70, 180, 25)
#Muenze setzen
v = IntVar()

buttoneWurfel1 = creating_radiobutton(imageeWurfel[0], 1)
place(buttoneWurfel1, 210, 110, 30, 30)

buttoneWurfel2 = creating_radiobutton(imageeWurfel[1], 2)
place(buttoneWurfel2, 270, 110, 30, 30)

buttoneWurfel3 = creating_radiobutton(imageeWurfel[2], 3)
place(buttoneWurfel3, 330, 110, 30, 30)

buttoneWurfel4 = creating_radiobutton(imageeWurfel[3], 4)
place(buttoneWurfel4, 210, 160, 30, 30)

buttoneWurfel5 = creating_radiobutton(imageeWurfel[4], 5)
place(buttoneWurfel5, 270, 160, 30, 30)

buttoneWurfel6 = creating_radiobutton(imageeWurfel[5], 6)
place(buttoneWurfel6, 330, 160, 30, 30)
#Button zum Auszahlen vom Gewinn
buttonAuszahlen = creating_button("Gewinn auszahlen", 15, auszahlen, DISABLED)
place(buttonAuszahlen, 210, 210, 180, 25)

#Grid3
#Unterueberschrift - Wuerfel
labelWuerfel = creating_label("Würfel")
place(labelWuerfel, 410, 70, 180, 25)
#Anzeige von den Spielwuerfeln
randomWurfel1 = Label(image=imageeWurfel[5])
place(randomWurfel1, 410, 110, 30, 30)

randomWurfel2 = Label(image=imageeWurfel[5])
place(randomWurfel2, 470, 110, 30, 30)

randomWurfel3 = Label(image=imageeWurfel[5])
place(randomWurfel3, 530, 110, 30, 30)
#Button zum Werfen der Spielwuerfeln
buttonWerfen = creating_button("Würfel werfen", 15, wurfeln, DISABLED)
place(buttonWerfen, 410, 210, 180, 25)

#Cheat 
versteckt = creating_button('', 15, cheat)
place(versteckt, 585, 10, 5, 5)
       
#Aktivierung des Fensters
mainFenster.mainloop()
