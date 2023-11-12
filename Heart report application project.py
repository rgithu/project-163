from tkinter import *
root = Tk();
from tkinter import messagebox

root.title("Heart Diagnostic Report")
root.configure(background="#800057")
root.geometry("700x700")

#question 1

question1_radiobutton = StringVar(value = "0")
Question1 = Label(root, text = "Do you feel shortness of  breath during routine activites??", background="#800057",foreground="#ffffff")
Question1.place(relx=0.5,rely=0.1,anchor=CENTER)

question1_r1 = Radiobutton(root,text="Yes",variable=question1_radiobutton,value="Yes")
question1_r1.place(relx=0.5,rely=0.15,anchor=CENTER)

question1_r2 = Radiobutton(root,text="No",variable=question1_radiobutton,value="No")
question1_r2.place(relx=0.5,rely=0.2,anchor=CENTER)

#question 2

question2_radiobutton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have swelling in the feet/ankles/legs (shoes feel tighter) abdomen??", background="#800057",foreground="#ffffff")
Question2.place(relx=0.5,rely=0.25,anchor=CENTER)

question2_r1 = Radiobutton(root,text="Yes",variable=question2_radiobutton,value="Yes")
question2_r1.place(relx=0.5,rely=0.3,anchor=CENTER)

question2_r2 = Radiobutton(root,text="No",variable=question2_radiobutton,value="No")
question2_r2.place(relx=0.5,rely=0.35,anchor=CENTER)

#question 3

question3_radiobutton = StringVar(value = "0")
Question3 = Label(root, text = "Do you have any of these symptoms - confusion, disorientation, or loss of memory??", background="#800057",foreground="#ffffff")
Question3.place(relx=0.5,rely=0.4,anchor=CENTER)

question3_r1 = Radiobutton(root,text="Yes",variable=question3_radiobutton,value="Yes")
question3_r1.place(relx=0.5,rely=0.45,anchor=CENTER)

question3_r2 = Radiobutton(root,text="No",variable=question3_radiobutton,value="No")
question3_r2.place(relx=0.5,rely=0.5,anchor=CENTER)

#question 4

question4_radiobutton = StringVar(value = "0")
Question4 = Label(root, text = "Do you experience shortness of breath while at rest/lying down??", background="#800057",foreground="#ffffff")
Question4.place(relx=0.5,rely=0.55,anchor=CENTER)

question4_r1 = Radiobutton(root,text="Yes",variable=question4_radiobutton,value="Yes")
question4_r1.place(relx=0.5,rely=0.6,anchor=CENTER)

question4_r2 = Radiobutton(root,text="No",variable=question4_radiobutton,value="No")
question4_r2.place(relx=0.5,rely=0.65,anchor=CENTER)

#question 5

question5_radiobutton = StringVar(value = "0")
Question5 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus??", background="#800057",foreground="#ffffff")
Question5.place(relx=0.5,rely=0.7,anchor=CENTER)

question5_r1 = Radiobutton(root,text="Yes",variable=question5_radiobutton,value="Yes")
question5_r1.place(relx=0.5,rely=0.75,anchor=CENTER)

question5_r2 = Radiobutton(root,text="No",variable=question5_radiobutton,value="No")
question5_r2.place(relx=0.5,rely=0.8,anchor=CENTER)

def results() :
    score = 0
    if question1_radiobutton.get() == "Yes" :
        score =score + 10
    if question2_radiobutton.get() == "Yes" :
        score = score +10
    if question3_radiobutton.get() == "Yes" :
        score = score +10
    if question4_radiobutton.get() == "Yes" :
        score = score +10
    if question5_radiobutton.get() == "Yes" :
        score = score +10
        
    if score <= 10 :
        messagebox.showinfo("","You don't need to visit the doctor!")
    elif score >10 and score <=30 : 
        messagebox.showinfo("","You may need to visit the doctor.")
    else :
        messagebox.showinfo("","You need to visit the doctor.")

button = Button(root, text = "Find Results", command = results)
button.place(relx= 0.5,rely=0.9,anchor=CENTER)
root.mainloop();