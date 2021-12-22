# Displaying all records with images 
from tkinter import * 
import tkinter  as tk
from tkinter import messagebox
import mysql.connector
import os
from tkinter import ttk
import io
import tkinter  as tk 
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox as msg

root2 = Tk()
root2.title("Ecommerce Website Home Page")
root2.geometry("1360x1000")
bg = PhotoImage(file = "Login_Page_Back.gif")
label1 = Label( root2, image = bg)
label1.place(x = -2, y = 50)
ent2 = Label(root2, text = "Decor INN Shopping Store",width=68,height=2,font='Times 26 bold',bg='grey42',fg='white')
ent2.place(x = -50,y = 0)

user_detail = []

global text_field1
global text_field2
global text_field3

global text_field4
global entry_name
global entry_email
global textcomment

def register():
    root2.destroy()
    root1 = Tk()
    root1.title("Login Page")
    root1.geometry("1360x1000")
    bg = PhotoImage(file = "Login_Page_Back.gif")
    label1 = Label( root1, image = bg)
    label1.place(x = 0, y = 0)


    ent1 = Label(root1, text = "Customer_Name",bg='yellow', width=15,font='times 13 bold')
    ent1.place(x = 500,y = 60)
    ent2 = Label(root1, text = "Username",bg='yellow', width=15,font='times 13 bold')
    ent2.place(x = 500,y = 95)
    ent3 = Label(root1, text = "Customer_email",bg='yellow', width=15,font='times 13 bold')
    ent3.place(x = 500,y = 130)
    ent4 = Label(root1, text = "Password",bg='yellow', width=15,font='times 13 bold')
    ent4.place(x = 500,y = 165)
    text_field1 = Entry(root1, width = 20,bg='white',font='times 13 bold')
    text_field1.place(x = 690, y = 60)
    text_field2 = Entry(root1, width = 20,bg='white',font='times 13 bold')
    text_field2.place(x = 690, y = 95)
    text_field3 = Entry(root1, width = 20,bg='white', font='times 13 bold')
    text_field3.place(x = 690, y = 130)
    text_field4 = Entry(root1, width = 20,bg='white', font='times 13 bold')
    text_field4.place(x = 690, y = 165)

    def register1():
        mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb.cursor()
        name_cust = text_field1.get()
        id_cust  = text_field2.get()
        email_cust= text_field3.get()
        pass_cust = text_field4.get()
        # name_cust = name_cust1,
        id_cust1   = id_cust,
        # email_cust = email_cust1,
        # pass_cust  = pass_cust1,
        # result = []

        mycursor.execute("SELECT Customer_login FROM  customer")
        result = mycursor.fetchall()
        
        # var = 0
        
        for i in result:
            if i == id_cust1:
                messagebox.showinfo("Not Registered","This Username has already been Registered")
                return
                
        dat1 = "INSERT INTO customer (Customer_Name,Customer_login,Customer_email,password) VALUES (%s,%s,%s,%s)"
        dat2 = (name_cust,id_cust, email_cust, pass_cust)
        mycursor.execute(dat1, dat2)
        mydb.commit()
        messagebox.showinfo("Registered","Successfully Registered")


    Button(root1, text= "Register",bg='yellow',fg='black',font='times 12 bold', command=register1).place(x = 800, y = 200)  
    root1.mainloop() 



def login():
    root2.destroy()
    root1 = Tk()
    root1.title("Login Page")
    root1.geometry("1360x1000")
    bg = PhotoImage(file = "Login_Back.gif")
    label1 = Label( root1, image = bg)
    label1.place(x = 0, y = 0)


    ent2 = Label(root1, text = "Username",bg='yellow', width=10,font='times 13 bold')
    ent2.place(x = 500,y = 100)

    ent4 = Label(root1, text = "Password",bg='yellow', width=10,font='times 13 bold')
    ent4.place(x = 500,y = 150)
    # e4 = Entry(my_w,width=30)

    text_field2 = Entry(root1, width = 20,bg='white',font= 'times 13 bold bold')
    text_field2.place(x = 630, y = 100)

    text_field4 = Entry(root1, width = 20,bg='white',font= 'times 13 bold bold')
    text_field4.place(x = 630, y = 150)

    def login1():
    
        mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb.cursor()
        user_name = text_field2.get()
        user_pass = text_field4.get()
        name_value= user_name,
        pas_value = user_pass,
        global user_detail
        
        mycursor.execute("SELECT Customer_login FROM customer")
        name_result = mycursor.fetchall()
        varnam = 0
        signal = 0


        
        for i in name_result:
            if i == name_value:
                user_detail = [user_name]

                # user_detail.append()
                varnam = 1
                break
        if user_name == 'admin':
            varnam = 0
            signal = 1
            
            
        mycursor.execute("SELECT password from customer")
        pass_result = mycursor.fetchall()
        varpas = 0
        signal1 = 0
        for i in pass_result:
            if i == pas_value:
                varpas = 1
                break
        if user_pass == 'admin':
            varpas = 0
            signal1 = 1
        

        if varnam == 1 and varpas == 1:
            root1.destroy()
            thenStart()
            return

        if signal == 1 and signal1 == 1:
            root1.destroy()
            adminpanel()
            return

        else:
            messagebox.showinfo("Failed", "Invalid username or password")
    Button(root1, text= "Login",bg='yellow',fg='black',font='times 12 bold' ,command=login1).place(x = 670, y = 190) 
    root1.mainloop() 





