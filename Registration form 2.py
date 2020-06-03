from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="D:/Registration form with database/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #===LEFT Image===
        self.left=ImageTk.PhotoImage(file="D:/Registration form with database/social impact21.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=450,height=550)
        #===Registration Frame===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=530,y=100,width=700,height=500)
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_lname.place(x=370, y=130, width=250)
        #----------------
        contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_email.place(x=370, y=200, width=250)
        #------------------
        question = Label(frame1, text="Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmd_quest = ttk.Combobox(frame1, font=("times new roman", 15),state='readonly',justify=CENTER)
        self.cmd_quest['values']=("select","your first pet name","your birth place","your best friend name")
        self.cmd_quest.place(x=50,y=270,width=250)
        self.cmd_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_answer.place(x=370, y=270, width=250)
        #--------------------
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_password.place(x=50, y=340, width=250)

        Cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.txt_Cpassword = Entry(frame1, font=("times new roman", 15), bg="light gray")
        self.txt_Cpassword.place(x=370, y=340, width=250)
        #--------------------Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman", 12)).place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="D:/Registration form with database/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login = Button(self.root,text="Sign IN",font=("times new roman",20),bd=0, cursor="hand2").place(x=200, y=500,width=180)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_Cpassword.delete(0,END)
        self.cmd_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmd_quest.get()=="" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_Cpassword.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        elif self.txt_password.get() != self.txt_Cpassword.get():
            messagebox.showerror("Error","Password and Confirmed password should be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error","user already Exist,please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmd_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                    self.clear()

            except Exception as es:
                    messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)



root=Tk()
obj=Register(root)
root.mainloop()