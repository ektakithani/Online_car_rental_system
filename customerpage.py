from tkinter import *
from PIL import ImageTk
from cars.defaultpage import *
from cars.databasehelper import *
from tkinter import messagebox
class CustomerHomePage(DefaultPage):
    def __init__(self,root,result):
        self.details=result
        print("customer page called")
        self.root=root
        self.text_font = ("Comic sans ms", 20)
        super().__init__(self.root)
        self.b = Message(self.f, width=600, font="Roman 20 bold italic", text="customer Page", bg="white",
                         relief=tk.SOLID, borderwidth=5)
        self.b.place(x=100, y=200)
        self.add_customer_details()
        self.add_buttons()



    def add_customer_details(self):
        print(self.details)
        print("My Profile")
        self.n = Message(self.f, width=600, font="Roman 20 bold italic", text="UserName= " + self.details[1], bg="white",
                         relief=SOLID, borderwidth=2)
        self.n.place(x=100, y=300)

    def add_buttons(self):
        self.mybookings_button = Button(self.f, text="My Bookings", width=20, height=2, bg="White", fg="black",activebackground="gray",command=lambda: self.mybookings(self.details[0],self.details[1]))
        self.mybookings_button.place(x=450, y=400)
        self.bookmycar_button = Button(self.f, text="Book my car", width=20, height=2, bg="White", fg="black",activebackground="gray", command=self.add_cars)
        self.bookmycar_button.place(x=650, y=400)


    def mybookings(self,id,name):
        self.mybookings_button.destroy()
        self.bookmycar_button.destroy()
        self.b.destroy()
        self.n.destroy()
        Label(self.f, text="Cars ID", font=self.text_font).place(x=200, y=200)
        Label(self.f, text="Car's Name", font=self.text_font).place(x=400, y=200)
        query1 = "Select CarId from CarOrder where CustomerName='%s'"
        args1 = (name)
        result1 = DatabaseHelper.get_all_data(query1, args1)
        query2 = "Select CarName,CarId from Cars where CarId='%d'"
        args2=list()
        for i in result1:
            args2.append(i[0])
        args2=tuple(args2)
        print(args2)
        # args2 = (result1[0][0])
        result2 = DatabaseHelper.get_all_data(query2, args2)
        print(result1)
        print(result2)

        for i in range(len(result2)):
            Label(self.f, text=result2[i][0], font=('roman', 15)).place(x=200, y=250 + 50 * i)
            Label(self.f, text=result2[i][1], font=('roman', 15)).place(x=400, y=250 + 50 * i)

    def add_cars(self):
        self.mybookings_button.destroy()
        self.bookmycar_button.destroy()
        self.n.destroy()
        self.b.destroy()
        self.m.destroy()
        self.car_b1 = Button(self.f, text="Mini Cars", width=10, height=2, bg="ivory2", fg="black",
                             activebackground="white", command=lambda: self.add_car_items("Mini"))
        self.car_b1.place(x=100, y=200)
        self.car_b2 = Button(self.f, text="Micro Cars", width=10, height=2, bg="ivory2", fg="black",
                             activebackground="white", command=lambda: self.add_car_items("Micro"))
        self.car_b2.place(x=300, y=200)

    def add_car_items(self, car_type):
        result = self.get_cars(car_type)
        selected_option = IntVar()
        print(selected_option)
        self.lst_images = []
        for i in range(len(result)):
            self.lst_images.append((ImageTk.PhotoImage(Image.open(result[i][4]))))
        for i in range(len(result)):
            Radiobutton(self.f, text=result[i][0], font=self.text_font,
                        variable=selected_option, value=result[i][0]).place(x=50, y=100 + 100 * i)
            Label(self.f, text=result[i][1], font=self.text_font).place(x=100, y=100 + 100 * i)
            Label(self.f, text=result[i][2], font=self.text_font).place(x=200, y=100 + 100 * i)
            Label(self.f, text=result[i][3], font=self.text_font).place(x=400, y=100 + 100 * i)

            Label(self.f, image=self.lst_images[i]).place(x=600, y=100 + 100 * i)
        print(selected_option.get())
        self.book_b5 = Button(self.f, text="Book car", width=40, height=2, bg="Green", fg="black",
                              activebackground="white", command=lambda: self.book_car(selected_option.get()))
        self.book_b5.place(x=700, y=500)

    def get_cars(self, car_type):
        query = "Select CarId,CarName,CarCompany,CarPricePerDay,CarImage from Cars where CarType='%s'"
        args = (car_type,)
        result = DatabaseHelper.get_all_data(query, args)
        return result

    def book_car(self, selected):
        print(selected)
        if (selected == 0):
            messagebox.showwarning("No car booked", "Please select atleast one car")
        else:
            messagebox.showinfo("Success ", "Car Booked Successfully")
            self.send_bookedcars_to_admin(selected)

    def send_bookedcars_to_admin(self,selected):

        query = "Insert into CarOrder(CustomerName,CarId) Values('%s',%d)"
        print(selected)
        args = (self.details[1],selected)
        DatabaseHelper.execute_query(query, args)
        messagebox.showinfo("Success", "Car stored in database")