Button(root2, text= "Sign Up",width=10,bg='grey42',fg='white',font='Times 12 bold', command=register).place(x = 950, y = 45)    
Button(root2, text= "Sign In",width=10,bg='grey42',fg='white',font='Times 12 bold', command=login).place(x = 1070, y = 45) 




grocery_list = []
electronics_list = []
sports_list = []
furniture_list = []
appliance_list = []
global entry_name
global entry_email
global textcomment

mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
mycursor = mydb.cursor()


def thenStart():
    root=Tk()
    root.title("Display Products")
    root.geometry("1360x1000")
    Heading=LabelFrame(root,bd=2,relief="groove",bg="light yellow")
    Heading.place(x=0,y=0,width=1380,height=55)
    image_logo=ImageTk.PhotoImage(Image.open("Logo.png"))
    label_logo=Label(Heading,image=image_logo)
    label_logo.grid(row=0,column=0)

    name=Label(Heading,text="DECOR INN",font="arial 20 bold italic",bg="light pink",fg="blue").grid(row=0,column=1)
    tagline=Label(Heading,text="Shopping made easier!",font="magneto 16 italic",fg="gold",bg="green").grid(row=0,column=2,padx=280)
    Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="dark blue")
    Products_frame.place(x=310,y=60,width=1040,height=620)
    label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
    Button_frame=LabelFrame(root,bd=2,relief="groove")
    Button_frame.place(x=2,y=60,width=300,height=380)

    def feedback():
        
        root = Tk()
        root.title("Feedback")
        frame_header = ttk.Frame(root)
        frame_header.pack()
        # logo = PhotoImage(file='logo.gif').subsample(2, 2)
        # logolabel = ttk.Label(frame_header, text='logo', image=logo)
        # logolabel.grid(row=0, column=0, rowspan=2)
        headerlabel = ttk.Label(frame_header, text='CUSTOMER FEEDBACK', foreground='orange',
                                font=('Arial', 24))
        headerlabel.grid(row=0, column=1)
        messagelabel = ttk.Label(frame_header,
                                text='PLEASE TELL US WHAT YOU THINK',
                                foreground='purple', font=('Arial', 10))
        messagelabel.grid(row=1, column=1)

        frame_content = ttk.Frame(root)
        frame_content.pack()

        myvar = StringVar()
        var = StringVar()
        # cmnt= StringVar()
        namelabel = ttk.Label(frame_content, text='Name')
        namelabel.grid(row=0, column=0, padx=5, sticky='sw')
        entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14))
        entry_name.grid(row=1, column=0)

        emaillabel = ttk.Label(frame_content, text='Email')
        emaillabel.grid(row=0, column=1, sticky='sw')
        entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14))
        entry_email.grid(row=1, column=1)

        commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
        commentlabel.grid(row=2, column=0, sticky='sw')
        textcomment = Text(frame_content, width=55, height=10)
        textcomment.grid(row=3, column=0, columnspan=2)


        textcomment.config(wrap ='word')
        # def clear():
        #     textcomment.delete(1.0,'end')
        def clear():
            global entry_name
            global entry_email
            global textcomment
            messagebox.showinfo(title='clear', message='Do you want to clear?')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)


        def submit():

            dat1 = entry_name.get()
            dat2 = entry_email.get()
            dat3 = textcomment.get(1.0, END)
            data = (dat1,dat2,dat3)
            mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO  feedback(customer_name,email,comments) \
                            VALUES (%s,%s,%s)",data)
            mydb.commit()
            messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            textcomment.delete(1.0, END)
            root.destroy()


        submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=4, column=0, sticky='e')
        clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=4, column=1, sticky='w')

        root.mainloop()





    def HideAllFrames():
        for widget in Products_frame.winfo_children():
            widget.destroy()
