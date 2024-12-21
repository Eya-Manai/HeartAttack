from tkinter import *
icon_Window=Tk()
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