from tkinter import *
from PIL import ImageTk
from defaultpage import *
from databasehelper import *
class AdminHomePage(DefaultPage):
    def __init__(self,root,result):
        print("admin page called")
        self.root=root
        self.details=result
        super().__init__(self.root)
        self.m = tk.Message(self.f, width=600, font="Roman 20 bold italic", text="Admin Page", bg="white",
                            relief=tk.SOLID, borderwidth=5)
        self.m.place(x=100,y=200)

        self.add_admin_details()
        self.add_buttons()
    def add_admin_details(self):
        print(self.details)
        self.profile_pic=ImageTk.PhotoImage(Image.open(self.details[4]))
        """inserts shape ,text with transparant bg"""
        self.c=Canvas(self.panel,width=100,height=180)
        """decided by image dimensuons"""
        self.canvas_pic=self.c.create_image(0,0,image=self.profile_pic,anchor=NW)
        self.m = Message(self.f, width=600, font="Roman 20 bold italic", text="Name= "+self.details[1] , bg="white",
                            relief=SOLID, borderwidth=2)
        self.m.place(x=100, y=300)


        self.m = Message(self.f, width=600, font="Roman 20 bold italic", text="Email "+self.details[3], bg="white",
                            relief=SOLID, borderwidth=2)
        self.m.place(x=100, y=400)

    def add_buttons(self):
        self.pending_bookings_button=Button(self.f,text="View Pending Bookings",width=20,height=2,bg="White",fg="black",activebackground="gray",command=self.view_pending_bookings)
        self.pending_bookings_button.place(x=450,y=400)
        self.booked_cars_button = Button(self.f, text="Booked cars", width=20, height=2, bg="White", fg="black",
                                          activebackground="gray",command=self.view_booked_cars)
        self.booked_cars_button.place(x=650, y=400)
    def add_car_frame(self):
        self.car_frame = Frame(self.f, height=500, width=1000)
        self.car_frame.place(x=500, y=1000)
        self.img_vanshi = ImageTk.PhotoImage(Image.open("vanshi.jpg"))
        self.vanshi_panel = Label(self.car_frame, image=self.img_vanshi, width=500, height=1000)
        self.vanshi_panel.pack()
        self.vanshi_panel.pack_propagate(0)
        self.car_frame.pack_propagate(0)

    def view_booked_cars(self):
        login_window = Toplevel()
        self.top_window = Frame(login_window, height=500, width=1000)
        self.top_window.pack()
        self.top_window.pack_propagate(0)
        self.img_vanshi = ImageTk.PhotoImage(Image.open("vanshi.jpg"))
        self.vanshi_panel = Label(self.top_window, image=self.img_vanshi, width=1000, height=500)
        self.vanshi_panel.pack()
        self.vanshi_panel.pack_propagate(0)
        query = "Insert into BookedCar(CustomerName) Values('%s')"
        args = (self.details[1], )
        DatabaseHelper.execute_query(query, args)
        messagebox.showinfo("Success", "Car stored in database")
        Label(self.top_window, font="Times 12", text="Customer Name").place(x=300, y=50)
        for i in range(len(result)):
            Label(self.top_window,font=self.text_font,text=result[i][1]).place(x=300,y=100)

    def view_pending_bookings(self):
        print("pending bookings called")
        self.pending_bookings_button.destroy()
        self.s=IntVar()
        self.booked_cars_button.destroy()
        login_window = Toplevel()
        self.top_window = Frame(login_window, height=500, width=1000)
        self.top_window.pack()
        self.top_window.pack_propagate(0)
        self.img_vanshi = ImageTk.PhotoImage(Image.open("vanshi.jpg"))
        self.vanshi_panel = Label(self.top_window, image=self.img_vanshi, width=1000, height=500)
        self.vanshi_panel.pack()
        self.vanshi_panel.pack_propagate(0)

        query = "Select * from world.CarOrder where IsComplete=0"
        print(query)
        result = DatabaseHelper.get_all_data(query)
        print(result)
        self.text_font = ("MS Serif", 12)
        Label(self.top_window, text="Pending Bookings", font=self.text_font).place(x=200,y=50)
        Label(self.top_window, text="CarId", font=self.text_font).place(x=400,y=50)

        Label(self.top_window, text="Customer Name", font=self.text_font).place(x=600, y=50)
        for i in range(len(result)):
            Radiobutton(self.top_window, text=result[i][0], font=self.text_font,
                        variable=self.s, value=result[i][0]).place(x=400, y=100 + 40 * i)
            Label(self.top_window, text=result[i][2], font=self.text_font).place(x=600, y=100 + 40 * i)
        self.book_b5 = Button(self.top_window, text="Execute booking", width=40, height=2, bg="Green", fg="black",
                               activebackground="white", command= self.execute)
        self.book_b5.place(x=400, y=400)

    def execute(self):
        messagebox.showinfo("Success", "Car Request approves or Booking Executed")
        query=f"UPDATE CarOrder SET IsComplete = 1 WHERE CarOrderID = {self.s.get()};"
        DatabaseHelper.execute_query(query)


