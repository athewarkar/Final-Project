# Final-Project
#WaterifyApp.py

from tkinter import *
class MyWindow:
    def __init__(self, win):
        #Labels
        self.lbl0 = Label(win, text='Waterify', font=("Times New Roman",25), relief=SOLID, bd=4, borderwidth=2)
        self.lbl1=Label(win, text='Name: ',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        self.lbl2=Label(win, text='Weight(lbs): ',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        self.lbl3=Label(win, text='Height(Inches): ',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        self.lbl4=Label(win, text='Age: ',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        self.lbl5=Label(win, text='Exercise Mins: ',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        self.lbl6=Label(win, text='Result:',font=("Times New Roman",17), relief=SOLID, bd=4, borderwidth=2)
        
        #input
        self.t1=Entry(bd=3, relief=SOLID)
        self.t2=Entry(bd=3, relief=SOLID)
        self.t3=Entry(bd=3, relief=SOLID)
        self.t4=Entry(bd=3, relief=SOLID)
        self.t5=Entry(bd=3, relief=SOLID)
        
        
        #button
        self.btn1 = Button(win, text='Calculate')

        #Header
        self.lbl0.place(x=400, y=10)
        #row1
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=300, y=50)
        #row2
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=300, y=100)
        #row3
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=300, y=150)
        #row4
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=300, y=200)

        #row5
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=300, y=250)
        
        #button1
        self.b1=Button(win, text='Calculate',font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=self.calculate)
        self.b1.place(x=100, y=350)
        #button2
        self.b1=Button(win, text='Clear',font=("Times New Roman",14), width=20, relief=SOLID, borderwidth=4, command=self.Clear)
        self.b1.place(x=100, y=400)

        #result
        self.lbl6.place(x=100, y=300)
        self.listboxDes = Listbox(font=("Times New Roman",14), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=2)
        self.listboxDes.place(x=300, y=300)

        
    def calculate(self):
        self.listboxDes.delete(0, 'end')
        name = self.t1.get()
        weight=float(self.t2.get())
        height=float(self.t3.get())
        exerciseMin = float(self.t5.get())
        bmi = (weight*703.0)/(height**2.0)
        bmi_Status=""
        formatted_bmi = "{:.2f}".format(bmi)
        if(bmi<18.5):
            bmi_Status = "Underweight"
        elif(bmi>=18.5 and bmi<=24.9):
             bmi_Status = "Normal Weight"          
        elif(bmi>=25 and bmi<=29.9):
           bmi_Status = "Over Weight"
        else:
            bmi_Status = "Obese"
        self.listboxDes.insert(END,"BMI: " + formatted_bmi )
        self.listboxDes.insert(END,"BMI Status: "  + bmi_Status )
        if(exerciseMin > 0):
            waterOunces = exerciseMin * 0.4
        formatted_Ounces = "{:.2f}".format(waterOunces)
        result= str(formatted_Ounces)
        self.listboxDes.insert(END, "Daily Water Ounces: " + str(result))
        
    def Clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        self.listboxDes.delete(0, 'end')

window=Tk()
window.title("Waterify")
window.geometry("855x600")
window.resizable(False, False)
mywin=MyWindow(window)
window.mainloop()