# Grocery_Label=Label(second_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)
# database connection 






    def ElectronicsCall():
        
        HideAllFrames()
        # Create main frame
        main_frame = Frame(Products_frame)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')

        
        # Electronics_Label=Label(second_frame,text="Electronics",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0)
        mycursor.execute("SELECT * FROM product where category_id = 2")
        my_row = mycursor.fetchall()
        
        mycursor.execute('SELECT product_name from product where category_id = 2')
        item_list = mycursor.fetchall()
        mycursor.execute('SELECT price from product where category_id = 2')
        price_list = mycursor.fetchall()
        mycursor.execute('SELECT product_id from product where category_id = 2')
        id_list = mycursor.fetchall()
        def AddG1():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[0])
                electronics_list.append(price_list[0])
                electronics_list.append(item_list[0])

                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is not added to the cart.")
        def AddG2():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[1])
                electronics_list.append(price_list[1])
                electronics_list.append(item_list[1])
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is not added to the cart.")
        def AddG3():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[2])
                electronics_list.append(price_list[2])
                electronics_list.append(item_list[2])
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is not added to the cart.")
        def AddG4():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[3])
                electronics_list.append(price_list[3])
                electronics_list.append(item_list[3])
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is not added to the cart.")
        def AddG5():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[4])
                electronics_list.append(price_list[4])
                electronics_list.append(item_list[4])

                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is not added to the cart.")
        def AddG6():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[5])
                electronics_list.append(price_list[5])
                electronics_list.append(item_list[5])
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is not added to the cart.")
        def AddG7():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[6])
                electronics_list.append(price_list[6])
                electronics_list.append(item_list[6])

                messagebox.showinfo("Product Status","("+str(item_list[6])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[6])+") is not added to the cart.")
        def AddG8():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[7])
                electronics_list.append(price_list[7])
                electronics_list.append(item_list[7])
                messagebox.showinfo("Product Status"," ("+str(item_list[7])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[7])+") is not added to the cart.")
        def AddG9():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[8])
                electronics_list.append(price_list[8])
                electronics_list.append(item_list[8])

                messagebox.showinfo("Product Status"," ("+str(item_list[8])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[8])+") is not added to the cart.")
        def AddG10():
            global electronics_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                electronics_list.append(id_list[9])
                electronics_list.append(price_list[9])
                electronics_list.append(item_list[9])

                messagebox.showinfo("Product Status","("+str(item_list[9])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[9])+") is not added to the cart.")


        i=1 # data starts from row 1 
        j=1
        images = [] # to manage garbage collection. 
        count = 1
        for student in my_row: 
            stream = io.BytesIO(student[3])
            img=Image.open(stream)
            img = ImageTk.PhotoImage(img) 
            if count == 1:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1)
            elif count == 2:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2)
            elif count == 3:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3)
            elif count == 4:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4)
            elif count == 5:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5)
            elif count == 6:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6)
            elif count == 7:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7)
            elif count == 8:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8)
            elif count == 9:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9)
            elif count == 10:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10)


            e1 = Label(second_frame, image=img) 
            e1.grid(row=j, column=i,ipadx=20) 

            e2 = Label(second_frame, text=student[2]) 
            e2.grid(row=j+1,column=i,ipadx=10) 

            e3 = Label(second_frame,text='RS:',font="times 9 bold")
            e3.grid(row=j+2,column=i,ipadx=15) 

            e4 = Label(second_frame, text=student[4],font="times 9 bold") 
            e4.grid(row=j+3,column=i,ipadx=20)        

            add_grocery.grid(row=j+4,column=i,ipady=3,ipadx=20)
    
            images.append(img) # garbage collection 
            i=i+1    
            if i == 6:
                j= j+5
                i = 1
            count = count + 1
        
        root.mainloop()

    def GroceryCall():

        HideAllFrames()
            # Create main frame
        main_frame = Frame(Products_frame)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')
        # Grocery_Label=Label(second_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)   

        mycursor.execute("SELECT * FROM product WHERE category_id = 1")
        my_row = mycursor.fetchall()
        mycursor.execute('SELECT product_name from product where category_id = 1')
        item_list = mycursor.fetchall()
        mycursor.execute('SELECT price from product where category_id = 1')
        price_list = mycursor.fetchall()
        mycursor.execute('SELECT product_id from product where category_id = 1')
        id_list = mycursor.fetchall()



    
        def AddG1():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[0])
                grocery_list.append(price_list[0])
                grocery_list.append(item_list[0])

                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is not added to the cart.")
        def AddG2():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[1])
                grocery_list.append(price_list[1])
                grocery_list.append(item_list[1])
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is not added to the cart.")
        def AddG3():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[2])
                grocery_list.append(price_list[2])
                grocery_list.append(item_list[2])
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is not added to the cart.")
        def AddG4():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[3])
                grocery_list.append(price_list[3])
                grocery_list.append(item_list[3])
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is not added to the cart.")
        def AddG5():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[4])
                grocery_list.append(price_list[4])
                grocery_list.append(item_list[4])
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is not added to the cart.")
        def AddG6():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[5])
                grocery_list.append(price_list[5])
                grocery_list.append(item_list[5])
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is not added to the cart.")
        def AddG7():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[6])
                grocery_list.append(price_list[6])
                grocery_list.append(item_list[6])
                messagebox.showinfo("Product Status","("+str(item_list[6])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[6])+") is not added to the cart.")
        def AddG8():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[7])
                grocery_list.append(price_list[7])
                grocery_list.append(item_list[7])
                messagebox.showinfo("Product Status"," ("+str(item_list[7])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[7])+") is not added to the cart.")
        def AddG9():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[8])
                grocery_list.append(price_list[8])
                grocery_list.append(item_list[8])
                messagebox.showinfo("Product Status"," ("+str(item_list[8])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[8])+") is not added to the cart.")
        def AddG10():
            global grocery_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                grocery_list.append(id_list[9])
                grocery_list.append(price_list[9])
                grocery_list.append(item_list[9])
                messagebox.showinfo("Product Status","("+str(item_list[9])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[9])+") is not added to the cart.")

        i=1 # data starts from row 1 
        j=1
        images = [] # to manage garbage collection. 
        count = 1
        for student in my_row: 
            stream = io.BytesIO(student[3])
            img=Image.open(stream)
            img = ImageTk.PhotoImage(img)  
            if count == 1:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1)
            elif count == 2:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2)
            elif count == 3:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3)
            elif count == 4:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4)
            elif count == 5:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5)
            elif count == 6:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6)
            elif count == 7:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7)
            elif count == 8:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8)
            elif count == 9:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9)
            elif count == 10:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10)


            e1 = Label(second_frame, image=img) 
            e1.grid(row=j, column=i) 

            e2 = Label(second_frame, text=student[2]) 
            e2.grid(row=j+1,column=i,ipadx=10) 

            e3 = Label(second_frame,text='RS:',font="times 9 bold")
            e3.grid(row=j+2,column=i,ipadx=15) 

            e4 = Label(second_frame, text=student[4],font="times 9 bold") 
            e4.grid(row=j+3,column=i,ipadx=20)        

            add_grocery.grid(row=j+4,column=i,ipady=3,ipadx=20)
    
            images.append(img) # garbage collection 
            i= i + 1    
            if i == 7:
                j= j + 5
                i = 1
            count = count + 1
        root.mainloop()

    def SportsGymCall():

        HideAllFrames()
            # Create main frame
        main_frame = Frame(Products_frame)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')
        # Grocery_Label=Label(second_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)   

        mycursor.execute("SELECT * FROM product WHERE category_id = 3")
        my_row = mycursor.fetchall()
        mycursor.execute('SELECT product_name from product where category_id = 3')
        item_list = mycursor.fetchall()
        mycursor.execute('SELECT price from product where category_id = 3')
        price_list = mycursor.fetchall()
        mycursor.execute('SELECT product_id from product where category_id = 3')
        id_list = mycursor.fetchall()



    
        def AddG1():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[0])
                sports_list.append(price_list[0])
                sports_list.append(item_list[0])

                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is not added to the cart.")
        def AddG2():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[1])
                sports_list.append(price_list[1])
                sports_list.append(item_list[1])
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is not added to the cart.")
        def AddG3():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[2])
                sports_list.append(price_list[2])
                sports_list.append(item_list[2])

                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is not added to the cart.")
        def AddG4():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[3])
                sports_list.append(price_list[3])
                sports_list.append(item_list[3])
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is not added to the cart.")
        def AddG5():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[4])
                sports_list.append(price_list[4])
                sports_list.append(item_list[4])
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is not added to the cart.")
        def AddG6():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[5])
                sports_list.append(price_list[5])
                sports_list.append(item_list[5])

                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is not added to the cart.")
        def AddG7():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[6])
                sports_list.append(price_list[6])
                sports_list.append(item_list[6])

                messagebox.showinfo("Product Status","("+str(item_list[6])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[6])+") is not added to the cart.")
        def AddG8():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[7])
                sports_list.append(price_list[7])
                sports_list.append(item_list[7])

                messagebox.showinfo("Product Status"," ("+str(item_list[7])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[7])+") is not added to the cart.")
        def AddG9():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[8])
                sports_list.append(price_list[8])
                sports_list.append(item_list[8])
                messagebox.showinfo("Product Status"," ("+str(item_list[8])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[8])+") is not added to the cart.")
        def AddG10():
            global sports_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                sports_list.append(id_list[9])
                sports_list.append(price_list[9])
                sports_list.append(item_list[9])
                messagebox.showinfo("Product Status","("+str(item_list[9])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[9])+") is not added to the cart.")

        i=1 # data starts from row 1 
        j=1
        images = [] # to manage garbage collection. 
        count = 1
        for student in my_row: 
            stream = io.BytesIO(student[3])
            img=Image.open(stream)
            img = ImageTk.PhotoImage(img)  
            if count == 1:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1)
            elif count == 2:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2)
            elif count == 3:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3)
            elif count == 4:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4)
            elif count == 5:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5)
            elif count == 6:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6)
            elif count == 7:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7)
            elif count == 8:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8)
            elif count == 9:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9)
            elif count == 10:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10)


            e1 = Label(second_frame, image=img) 
            e1.grid(row=j, column=i,ipadx=20) 

            e2 = Label(second_frame, text=student[2]) 
            e2.grid(row=j+1,column=i,ipadx=10) 

            e3 = Label(second_frame,text='RS:',font="times 9 bold")
            e3.grid(row=j+2,column=i,ipadx=15) 

            e4 = Label(second_frame, text=student[4],font="times 9 bold") 
            e4.grid(row=j+3,column=i,ipadx=20)        

            add_grocery.grid(row=j+4,column=i,ipady=3,ipadx=20)
    
            images.append(img) # garbage collection 
            i = i + 1    
            if i == 7:
                j= j + 5
                i = 1
            count = count + 1
        root.mainloop()


    def FurnitureCall():

        HideAllFrames()
            # Create main frame
        main_frame = Frame(Products_frame)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')
        # Grocery_Label=Label(second_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)   

        mycursor.execute("SELECT * FROM product WHERE category_id = 4")
        my_row = mycursor.fetchall()
        mycursor.execute('SELECT product_name from product where category_id = 4')
        item_list = mycursor.fetchall()
        mycursor.execute('SELECT price from product where category_id = 4')
        price_list = mycursor.fetchall()
        mycursor.execute('SELECT product_id from product where category_id = 4')
        id_list = mycursor.fetchall()



    
        def AddG1():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[0])
                furniture_list.append(price_list[0])
                furniture_list.append(item_list[0])


                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is not added to the cart.")
        def AddG2():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[1])
                furniture_list.append(price_list[1])
                furniture_list.append(item_list[1])
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is not added to the cart.")
        def AddG3():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[2])
                furniture_list.append(price_list[2])
                furniture_list.append(item_list[2])

                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is not added to the cart.")
        def AddG4():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[3])
                furniture_list.append(price_list[3])
                furniture_list.append(item_list[3])

                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is not added to the cart.")
        def AddG5():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[4])
                furniture_list.append(price_list[4])
                furniture_list.append(item_list[4])
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is not added to the cart.")
        def AddG6():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[5])
                furniture_list.append(price_list[5])
                furniture_list.append(item_list[5])
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is not added to the cart.")
        def AddG7():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[6])
                furniture_list.append(price_list[6])
                furniture_list.append(item_list[6])
                messagebox.showinfo("Product Status","("+str(item_list[6])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[6])+") is not added to the cart.")
        def AddG8():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[7])
                furniture_list.append(price_list[7])
                furniture_list.append(item_list[7])
                messagebox.showinfo("Product Status"," ("+str(item_list[7])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[7])+") is not added to the cart.")
        def AddG9():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[8])
                furniture_list.append(price_list[8])
                furniture_list.append(item_list[8])

            
                messagebox.showinfo("Product Status"," ("+str(item_list[8])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[8])+") is not added to the cart.")
        def AddG10():
            global furniture_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                furniture_list.append(id_list[9])
                furniture_list.append(price_list[9])
                furniture_list.append(item_list[9])

                messagebox.showinfo("Product Status","("+str(item_list[9])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[9])+") is not added to the cart.")

        i=1 # data starts from row 1 
        j=1
        images = [] # to manage garbage collection. 
        count = 1
        for student in my_row: 
            stream = io.BytesIO(student[3])
            img=Image.open(stream)
            img = ImageTk.PhotoImage(img)  
            if count == 1:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1)
            elif count == 2:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2)
            elif count == 3:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3)
            elif count == 4:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4)
            elif count == 5:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5)
            elif count == 6:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6)
            elif count == 7:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7)
            elif count == 8:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8)
            elif count == 9:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9)
            elif count == 10:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10)


            e1 = Label(second_frame, image=img) 
            e1.grid(row=j, column=i,ipadx=20) 

            e2 = Label(second_frame, text=student[2]) 
            e2.grid(row=j+1,column=i,ipadx=10) 

            e3 = Label(second_frame,text='RS:',font="times 9 bold")
            e3.grid(row=j+2,column=i,ipadx=15) 

            e4 = Label(second_frame, text=student[4],font="times 9 bold") 
            e4.grid(row=j+3,column=i,ipadx=20)        

            add_grocery.grid(row=j+4,column=i,ipady=3,ipadx=20)
    
            images.append(img) # garbage collection 
            i=i+1    
            if i == 4:
                j= j+5
                i = 1
            count = count + 1
        root.mainloop()

    def AppliancesCall():

        HideAllFrames()
            # Create main frame
        main_frame = Frame(Products_frame)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')
        # Grocery_Label=Label(second_frame,text="Grocery",font="times 15 bold",fg="gold",bg="black").grid(row=0,column=0,padx=20)   

        mycursor.execute("SELECT * FROM product WHERE category_id = 5")
        my_row = mycursor.fetchall()
        mycursor.execute('SELECT product_name from product where category_id = 5')
        item_list = mycursor.fetchall()
        mycursor.execute('SELECT price from product where category_id = 5')
        price_list = mycursor.fetchall()
        mycursor.execute('SELECT product_id from product where category_id = 5')
        id_list = mycursor.fetchall()



    
        def AddG1():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[0])
                appliance_list.append(price_list[0])
                appliance_list.append(item_list[0])

                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[0])+" is not added to the cart.")
        def AddG2():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[1])
                appliance_list.append(price_list[1])
                appliance_list.append(item_list[1])
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[1])+" is not added to the cart.")
        def AddG3():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[2])
                appliance_list.append(price_list[2])
                appliance_list.append(item_list[2])
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[2])+" is not added to the cart.")
        def AddG4():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[3])
                appliance_list.append(price_list[3])
                appliance_list.append(item_list[3])
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[3])+" is not added to the cart.")
        def AddG5():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[4])
                appliance_list.append(price_list[4])
                appliance_list.append(item_list[4])
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," "+str(item_list[4])+" is not added to the cart.")
        def AddG6():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[5])
                appliance_list.append(price_list[5])
                appliance_list.append(item_list[5])
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[5])+") is not added to the cart.")
        def AddG7():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[6])
                appliance_list.append(price_list[6])
                appliance_list.append(item_list[6])
                messagebox.showinfo("Product Status","("+str(item_list[6])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[6])+") is not added to the cart.")
        def AddG8():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[7])
                appliance_list.append(price_list[7])
                appliance_list.append(item_list[7])
                messagebox.showinfo("Product Status"," ("+str(item_list[7])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[7])+") is not added to the cart.")
        def AddG9():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[8])
                appliance_list.append(price_list[8])
                appliance_list.append(item_list[8])
                messagebox.showinfo("Product Status"," ("+str(item_list[8])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status","("+str(item_list[8])+") is not added to the cart.")
        def AddG10():
            global appliance_list
            op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
            if op:
                appliance_list.append(id_list[9])
                appliance_list.append(price_list[9])
                appliance_list.append(item_list[9])
                messagebox.showinfo("Product Status","("+str(item_list[9])+") is successfully added to the cart.")
            else:
                messagebox.showinfo("Product Status"," ("+str(item_list[9])+") is not added to the cart.")

        i=1 # data starts from row 1 
        j=1
        images = [] # to manage garbage collection. 
        count = 1
        for student in my_row: 
            stream = io.BytesIO(student[3])
            img=Image.open(stream)
            img = ImageTk.PhotoImage(img)  
            if count == 1:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG1)
            elif count == 2:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG2)
            elif count == 3:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG3)
            elif count == 4:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG4)
            elif count == 5:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG5)
            elif count == 6:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG6)
            elif count == 7:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG7)
            elif count == 8:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG8)
            elif count == 9:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG9)
            elif count == 10:
                add_grocery=Button(second_frame,text="Add Item",bg="green",fg="white",font="times 9 bold",command=AddG10)


            e1 = Label(second_frame, image=img) 
            e1.grid(row=j, column=i,ipadx=20) 

            e2 = Label(second_frame, text=student[2]) 
            e2.grid(row=j+1,column=i,ipadx=10) 

            e3 = Label(second_frame,text='RS:',font="times 9 bold")
            e3.grid(row=j+2,column=i,ipadx=15) 

            e4 = Label(second_frame, text=student[4],font="times 9 bold") 
            e4.grid(row=j+3,column=i,ipadx=20)        

            add_grocery.grid(row=j+4,column=i,ipady=3,ipadx=20)
    
            images.append(img) # garbage collection 
            i=i+1    
            if i == 5:
                j= j+5
                i = 1
            count = count + 1
        root.mainloop()

    def Bill():
        global grocery_list
        global electronics_list
        global sports_list
        global furniture_list
        global appliance_list
        global user_detail
 
        mydb1 = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb1.cursor()

        # mycursor.execute("Truncate order1")
        # mydb1.commit()
        signal = 0
        if len(grocery_list) > 0:
            count = 0
            for i in range(len(grocery_list)//3):
                
                data = (str(grocery_list[count]),str(grocery_list[count+1]),user_detail[0],str(grocery_list[count+2]))
                mycursor.execute("INSERT INTO  order1 (product_id,amount,customer_id,product_name) \
                                    VALUES (%s,%s,%s,%s)",data)
                mydb1.commit()
                count = count + 3
            signal = 1
        if len(electronics_list) > 0:
            count = 0
            for i in range(len(electronics_list)//3):
                
                data = (str(electronics_list[count]),str(electronics_list[count+1]),user_detail[0],str(electronics_list[count+2]))
                mycursor.execute("INSERT INTO  order1 (product_id,amount,customer_id,product_name) \
                                    VALUES (%s,%s,%s,%s)",data)
                mydb1.commit()
                count = count + 3
            signal = 1

        if len(sports_list) > 0:
            count = 0
            for i in range(len(sports_list)//3):
                
                data = (str(sports_list[count]),str(sports_list[count+1]),user_detail[0],str(sports_list[count+2]))
                mycursor.execute("INSERT INTO  order1 (product_id,amount,customer_id,product_name) \
                                    VALUES (%s,%s,%s,%s)",data)
                mydb1.commit()
                count = count + 3
            signal = 1

        if len(furniture_list) > 0:
            count = 0
            for i in range(len(furniture_list)//3):
                
                data = (str(furniture_list[count]),str(furniture_list[count+1]),user_detail[0],str(furniture_list[count+2]))
                mycursor.execute("INSERT INTO  order1 (product_id,amount,customer_id,product_name) \
                                    VALUES (%s,%s,%s,%s)",data)
                mydb1.commit()
                count = count + 3
            signal = 1

        if len(appliance_list) > 0:
            count = 0
            for i in range(len(appliance_list)//3):
                
                data = (str(appliance_list[count]),str(appliance_list[count+1]),user_detail[0],str(appliance_list[count+2]))
                mycursor.execute("INSERT INTO  order1 (product_id,amount,customer_id,product_name) \
                                    VALUES (%s,%s,%s,%s)",data)
                mydb1.commit()
                count = count + 3
            signal = 1
        if signal == 1:
            op=messagebox.showinfo("Confirmation","Your Order has been placed successfully.")
        
        else:
            op=messagebox.showinfo("Order Info","Please select items before placing the Order.")

      


# Buttons of Category

    Grocery_button=Button(Button_frame,text="Grocery",font="times 20 bold",width=17,bd=6,bg="grey",fg="white",activebackground="light blue",command = GroceryCall)
    Grocery_button.grid(row=0,column=0,padx=5,pady=5)
    Electronics_button=Button(Button_frame,text="Electronics",font="times 20 bold",width=17,bd=6,bg="grey",fg="white",activebackground="light blue",command=ElectronicsCall)
    Electronics_button.grid(row=1,column=0,padx=5,pady=5)
    Sports_Gym_button=Button(Button_frame,text="Sports and Gym",font="times 20 bold",width=17,bd=6,bg="grey",fg="white",activebackground="light blue",command=SportsGymCall)
    Sports_Gym_button.grid(row=2,column=0,padx=5,pady=5)
    Furniture_button=Button(Button_frame,text="Furniture",font="times 20 bold",width=17,bd=6,bg="grey",fg="white",activebackground="light blue",command=FurnitureCall)
    Furniture_button.grid(row=3,column=0,padx=5,pady=5)
    Appliances_button=Button(Button_frame,text="Appliances",font="times 20 bold",width=17,bd=6,bg="grey",fg="white",activebackground="light blue",command=AppliancesCall)
    Appliances_button.grid(row=4,column=0,padx=5,pady=5)
    bill_gen_button=Button(Heading,bd=4,text="Place Order",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=Bill)
    bill_gen_button.grid(row=0,column=3)
    feedback_button=Button(Heading,bd=4,text="Review Us",font="times 17 bold",bg="skyblue",fg="white",activebackground="purple",command=feedback)
    feedback_button.place(x=900,y=2)
    root.mainloop()

def adminpanel():
    root2 = Tk()
    root2.title("Admin Panel")
    root2.geometry("400x500")
    bg = PhotoImage(file = "admin_panel_back.gif")
    label1 = Label( root2, image = bg)
    label1.place(x = -1, y = 0)



    def add_product():
        root2.destroy()
        my_w = Tk()
        my_w.geometry("700x500")  # Size of the window 
        my_w.title('Admin Panel @ Add_Product')
        my_font1=('times', 18, 'bold')
        bg = PhotoImage(file = "Add_Product_Back.gif")
        label1 = Label( my_w, image = bg)
        label1.place(x = 0, y = 0)

        l1 = Label(my_w,text='Add Product detail',font=my_font1).place(x=240,y = 10)

        l3 = Label(my_w,  text='Category ID :', width=10,bg= 'yellow' ).place(x=15,y= 70)
        e3 = Entry(my_w,width=30,bg='white',font= 'times 13 bold bold')
        e3.place(x=100,y= 70)

        l4 = Label(my_w,  text='Product Name', width=10,bg= 'yellow' ).place(x=15,y= 105)
        e4 = Entry(my_w,width=30,bg='white',font= 'times 13 bold bold')
        e4.place(x=100,y= 105)

        l5 = Label(my_w,  text='Price :', width=10 ,bg= 'yellow').place(x=15,y= 140)
        e5 = Entry(my_w,width=30,bg='white',font= 'times 13 bold bold')
        e5.place(x=100,y= 140)

        l6 = Label(my_w,  text='Quantity :', width=10,bg= 'yellow' ).place(x=15,y= 175)
        e6 = Entry(my_w,width=30,bg='white',font= 'times 13 bold bold')
        e6.place(x=100,y= 175)


        def upload_file(): # Image upload and display
            global filename,img
            f_types =[('Gif files','*.gif'),('Png files','*.png'),('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            b2 =Button(my_w,image=img) # using Button 
            b2.place(x=300,y=120)#display uploaded photo

        def add_data():   # Add data to MySQL table
        
            global img , filename 
    
            data2 = e3.get()
            data3 = e4.get()
            data4 = e5.get() 
            data5 = e6.get()

            fob=open(filename,'rb') # filename from upload_file()
            fob=fob.read()
            data=(data2,data3,fob,data4,data5) # tuple with data 

            mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO  product(Category_ID,Product_Name,Image,Price,Quantity) \
                            VALUES (%s,%s,%s,%s,%s)",data)
            mydb.commit()

            my_w.destroy() # close window after adding data


        my_font=('times', 12, 'bold')
        b2 = Button(my_w, text='Upload File', font=my_font,bg='yellow', command =upload_file)
        b2.place(x=105,y=210)
        # b2.grid(row=2,column=4) 

        
        b3 = Button(my_w, text='Submit Product Detail', font=my_font,bg='Green',fg='white',command =add_data)
        b3.place(x=100,y=250)

        my_w.mainloop()  # Keep the window open


    def delete_product():
        root2.destroy()
        my_w = tk.Tk() # parent window 
        my_w.geometry("1360x1000") # size as width height
        my_w.title("Product Record Deletion")  # Adding a title


        # database connection 


        main_frame = Frame(my_w)
        main_frame.pack(fill=BOTH, expand=1)


        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas

        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')




        mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb.cursor()
        global img,images
        images=[] # garbage collection 
        def display(): # show all records 

            mycursor.execute("SELECT * FROM product")
            my_row=mycursor.fetchall()

            i=1 # data starts from row 1 
            j = 1
            global  images
            for student in my_row: 
                stream = io.BytesIO(student[3])
                img=Image.open(stream)
                img = ImageTk.PhotoImage(img)    

                e = Label(second_frame, text=student[2],font='times 9 bold') 
                e.grid(row=j+1,column=i,ipadx=10) 
                e = Label(second_frame, image=img) 
                e.grid(row=j, column=i,ipady=1,ipadx=30) 
                e = Button(second_frame,bg='Red',
                    text='X',command=lambda k=student[2]:del_data(k)) 
                e.grid(row=j+3, column=i,ipady=7,ipadx=30) 
                images.append(img) # garbage collection 
                i=i+1 
                if i == 6:
                    j= j+4
                    i = 1
                
        display()  # call to display all records 
        def del_data(s_id):

            # try:
            my_var=msg.askyesnocancel("Delete Record",
                "Are you sure ? ",icon='warning')
            if my_var:
                query="DELETE FROM  product WHERE product_name=%s"
                my_data=[s_id]
                mycursor.execute(query,my_data)
                mydb.commit()
                display() # refresh the list
                return 

        my_w.mainloop()

    def view_orders():
        root2.destroy()
        my_w = tk.Tk() # parent window 
        my_w.geometry("650x400") # size as width height
        my_w.title("Admin Panel @ Customers Orders")  # Adding a title

        main_frame = Frame(my_w)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')

        l5 = Label(second_frame,text='Orders Received from Customers',font='times 18 bold')
        l5.grid(row=0,column=2)

        # Create Database Connection
        mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT order_id,product_name,amount,customer_id FROM order1")
        my_row=mycursor.fetchall()


        # Column headers  row 0
        l1=Label(second_frame, text='Order_ID',font= "times 9 bold",bg="grey") 
        l1.grid(row=1,column=1) 
        l2=Label(second_frame, text='Product_Name',font= "times 9 bold",bg="grey") 
        l2.grid(row=1,column=2) 
        l3=Label(second_frame, text='Price',font= "times 9 bold",bg="grey") 
        l3.grid(row=1,column=3)
        l4=Label(second_frame, text='Customer_ID',font= "times 9 bold",bg="grey") 
        l4.grid(row=1,column=4)


        i = 2 # data starts from row 1 
        j = 1
        for student in my_row: 
            e = Label(second_frame, text=student[0]) 
            e.grid(row=i,column=j,ipadx=10) 
            e = Label(second_frame, text=student[1]) 
            e.grid(row=i, column=j+1,ipady=1,ipadx=30) 
            e = Label(second_frame,text=student[2]) 
            e.grid(row=i, column=j+2,ipady=7,ipadx=30)
            e = Label(second_frame,text=student[3]) 
            e.grid(row=i, column=j+3,ipady=7,ipadx=30)     
            i = i + 1 
            j = 1

        my_w.mainloop()

    def customer_review ():
        root2.destroy()
        my_w = tk.Tk() # parent window 
        my_w.geometry("650x400") # size as width height
        my_w.title("Admin Panel @ Customers Reviews")  # Adding a title

        main_frame = Frame(my_w)
        main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Create Scroll bar
        my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

        # Create another frame inside the Canvas
        second_frame = Frame(my_canvas)

        # Add that new frame to a window in canvas
        my_canvas.create_window((0,0), window = second_frame, anchor= 'nw')

        l5 = Label(second_frame,text='Feedback from Customers',font='times 18 bold')
        l5.grid(row=0,column=2)

        # Create Database Connection
        mydb = mysql.connector.connect(host="localhost", user="root", password="mian.4.5.6", database = "ecomerce")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT customer_name,email,comments FROM feedback")
        my_row=mycursor.fetchall()




        # Column headers  row 0
        l1=Label(second_frame, text='Customer Name',font= "times 9 bold",bg="grey") 
        l1.grid(row=1,column=1) 
        l2=Label(second_frame, text='Customer Email',font= "times 9 bold",bg="grey") 
        l2.grid(row=1,column=2) 
        l3=Label(second_frame, text='Comments',font= "times 9 bold",bg="grey") 
        l3.grid(row=1,column=3)



        i = 2 # data starts from row 1 
        j = 1
        for student in my_row: 
            e = Label(second_frame, text=student[0]) 
            e.grid(row=i,column=j,ipadx=10) 
            e = Label(second_frame, text=student[1]) 
            e.grid(row=i, column=j+1,ipady=1,ipadx=30) 
            e = Label(second_frame,text=student[2]) 
            e.grid(row=i, column=j+2,ipady=7,ipadx=30)    
            i = i + 1 
            j = 1

        my_w.mainloop()


    Button(root2, text="Add Product",height = 3,width = 15,bg="green",fg="white",font="times 12 bold ",command = add_product).place(x = 120, y = 70)    
    Button(root2, text="Delete Product",height = 3,width = 15,bg="green",fg="white",font="times 12 bold ",command = delete_product).place(x = 120, y = 160) 
    Button(root2, text="View Orders",height = 3,width = 15,bg="green",fg="white",font="times 12 bold ",command = view_orders).place(x = 120, y = 250)  
    Button(root2, text="Customer Feedback",height = 3,width = 15,bg="green",fg="white",font="times 12 bold ",command = customer_review).place(x = 120, y = 340)  
  
    root2.mainloop()


root2.mainloop()