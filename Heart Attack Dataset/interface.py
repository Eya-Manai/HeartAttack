from  tkinter import * 
from datetime import date
from  tkinter.ttk import Combobox 
import tkinter as tk 
from tkinter import ttk
import os 
import matplotlib 
matplotlib.use("tkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
background="#f0ddd5"
frameBg="#62a7ff"
framefg="#fefbfb"
root=Tk()
root.title("Heart Attack Predection System")
root.geometry('1450x750') 
root.resizable(False,False)
root.config(bg=background)
image_Icon=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\heart.png')
root.iconphoto(False,image_Icon)

#Header Section
logo=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\doctor.png')

#Header Section2
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=0)

#Frame
headingEntry=Frame(root,width=800,height=190, bg="#df2d4b")
headingEntry.place(x=600,y=20)

Label(headingEntry,text="Regestration N0",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=0)
Label(headingEntry,text="Date",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=0)
Label(headingEntry,text="Patient Name",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=90)
Label(headingEntry,text="Birth Year",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=90)

entryImage=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\rectangle.png')
entryImage2=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\rectangle2.png')

Label(headingEntry,image=entryImage,bg="#df2d4b").place(x=20,y=30)
Label(headingEntry,image=entryImage,bg="#df2d4b").place(x=420,y=30)
Label(headingEntry,image=entryImage2,bg="#df2d4b").place(x=20,y=120)
Label(headingEntry,image=entryImage2,bg="#df2d4b").place(x=420,y=120)

###RegestrationN0Input(int)
Regestration=IntVar()
regestrationEntry=Entry(headingEntry,textvariable=Regestration,width=30,font="arial 15",bg="#0e5363",fg="white",bd=0, insertbackground="white")
regestrationEntry.place(x=30,y=45)

###RegestrationDateInput(str)
Date=StringVar()
today=date.today()
d1=today.strftime("%d/%m/%Y")
dateEntry=Entry(headingEntry,textvariable=Date,width=15,font="arial 15",bg="#0e5363",fg="white",bd=0,insertbackground="white")
dateEntry.place(x=535,y=45)
Date.set(d1)

