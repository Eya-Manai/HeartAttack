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
import pickle
import sklearn

background="#f0ddd5"
frameBg="#477dba"
framefg="#fefbfb"
root=Tk()
root.title("Heart Attack Predection System")
root.geometry('1450x750') 
root.resizable(False,False)
root.config(bg=background)
print(__file__)

with open(r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\modelthis.pkl',"rb") as model_File:
    rf_model=pickle.load(model_File)
with open(r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\scaler.pkl',"rb") as scaler_File:
    scaler=pickle.load(scaler_File)



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
Label(headingEntry,text="Age",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=90)

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
age=IntVar()
ageEntry=Entry(headingEntry,textvariable=age,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
ageEntry.place(x=450,y=130)

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
    age.get("")
    bloodP.get("")
    chol.get("")
    maxHr.set("")
    oldPeak.set("")




def Analysis():
    try:
        name=Name.get()
    except:
        messagebox.showerror("Age Error","Please enter the Name")
        return
    try:
        A=getAge()
    except:
        messagebox.showerror("Age Error","Please enter patient age a number>0")
        return
    try:
        B=getGender()
    except:
        messagebox.showerror("Gender Error","Please select a gender")
        return

    try:
        C=Getfbs()
    except:
        messagebox.showerror("Fbs Error","Please check if (fasting blood sugar>120 mg/dl)")
        return

    try:
        D=getExAngina()
    except:
        messagebox.showerror("Exercice Angina Error","Please select the exercice angina")
        return

    try:
        E=int(getChestPain())
    except:
        messagebox.showerror("Chest Pain Error", "Please select chest pain value")
        return

    try:
        F=int(getResting())
    except:
        messagebox.showerror("Resting Er Error", "Please select resting electrocardiogram results")
        return
    try:
        G=int(get_St_Slope())
    except:
        messagebox.showerror("ST slope Error", "Please select the slope of the peak exercise ST segment")
        return
    try:
        H=int(getClass())
    except:
        messagebox.showerror("Class Error", "Please check if the patient has already heart disease")
        return

    try:
        I=int(bloodP.get())
    except:
        messagebox.showerror("Blood Pressure Error", "Please enter blood pressure value")
        return
    try:
        J=int(chol.get())
    except:
        messagebox.showerror("Cholesterol Error", "Please enter cholesterol value")
        return
    try:
        K=int(maxHr.get())
    except:
        messagebox.showerror("Maximun Heart rate Error", "Please enter Max heart rate value")
        return
    
    try:
        L=float(oldPeak.get())
    except:
        messagebox.showerror("Old peak Error", "Please enter old peak value")
        return
        
    
    print(f"A is Age: {A} years")
    print(f"B is Sex: {'Male' if B == 1 else 'Female'}")
    print(f"C is Fasting Blood Sugar: {'> 120 mg/dl' if C == 1 else '<= 120 mg/dl'}")
    print(f"D is Exercise-Induced Angina: {'Yes' if D == 1 else 'No'}")
    print(f"E is Chest Pain Type: {'Typical Angina' if E == 1 else 'Atypical Angina' if E == 2 else 'Non-Anginal Pain' if E == 3 else 'Asymptomatic'}")
    print(f"F is Resting Electrocardiogram Results: {'Normal' if F == 0 else 'ST-T Wave Abnormality' if F == 1 else 'Probable or Definite Left Ventricular Hypertrophy'}")
    print(f"G is ST Segment Slope: {'Upsloping' if G == 1 else 'Flat' if G == 2 else 'Downsloping'}")
    print(f"H is Class: {'Heart Disease' if H == 1 else 'Normal'}")
    print(f"I is Blood Pressure: {I} mmHg")
    print(f"J is Cholesterol: {J} mg/dl")
    print(f"K is Maximum Heart Rate Achieved: {K} bpm")
    print(f"L is Old Peak: {L}")

                
    #Fist Graph 
    f=Figure(figsize=(4,4),dpi=100)
    a=f.add_subplot(111)
    a.plot(["Sex","Fbs","ExAng"],[B,C,D])
    canvas=FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=580,y=240)

    #Second Graph 
    f2=Figure(figsize=(5,5),dpi=100)
    a2=f2.add_subplot(111)
    a2.plot(["Age","Bp","Chol","MaxHrt"],[A,I,J,K])
    canvas=FigureCanvasTkAgg(f2)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=860,y=240)
    
    #Third Graph 
    f3=Figure(figsize=(4,4),dpi=100)
    a3=f3.add_subplot(111)
    a3.plot(["Chest Pain","Resting","Old peak"],[E,F,L])
    canvas=FigureCanvasTkAgg(f3)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=580,y=500)

    #Forth Graph 
    f4=Figure(figsize=(5,5),dpi=100)
    a4=f4.add_subplot(111)
    a4.plot(["Slope","MaxHrt"],[G,K])
    canvas=FigureCanvasTkAgg(f4)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=860,y=500)
    
    ##################################Report##############################################
    report=Label(root,font="arial 25 bold",text="Hello",bg="white",fg="red")
    report.place(x=1190,y=550)
    report1=Label(root,font="arial 10 bold",text="Hello",bg="white")
    report1.place(x=1190,y=610)
    #Input Data age sex chestpain Hr exangina oldpeak slope
    
    input_data=[[A,B,E,K,D,L,G]]
    scaled_input=scaler.transform(input_data)
    print(input_data)
    predection=rf_model.predict(scaled_input)
    print(predection[0])
    if(predection[0]==0):
        print("The Person does not have a Heart attack ")
        report.config(text=f"Report:{0}",fg="#8dc63f")
        report1.config(text=f"{name},do not have a heart attack",fg="#8dc63f")
    else:
        print("The Person risks to have a Heart attack attack")
        report.config(text=f"Report:{1}",fg="#ed1c24")
        report1.config(text=f"{name}, risks to have a heart attack",fg="#FF0000")
        
    
