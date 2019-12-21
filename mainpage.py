from tkinter import *
from defaultpage import *
from databasehelper import *
from tkinter import messagebox
from adminpage import *
from customerpage import *
import time
class MainPage(DefaultPage):
    def __init__(self,root):
        super().__init__(root)
        self.add_widgets()

    def add_widgets(self):
        self.admin_button = Button(self.panel, text="Admin Login", width=20, height=2, activebackground="gray",
                                   activeforeground="blue", command=lambda: self.get_login_screen("Admin"))
        self.admin_button.place(x=400, y=200)
        self.user_button = Button(self.panel, text="User Login", width=20, height=2, activebackground="gray",
                                  activeforeground="blue", command=lambda: self.get_login_screen("User"))
        self.user_button.place(x=600, y=200)
        self.new_user_button = Button(self.panel, text="New User? Sign up Here", width=20, height=2,
                                      activebackground="gray", activeforeground="blue", relief=RIDGE,
                                      command=lambda: self.sign_up("User"))
        self.new_user_button.place(x=500, y=300)

    def reset(self):
        self.e1.delete(0,END)
        self.e2.delete(0, END)
        """END is constant given by python tkinter,like relief,etc caps"""

    def validate(self,login_window,login_type):
        username=self.e1.get()
        pwd = self.e2.get()
        if(login_type=="Admin"):
            query="select * from Admin where AdminName='%s' and AdminPassword='%s'"
            """jaise hi %s aaega wo param k pass jayega"""
        else:
            query="select * from Customer where CustomerUser='%s' and CustomerPassword='%s'"

        params=(username,pwd)
        result = DatabaseHelper.get_data(query,params)

        if (result is None or len(result)==0):
            messagebox.showerror("Login Failed","Incorrect Credentials")
        else:
            messagebox.showinfo('Login Success ',"Login Successfully Completed")
            login_window.destroy()
            """small window destroyed"""
            self.f.destroy()
            self.panel.destroy()
            """can or cannot write"""

            if (login_type=="Admin"):
                self.redirect = AdminHomePage(self.root,result)
                """root p apne stickers add karega,result tuple """
            else:
                #self.redirect = CustomerHomePage(self.root,result)
                self.redirect = CustomerHomePage(self.root,result)

    def get_login_screen(self,login_type):
        login_window=Toplevel()
        f=Frame(login_window,height=200,width=700)
        l1=Label(f,width=20,text="Username")
        self.e1=Entry(f,width=30,fg="black",bg="white")
        l2=Label(f,width=20,text="Password")
        self.e2=Entry(f,width=30,fg="black",bg="white",show="*")
        l1.grid(row=1,column=1,padx=10,pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        self.e1.focus_set()
        self.e1.grid(row=1, column=4, padx=10, pady=10)
        self.e2.grid(row=2, column=4, padx=10, pady=10)
        self.b1 = Button(f, text="Login", width=20, height=2, activebackground="gray",command=lambda:self.validate(login_window,login_type))
        self.b1.grid(row=3, column=1,sticky="e",padx=10)
        self.b2 = Button(f, text="Reset", width=20, height=2, activebackground="gray",command=lambda:self.reset())
        self.b2.grid(row=3, column=2,sticky="w",padx=10)


        f.pack()
        f.grid_propagate(0)

    def sign_up(self,registration_type):
        registration_window=Toplevel()
        f=Frame(registration_window,height=500,width=600)
        l1=Label(f,width=20,text="Username")
        self.e1 = Entry(f, width=30, fg="black", bg="white")
        l2 = Label(f, width=20, text="Firstname")
        self.e2 = Entry(f, width=30, fg="black", bg="white")
        l3 = Label(f, width=20, text="Lastname")
        self.e3 = Entry(f, width=30, fg="black", bg="white")
        l4 = Label(f, width=20, text="Address")
        self.e4 = Entry(f, width=30, fg="black", bg="white")
        l5 = Label(f, width=20, text="City")
        self.e5 = Entry(f, width=30, fg="black", bg="white")
        l6 = Label(f, width=20, text="Country")
        self.e6 = Entry(f, width=30, fg="black", bg="white")
        l8 = Label(f, width=20, text="Contact No")
        self.e8 = Entry(f, width=30, fg="black", bg="white")
        l9 = Label(f, width=20, text="Password")
        self.e9 = Entry(f, width=30, fg="black", bg="white")
        l10 = Label(f, width=20, text="Confirm Password")
        self.e10 = Entry(f, width=30, fg="black", bg="white")

        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        l3.grid(row=3, column=1, padx=10, pady=10)
        l4.grid(row=4, column=1, padx=10, pady=10)
        l5.grid(row=5, column=1, padx=10, pady=10)
        l6.grid(row=6, column=1, padx=10, pady=10)
        l8.grid(row=8, column=1, padx=10, pady=10)
        l9.grid(row=9, column=1, padx=10, pady=10)
        l10.grid(row=10, column=1, padx=10, pady=10)

        self.e1.grid(row=1, column=4, padx=10, pady=10)
        self.e2.grid(row=2, column=4, padx=10, pady=10)
        self.e3.grid(row=3, column=4, padx=10, pady=10)
        self.e4.grid(row=4, column=4, padx=10, pady=10)
        self.e5.grid(row=5, column=4, padx=10, pady=10)
        self.e6.grid(row=6, column=4, padx=10, pady=10)
        self.e8.grid(row=8, column=4, padx=10, pady=10)
        self.e9.grid(row=9, column=4, padx=10, pady=10)

        self.e10.grid(row=10, column=4, padx=10, pady=10)

        self.submit_button = Button(f, text="Submit", width=20, height=2,activebackground="Green", activeforeground="blue", relief=RIDGE,command=lambda:self.register_user(registration_window))
        self.submit_button.place(x=300, y=400)
        f.pack()
        f.grid_propagate(0)
    def register_user(self,registration_type):
        username = self.e1.get()
        firstname = self.e2.get()
        lastname = self.e3.get()
        address = self.e4.get()
        city = self.e5.get()
        country = self.e6.get()
        contact = self.e8.get()
        pwd = self.e9.get()
        pwd2 = self.e10.get()
        print(type(contact))
        if (username == "" or contact == "" or firstname == "" or address=="" or city=="" or country==""or  pwd == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
        elif (pwd != pwd2):
            messagebox.showerror("Password Error", "Passwords don't match.Please re-enter")
        else:
            query = "Insert into Customer(CustomerUser,CustomerFirstName,CustomerLastName, CustomerAddress,CustomerCity,CustomerCountry,CustomerContact,CustomerPassword) Values ('%s','%s','%s','%s','%s','%s','%s','%s')"
            args = (username,firstname,lastname,address,city,country,contact,pwd)
            DatabaseHelper.execute_query(query % args)
            messagebox.showinfo("Success", "User registered successfully. Please login")

        #what color after active


root=tk.Tk()
m=MainPage(root)
root.mainloop()
