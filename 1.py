from tkinter import *

window=Tk()
window.geometry("700x500")


label6=Label(window,text="Rungta Canteen",font ="times 30 bold")
label6.place(x=350, y=20)

#.....Menu section

label1=Label(window,text="MENU",font= "times 28 bold ")
label1.place(x=550,y=70)

label2=Label(window,text="Poha                   rs15",font= "times 20 bold ")
label2.place(x=450,y=120)

label3=Label(window,text="Dosa                   rs30",font= "times 20 bold ")
label3.place(x=450,y=150)

label4=Label(window,text="Bread                   rs20",font= "times 20 bold ")
label4.place(x=450,y=180)

label5=Label(window,text="juice                   rs25",font= "times 20 bold ")
label5.place(x=450,y=210)

#-----billing section-----
label7=Label(window,text="Select the items", font="times 18 bold")
label7.place(x=70,y=70)

label8=Label(window,text="Poha", font="times 18 bold")
label8.place(x=20,y=120)
e1=Entry(window)
e1.place(x=20,y=150)

label9=Label(window,text="Dosa", font="times 18 bold")
label9.place(x=250,y=120)
e2=Entry(window)
e2.place(x=250,y=150)

label10=Label(window,text="Bread", font="times 18 bold")
label10.place(x=20,y=200)
e3=Entry(window)
e3.place(x=20,y=230)

label11=Label(window,text="Juice", font="times 18 bold")
label11.place(x=250,y=200)
e4=Entry(window)
e4.place(x=250,y=230)


window.mainloop()