###RegestrationNameInput(str)
Name=StringVar()
nameEntry=Entry(headingEntry,textvariable=Name,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
nameEntry.place(x=30,y=130)

###RegestrationBirthDateInput(str)
BD=IntVar()
BDEntry=Entry(headingEntry,textvariable=BD,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
BDEntry.place(x=450,y=130)

####################################################################################################
DetailsEntry=Frame(root,width=550,height=262,bg="#dbe0e3")
DetailsEntry.place(x=30,y=450)

#RadioButtons
#Fbs: fasting blood sugar 
# Ex Angina: Exercise angina
Label(DetailsEntry,text="sex:",font="arial 13",bg=frameBg,fg=framefg).place(x=10,y=10)
Label(DetailsEntry,text="Fbs:",font="arial 13",bg=frameBg,fg=framefg).place(x=180,y=10)
Label(DetailsEntry,text="Ex An:",font="arial 13",bg=frameBg,fg=framefg).place(x=335,y=10)


def selection():
    if gen.get()==0:
        gender=0
        return gender
        print(gender)
    elif gen.get()==1:
        gender=1
        return gender
        print(gender)
    else:
        print(gen)

    

def selection2():
    if Fbs.get()==1:
        fbs=1
        return fbs
        print(fbs)

    elif Fbs.get()==0:
        fbs=0
        return fbs
        print(fbs)
    else:
        print(fbs)

    

def selection3():
    if ExAngina.get()==1:
        exa=1
        return exa
        print(exa)

    elif ExAngina.get()==0:
        exa=0
        return exa
        print(exa)
    else:
        print(exa)
#Gender
gen=IntVar(value=-1)
R1=Radiobutton(DetailsEntry,text="Male",variable=gen,value=1,command=selection)
R2=Radiobutton(DetailsEntry,text="Male",variable=gen,value=0,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

#FBS
Fbs=IntVar(value=-1)
R3=Radiobutton(DetailsEntry,text="True",variable=Fbs,value=1,command=selection2)
R4=Radiobutton(DetailsEntry,text="False",variable=Fbs,value=0,command=selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

#ExerciceAngina
ExAngina=IntVar(value=-1)
R5=Radiobutton(DetailsEntry,text="Yes",variable=ExAngina,value=1,command=selection3)
R6=Radiobutton(DetailsEntry,text="No",variable=ExAngina,value=0,command=selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)


##################################ComBox##############################################

Label(DetailsEntry,text="Chest Pain:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=50)
Label(DetailsEntry,text="Resting ER:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=90)
Label(DetailsEntry,text="ST slope:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=130)
Label(DetailsEntry,text="Class:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=170)
Label(DetailsEntry,text="Smoking:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=210)


def slection4():
    input=cp_combox.get()
    if input=="1=typical angina":
        return(1)
    elif input=="2=atypical angina":
        return(2)
    elif input=="3=non-anginal pain":
        return(3)
    elif input=="4=asymptomatic":
        return(4)
    else:
        print(ExAngina)
    
def slection5():
    input=resting_combox.get()
    if input=="0=normal":
        return(0)
    elif input=="1=ST abnormality":
        return(1)
    elif input=="2=hypertrophy":
        return(2)
        

cp_combox=Combobox(DetailsEntry,values=["1=typical angina","2=atypical angina","3=non-anginal pain","4=asymptomatic"],font="arial 13",state="r",width=14).place(x=105,y=50)
resting_combox=Combobox(DetailsEntry,values=["0=normal","1=ST abnormality","2=hypertrophy"],font="arial 13",state="r",width=14).place(x=105,y=90)
stSlope_combox=Combobox(DetailsEntry,values=["0=upsloping","2=flat","3=downsloping"],font="arial 13",state="r",width=14).place(x=105,y=130)
class_combox=Combobox(DetailsEntry,values=["Normal","Heart disease"],font="arial 13",state="r",width=14).place(x=105,y=170)


##################################Data Entry Box##############################################
Label(DetailsEntry,text="Blood Pressure:",font="arial 13",width=15,bg=frameBg,fg=framefg).place(x=260,y=50)
Label(DetailsEntry,text="Cholesterol:",font="arial 13",width=15,bg=frameBg,fg=framefg).place(x=260,y=90)
Label(DetailsEntry,text="Max Heart rate:",font="arial 13",width=15,bg=frameBg,fg=framefg).place(x=260,y=130)
Label(DetailsEntry,text="Old Peak:",font="arial 13",width=15,bg=frameBg,fg=framefg).place(x=260,y=170)



bloodP=StringVar()
chol=StringVar()
maxHr=StringVar()
oldPeak=StringVar()

bloodPEntry=Entry(DetailsEntry,textvariable=bloodP,width=10,font="arial 13",bg="#ededed",fg="#222222",bd=0).place(x=410,y=50)
cholEntry=Entry(DetailsEntry,textvariable=chol,width=10,font="arial 13",bg="#ededed",fg="#222222",bd=0).place(x=410,y=90)
maxHrEntry=Entry(DetailsEntry,textvariable=maxHr,width=10,font="arial 13",bg="#ededed",fg="#222222",bd=0).place(x=410,y=130)
oldpeakEntry=Entry(DetailsEntry,textvariable=oldPeak,width=10,font="arial 13",bg="#ededed",fg="#222222",bd=0).place(x=410,y=170)

##################################Report##############################################
reportImage=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\Report.png')
reportBackground=Label(image=reportImage,bg=background)
reportBackground.place(x=1120,y=340)
report=Label(root,font="arial 25 bold",text="Hello",bg="white",fg="red").place(x=1170,y=550)
report1=Label(root,font="arial 10 bold",text="Hello",bg="white").place(x=1130,y=610)

##################################Graph##############################################
graph_image=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\graph.png')
Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)


##################################Button##############################################
analysis_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\Analysis.png')
Button(root,image=analysis_Button,bd=0,bg=background,cursor="hand1").place(x=1130,y=240)

##################################InfoButton##############################################
info_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\info.png')
Button(root,image=info_Button,bd=0,bg=background,cursor="hand2").place(x=10,y=240)

##################################SaveButton##############################################
save_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\save.png')
Button(root,image=save_Button,bd=0,bg=background,cursor="hand2" ,width=50,height=50).place(x=1350,y=250)

##################################Smooking Button##############################################
button_mode=True
choice="smoking"

def changeMode():
    global button_mode
    global choice
    if button_mode:
        choice="non_smoking"
        mode.config(image=non_smooking_Icon,activebackground="white")
        button_mode=False
    else:
        choice="smoking"
        mode.config(image=smooking_Icon,activebackground="white")
        button_mode=True
    print(choice)

smooking_Icon=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\smoker.png')
non_smooking_Icon=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\nonsmoker.png')
mode=Button(root,image=smooking_Icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changeMode)
mode.place(x=135,y=656)

##################################Log out Button##############################################

logOut_icon=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\logout.png')
logOut_Button=Button(root,image=logOut_icon,bd=0,bg="#df2d4b",cursor="hand2")
logOut_Button.place(x=1375,y=55)






root.mainloop()

