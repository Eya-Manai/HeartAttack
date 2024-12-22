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
from datetime import date
from tkinter import messagebox

background="#f0ddd5"
frameBg="#62a7ff"
framefg="#fefbfb"
root=Tk()
root.title("Heart Attack Predection System")
root.geometry('1450x750') 
root.resizable(False,False)
root.config(bg=background)

def Info():
    icon_Window=Toplevel(root)
    icon_Window.geometry("1000x600+100+100")
    icon_Window.title("Info")

    #iconImage

    icon_image=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\info.png')
    icon_Window.iconphoto(False,icon_image)

    #Heading 
    Label(icon_Window,text="Information related to dataset",font="robot 17 bold").pack(padx=20,pady=20)

    #Label
    Label(icon_Window,text="Age- Age in years ",font="arial 11").place(x=20,y=100) 
    Label(icon_Window,text="Sex- Sex 1 = male, 0= female",font="arial 11").place(x=20,y=130) 
    Label(icon_Window,text="Chest pain type- Chest Pain Type Value 1: typical angina,Value 2: atypical angina, Value 3: non-anginal pain,Value 4: asymptomatic ",font="arial 11").place(x=20,y=160) 
    Label(icon_Window,text="Resting bp s - Resting blood pressure in mm Hg",font="arial 11").place(x=20,y=190) 
    Label(icon_Window,text="Cholesterol - serum cholesterol in mg/dl",font="arial 11").place(x=20,y=220) 
    Label(icon_Window,text="Fbs- (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)",font="arial 11").place(x=20,y=250) 
    Label(icon_Window,text=("Resting ecg - resting electrocardiogram results Value 0: normal , Value 1: having ST-T wave abnormality ST elevation or depression of > 0.05 mV "),font="arial 11").place(x=20, y=280)
    Label(icon_Window,text=("    Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria"),font="arial 11").place(x=20, y=310)
    Label(icon_Window,text="Max heart rate - maximum heart rate achieved 71–202",font="arial 11").place(x=20,y=340) 
    Label(icon_Window,text="Oldpeak =ST - oldpeak Unit depression",font="arial 11").place(x=20,y=370) 
    Label(icon_Window,text="ST slope -the slope of the peak exercise ST segment Value 1: upsloping, Value 2: flat ,Value 3: downsloping",font="arial 11").place(x=20,y=400) 
    Label(icon_Window,text="Class- target  1=heart disease, 0=Normal",font="arial 11").place(x=20,y=430) 
    icon_Window.mainloop()






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

def Clear():
    Name.get("")
    BD.get("")
    bloodP.get("")
    chol.get("")
    maxHr.set("")
    oldPeak.set("")

def Analysis():
    name=Name.get()
    D1=Date.get()
    today=date.today()

    try:
        B=selection()
    except:
        messagebox.showerror("Gender Error","Please select a gender")

    try:
        C=selection2()
    except:
        messagebox.showerror("Fbs Error","Please check if (fasting blood sugar>120 mg/dl)")

    try:
        D=selection3()
    except:
        messagebox.showerror("Exercice Angina Error","Please select the exercice angina")
    try:
        E=int(slection4())
    except:
        messagebox.showerror("Chest Pain Error","Please select chest pain value")
    
    try:
        F=int(slection5())
    except:
        messagebox.showerror("Resting","Please select the resting electrocardiogram results")
        
        



def selection():
    gender = gen.get()
    if gender == -1:
        raise ValueError("Gender not selected")
    elif gender == 0:
        print("Female")
    elif gender == 1:
        print("Male")
    return gender

    

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

#Gender
gen=IntVar(value=-1)
R1=Radiobutton(DetailsEntry,text="Male",variable=gen,value=1,command=selection)
R2=Radiobutton(DetailsEntry,text="Female",variable=gen,value=0,command=selection)
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
Button(root,image=analysis_Button,bd=0,bg=background,cursor="hand1",command=Analysis).place(x=1130,y=240)

##################################InfoButton##############################################
info_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\info.png')
Button(root,image=info_Button,bd=0,bg=background,cursor="hand2",command=Info).place(x=10,y=240)

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

#To close window
def Logout():
    root.destroy()

logOut_icon=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\off.png')
logOut_Button=Button(root,image=logOut_icon,bd=0,bg="#df2d4b",cursor="hand2", command=Logout)
logOut_Button.place(x=1375,y=55)


root.mainloop()

def Logout():
    root.destroy()