def getAge():
    try:
        patient_age = age.get()
        if patient_age <= 0:
            raise ValueError("Age must be greater than 0")
        print(f"Patient age recorded: {patient_age} years")
        return patient_age
    except (TclError, ValueError) as e:
        raise ValueError("Invalid age value")

def getGender():
    gender = gen.get()
    if gender == -1:
        raise ValueError("Gender not selected")
    elif gender == 0:
        print("Female")
    elif gender == 1:
        print("Male")
    return gender


def Getfbs():
    fbs = Fbs.get()
    if fbs not in [0, 1]:
        raise ValueError("FBS not selected")
    print(f"FBS value: {fbs}")
    return fbs

def getExAngina():
   angina = ExAngina.get()
   if angina not in [0, 1]:
        raise ValueError("Exercise Angina not selected")
   print(f"Exercise Angina value: {angina}")
   return angina

def getChestPain():
    input = cp_combox.get()
    if input == "1=typical angina":
        print("Typical angina")
        return 1
    elif input =="2=atypical angina":
        print("Atypical angina")
        return 2
    elif input =="3=non-anginal pain":
        print("Non-anginal pain")
        return 3
    elif input =="4=asymptomatic":
        print("Asymptomatic")
        return 4
    else:
        raise ValueError("Chest pain not selected")
    
def getResting():
    input=resting_combox.get()
    if input=="0=normal":
        return(0)
    elif input=="1=ST abnormality":
        return(1)
    elif input=="2=hypertrophy":
        return(2)

def get_St_Slope():
    input=stSlope_combox.get()
    if input=="0=upsloping":
        return(0)
    elif input=="1=flat":
        return(1)
    elif input=="2=downsloping":
        return(2)
        

def getClass():
    input=class_combox.get()
    if input=="Normal":
        return(0)
    elif input=="Heart disease":
        return(1)


#Gender
gen=IntVar(value=-1)
R1=Radiobutton(DetailsEntry,text="Male",variable=gen,value=1,command=getGender)
R2=Radiobutton(DetailsEntry,text="Female",variable=gen,value=0,command=getGender)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

#FBS
Fbs=IntVar(value=-1)
R3=Radiobutton(DetailsEntry,text="True",variable=Fbs,value=1,command=Getfbs)
R4=Radiobutton(DetailsEntry,text="False",variable=Fbs,value=0,command=Getfbs)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

#ExerciceAngina
ExAngina=IntVar(value=-1)
R5=Radiobutton(DetailsEntry,text="Yes",variable=ExAngina,value=1,command=getExAngina)
R6=Radiobutton(DetailsEntry,text="No",variable=ExAngina,value=0,command=getExAngina)
R5.place(x=387,y=10)
R6.place(x=430,y=10)


##################################ComBox##############################################

Label(DetailsEntry,text="Chest Pain:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=50)
Label(DetailsEntry,text="Resting ER:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=90)
Label(DetailsEntry,text="ST slope:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=130)
Label(DetailsEntry,text="Class:",font="arial 13",width=9,bg=frameBg,fg=framefg).place(x=10,y=170)


        

cp_combox=Combobox(DetailsEntry,values=["1=typical angina","2=atypical angina","3=non-anginal pain","4=asymptomatic"],font="arial 13",state="r",width=14)
cp_combox.place(x=105,y=50)
resting_combox=Combobox(DetailsEntry,values=["0=normal","1=ST abnormality","2=hypertrophy"],font="arial 13",state="r",width=14)
resting_combox.place(x=105,y=90)
stSlope_combox=Combobox(DetailsEntry,values=["0=upsloping","1=flat","2=downsloping"],font="arial 13",state="r",width=14)
stSlope_combox.place(x=105,y=130)
class_combox=Combobox(DetailsEntry,values=["Normal","Heart disease"],font="arial 13",state="r",width=14)
class_combox.place(x=105,y=170)


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



##################################Graph##############################################
graph_image=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\graph.png')
Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)


##################################Button##############################################
analysis_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\analyse.png')
Button(root,image=analysis_Button,bd=0,bg=background,cursor="hand1",command=Analysis).place(x=1160,y=250)

##################################InfoButton##############################################
info_Button=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\info.png')
Button(root,image=info_Button,bd=0,bg=background,cursor="hand2",command=Info).place(x=10,y=240)

##################################ReportImage##############################################

reportImage=PhotoImage(file=r'C:\Users\eyama\Documents\Python Heart Attack\Heart Attack Dataset\Images\Report.png')
reportBackground=Label(image=reportImage,bg=background)
reportBackground.place(x=1150,y=340)

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

