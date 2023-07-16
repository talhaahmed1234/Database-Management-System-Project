from datetime import datetime
from datetime import date, timedelta
from tkinter import Tk, W, E, filedialog, ttk
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image as pilImage, ImageTk
from tkinter import * 
from tkinter import messagebox
import random
from abc import ABC, abstractmethod
import glob
import sqlite3
import matplotlib.pyplot as plt
from io import BytesIO
import io
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#making a database connection
conn = sqlite3.connect("e commerce.db")
c = conn.cursor()

#to pre-fill entry bosex
class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label="Type here", **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)
#starting page 
class introductory_page:
    def __init__(self,root):
        self.root=root
        logo = tk.PhotoImage(file="splogor.png")
        root.iconphoto(True, logo)
        self.root.title("Ample Access")
        self.root.geometry("1000x600")
        self.image2 = PhotoImage(file = "BGGG.png")
        self.intro = Frame(self.root,width=950,height=609,bg= "light green")
        self.contacts = Frame(self.root,width=1099,height = 20, bg = "grey")
        self.root.resizable(False,False)
        self.label3 = Label(self.intro,text=" "*20)
        self.label3.config(image = self.image2 ,width = 1300, height = 750)
        self.label3.pack()
        self.label1=Label(self.intro,text="                  "+"                CONTACT US                               "+"                    ",bg = "#363636", fg = "#C71585" ,font = "consolas 17 bold")
        self.label1.place(x=0,y=0)
        self.label2=Label(self.intro,text="☎:+923122211828     "+"                 ✉:Ample Access.com           "+"       📌:Karachi        ",bg = "#363636", fg = "#C71585" ,font = ("consolas",  15))
        self.label2.place(x=0,y=28)
        self.image1 = PhotoImage(file = "LOGO.png")
        self.cont = Label(self.intro,image = self.image1)
        self.cont.place(x=20,y=70)
        self.label=Label(self.intro,text= "➡Welcome!! This site really helps you in shopping with ease and reasonable prices.",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
        self.label.place(x=20,y=310)
        self.label=Label(self.intro,text= "➡You acknowledge and recognize that we are a private commercial enterprise and reserve the right to conduct business \n  to achieve our objectives in a manner we deem fit.",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
        self.label.place(x=20,y=345)
        self.label=Label(self.intro,text= "➡The entire contents of the Site also are protected by copyright as a collective work under Pakistani copyright laws and \n international conventions. All rights are reserved..",bg='#ff9342',fg = "#fff5db",font="lato 13 bold")
        self.label.place(x=20,y=400)
        self.label4=Label(self.intro,text= "➡We shall neither be liable or responsible for any actions or inactions of any other service provider as listed on our Site"+"\n"+ "which includes but is not limited to payment providers, instalment offerings, warranty services amongst others.",bg='#ff9342',fg = "#fff5db",font=("lato", 13, "bold"))
        self.label4.place(x=20,y=460)
        self.agreement=Label(self.intro,text="➡BY PROCEDING TO NEXT PAGE ,YOU ARE ACCEPTING TO OUR ALL TERMS AND CONDITIONS.",fg="black",bg="#ff9342",font="lato 13 bold")
        self.agreement.place(x=20,y=515)

#user features 
class user_account:
    def __init__(self,obj1):
        self.root = obj.root
        self.obj1=obj1

        self.image2 = PhotoImage(file = "BGGG.png")
        self.f1_introductory = tk.Frame(self.root)

        self.label3 = Label(self.f1_introductory,text=" "*20)
        self.label3.config(image = self.image2 ,width = 1300, height = 750)
        self.label3.pack()
        
        self.LOGINLABEL=Label(self.f1_introductory,text="LOGIN/SIGNUP",fg="black",bg="#b5928e",font="consolas 20 bold").place(x=405,y=40)

        self.username = tk.Label(self.f1_introductory, text="USERNAME:", font="Consolas 15 bold",bg = "grey").place(x=450,y=110)

        self.username_entry = LabeledEntry(self.f1_introductory, label="Type username", font="Times 15", fg="grey")
        self.username_entry.place(x=400,y=150)

        self.password = tk.Label(self.f1_introductory, text="PASSWORD:", font="Consolas 15 bold",bg = "grey").place(x=450,y=190)

        self.pass_entry = LabeledEntry(self.f1_introductory, label="Type Password",show="*", font="Times 15", fg="grey")
        self.pass_entry.place(x=400,y=230)

        self.loginbutton = tk.Button(self.f1_introductory, text="Login", font="Consolas 15 bold", bg="blue", fg="yellow",command=self.login).place(x=470,y=280)

        signupbutton=tk.Button(self.f1_introductory, text="Don't have an account(Sign Up)",font="Consolas 15 bold",bg="blue" ,fg="yellow",command=self.login_signup).place(x=330,y=330)
        
        self.f2_Signup = tk.Frame(self.root)

        self.label4 = Label(self.f2_Signup,text=" "*20)
        self.label4.config(image = self.image2 ,width = 1300, height = 750)
        self.label4.pack()

        self.image3 = PhotoImage(file = "SAKO.png")
        
        #marketing poster
        self.sale = Label(self.f2_Signup,image = self.image3)
        self.sale.place(x=20,y=120)

        Label(self.f2_Signup, text="SIGNUP", font="Consolas 20 bold",bg="#b5928e",fg = "black").place(x=440,y=25)

        Newuser = tk.Label(self.f2_Signup, text="First name:", font="Consolas 15 bold",bg="grey",fg="black").place(x=430,y=70)
        self.Newuserfname = LabeledEntry(self.f2_Signup, label="Type Firstname", font="Times 15", fg="grey")
        self.Newuserfname.place(x=400,y=105)

        Newuserlname = tk.Label(self.f2_Signup, text="Last Name:", font="Consolas 15 bold",bg="grey",fg="black").place(x=433,y=140)
        self.Newuserlnameentry = LabeledEntry(self.f2_Signup, label="Type Last name", font="Times 15", fg="grey")
        self.Newuserlnameentry.place(x=400,y=175)

        Newuseradress = tk.Label(self.f2_Signup, text="Address:", font="Consolas 15 bold",bg="grey",fg="black").place(x=445,y=210)
        self.Newuseraddressentry = LabeledEntry(self.f2_Signup, label="Type Address", font="Times 15", fg="grey")
        self.Newuseraddressentry.place(x=400,y=245)

        self.back = tk.Button(self.f2_Signup, text="BACK", font="Consolas 15 bold", bg="blue", fg="yellow",command=self.f2tof1).place(x=10,y=10)

        self.Newuseremail = tk.Label(self.f2_Signup, text="Email adress:", font="Consolas 15 bold",bg="grey",fg="black").place(x=420,y=280)
        self.Newuseremailentry = LabeledEntry(self.f2_Signup, label="Type Your e-mail", font="Times 15", fg="grey")
        self.Newuseremailentry.place(x=400,y=315)

        Newuserph = tk.Label(self.f2_Signup, text="Phone number:", font="Consolas 15 bold",bg="grey",fg="black").place(x=415,y=350)
        self.Newuserphentry = LabeledEntry(self.f2_Signup, label="eg:03*********", font="Times 15", fg="grey")
        self.Newuserphentry.place(x=400,y=385)

        Newuseruname = tk.Label(self.f2_Signup, text="Username:", font="Consolas 15 bold",bg="grey",fg="black").place(x=443,y=420)
        self.usernameentry = LabeledEntry(self.f2_Signup, label="Type username", font="Times 15", fg="grey")
        self.usernameentry.place(x=400,y=455)

        Newuserpass = tk.Label(self.f2_Signup, text="Password:", font="Consolas 15 bold",bg="grey",fg="black").place(x=443,y=490)
        self.Newuserpassentry = LabeledEntry(self.f2_Signup, label="Type Password", show="*",font="Times 15", fg="grey")
        self.Newuserpassentry.place(x=400,y=525)

        signupbutton2 = tk.Button(self.f2_Signup, text="Sign Up", font="Consolas 15 bold", bg="blue", fg="yellow",
                                  command=self.saveinfo).place(x=448,y=555)

        self.label=Label(self.f2_Signup,text= '''"NOTE:ALL THE FOLLOWING INFORMATION \n IS MANDATORY FOR SIGNUP"''',bg="#b50000",fg = "white",font="lato 13 bold")
        self.label.place(x=600,y=45)

        C1 = Checkbutton(self.f2_Signup, text = "Keep notify me for upcoming discounts", font = "lato 12",
                 onvalue = "yes", offvalue = "no").place(x=38,y=80)

        self.font = ("Consolas", 14, "bold")

        self.image1 = PhotoImage(file = "proced.png")
        self.btn2=Button(self.obj1.intro,image = self.image1,command=self.turn_to_product).place(x=400,y=555)
        self.usernameofperson=""
        
        #shoppping interface 
        self.intro_user = Frame(self.root, width = 1000, height = 100, bg = "black")

        #name
        self.label3 = Label(self.intro_user, text="\tAMPLE ACCESS", font = ('Algerian 40 bold'), bg = "black", fg = "white")
        self.label3.place(x=10,y=0)
        #tagline
        self.label4 = Label(self.intro_user, text = "Here Is The One Stop Solution To All Your Needs.", font = ('Algerian 12 bold'), bg = "black", fg = "gray")
        self.label4.place(x=250,y=55)

        #Logo
        img = tk.PhotoImage(file = "splogor.png")
        self.label4 = tk.Label(self.intro_user,image = img)
        self.label4.image = img
        self.label4.place(x=10,y=10)

        #cart icon
        img = tk.PhotoImage(file = "cart.png")
        self.label5 = tk.Button(self.intro_user,image = img,bg = "black",command = self.added_to_cart)
        self.label5.image = img
        self.label5.place(x=880,y=6)

        #logout button
        self.logout = tk.Button(self.intro_user, text = "LOGOUT", bg = "white", fg = "black", font = ("Comic Sans MS", 12, "bold"), command = self.logout)
        self.logout.place(x = 760, y = 8)

        
        self.view_products_f = Frame(self.root, width = 1000, height = 500, bg = "#504a4c")
        
        self.cart_frame = Frame(self.root, width = 1000, height = 500, bg = "blue")
        #cart background
        img = tk.PhotoImage(file = "cartbg.png")
        self.label6 = tk.Label(self.cart_frame,image = img)
        self.label6.image = img
        self.label6.pack()

        self.back = tk.Button(self.cart_frame, text = "Back" , font = ("Comic Sans MS",12, "bold"), bg = "white", fg = "black", command = self.back_1)
        self.back.place(x = 20, y = 12)

        self.bill_Label = tk.Label(self.cart_frame, text = "Total Bill:" , font = ("Comic Sans MS",14, "bold"), bg = "black", fg = "white")
        self.bill_Label.place(x = 120, y = 12)
        
        self.bill = []
        self.bill_Amount = tk.Label(self.cart_frame, text = f"{self.bill}" , font = ("Comic Sans MS",14, "bold"), bg = "black", fg = "white")
        self.bill_Amount.place(x = 220, y = 12)

        self.checkout = tk.Button(self.cart_frame, text = "CHECKOUT", font = ("Comic Sans MS", 12, "bold"),
                                  bg = "#07b5ac",fg = "yellow", command = self.checkout)
        self.checkout.place(x = 440, y = 8)

        #checkout background GUI
        self.image = PhotoImage(file = "checkout.png")
        self.checkout_frame = tk.Frame(self.root, width = 1000, height = 500)

        self.label3 = Label(self.checkout_frame,text=" "*20)
        self.label3.config(image = self.image ,width = 1300, height = 750)
        self.label3.pack()

        self.label_thanks = tk.Label(self.checkout_frame, text = f"Thank You For Choosing AMPLE ACCESS , {self.username}!",
                              font = ("Comic Sans MS", 20, 'bold'))
        self.label_thanks.place(x = 20, y = 10)

        self.label_deliver = tk.Label(self.checkout_frame,text = "Your Order Will Be Delivered To You In Two Working Days !",
                               font = ("Comic Sans MS", 15, 'bold'))
        self.label_deliver.place(x = 20,y = 120)

        self.label3 = tk.Label(self.checkout_frame, text = "", font = ("Comic Sans MS", 15, 'bold'))
        self.label3.place(x = 20, y = 200)

        self.label4 = tk.Label(self.checkout_frame,text = "",font = ("Comic Sans MS", 15, 'bold'))
        self.label4.place(x = 20, y = 280)

        self.label5 = tk.Label(self.checkout_frame,text = "", font = ("Algerian", 25, 'bold'))
        self.label5.place(x =300, y = 350)

    #user products viewing
    class UserProductApp:
        def __init__(self, master):
            master.pack()
            self.master = master

            self.product_list = []
            self.cart = []

            #the four categories
            appliance = tk.Button(self.master,command=lambda: self.show_products("APPLIANCES"))#,command=self.switch_to_garments)
            image = ImageTk.PhotoImage(file="APPLIANCES.jpg")
            appliance.config(image=image, width=198, height=100, bg="grey")
            appliance.image = image
            appliance.place(x=30,y=25)
            appliancelabel=Button(self.master,text="      APPLIANCES      ",fg ="black",bg = "white" ,command=lambda: self.show_products("APPLIANCES"),font = ("Comic Sans MS", 12, "bold"))
            appliancelabel.place(x=30,y=10)

            electronic = tk.Button(self.master,command=lambda: self.show_products("ELECTRONICS"))#,command=self.switch_to_garments)
            image = ImageTk.PhotoImage(file="ELECROLOGO.png")
            electronic.config(image=image, width=202, height=100, bg="grey")
            electronic.image = image
            electronic.place(x=30+250,y=25)
            electroniclabel=Button(self.master,text="     ELECTRONICS      ",fg ="black",bg = "white" ,command=lambda: self.show_products("ELECTRONICS"),font = ("Comic Sans MS", 12, "bold"))
            electroniclabel.place(x=30+250,y=10)

            sports = tk.Button(self.master,command=lambda: self.show_products("SPORTS"))#,command=self.switch_to_garments)
            image = ImageTk.PhotoImage(file="download.jpg")
            sports.config(image=image, width=200, height=100, bg="grey")
            sports.image = image
            sports.place(x=30+500,y=25)
            sportslabel=Button(self.master,text="          SPORTS        ",fg ="black",bg = "white" ,font = ("Comic Sans MS", 12, "bold"),command=lambda: self.show_products("SPORTS"))
            sportslabel.place(x=30+500,y=10)

            garments = tk.Button(self.master,command=lambda: self.show_products("GARMENTS"))#,command=self.switch_to_garments)
            image = ImageTk.PhotoImage(file="garment.jpg")
            garments.config(image=image, width=202, height=100, bg="grey")
            garments.image = image
            garments.place(x=30+750,y=25)
            garmentslabel=Button(self.master,text="       CLOTHING        ",fg ="black",bg = "white" ,command=lambda: self.show_products("GARMENTS"),font = ("Comic Sans MS", 12, "bold"))
            garmentslabel.place(x=30+750,y=10)

            # Create product display area
            self.product_frame = tk.Frame(self.master, width=1000, height=350, bd=3, relief="groove")
            self.product_frame.place(x=0, y=150)
            
            # Create scrollbar for product display area
            self.scrollbar = ttk.Scrollbar(self.product_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

            # Create canvas for product display area
            self.canvas = tk.Canvas(self.product_frame, width=1000, height=350, yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar.config(command=self.canvas.yview)

            # Create frame for product items
            self.product_items_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.product_items_frame, anchor=tk.NW)

            self.show_products("SPORTS")
        def fetch_products(self, category):
            # Fetch products from database for specific category
            conn = sqlite3.connect("C:\DISK D\FE SPRING\OOP\e commerce.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE category=?", (category,))
            rows = cursor.fetchall()
            conn.close()

            # Convert fetched rows to Product objects
            products = []
            for row in rows:
                product = Admin_account.Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                products.append(product)

            return products
        def show_products(self, category):
            #display products
            # Clear previous product items
            for widget in self.product_items_frame.winfo_children():
                widget.destroy()

            # Fetch products for selected category
            self.product_list = self.fetch_products(category)

            # Create product items
            if self.product_list == []:
                empty_label = tk.Label(self.product_items_frame, text = "NO PRODUCTS TO SHOW... ", font = ("Arial",12,"bold"))
                empty_label.place(x = 10, y =10)
                return
                
            for i, product in enumerate(self.product_list):
                # Create frame for each product item
                item_frame = tk.Frame(self.product_items_frame, width=310, height=300, bd=4, relief="solid")
                item_frame.grid(row=i//3, column=i%3, padx=5, pady=5)
                
                # Display product name
                name_label = tk.Label(item_frame, text="Name: "+product.name, font=("Arial", 12, "bold"),wraplength=120)
                name_label.place(x=10, y=10)
                
                #add to cart button
                add_cart_i = Button(item_frame, text = "Add To Cart", font= ("Comic sans MS",12,"bold"), command = lambda id = product.product_id: self.add_to_cart(id), bg = "grey", fg = "white")
                add_cart_i.place(x = 10, y= 140) 

                # Display product image
                img = pilImage.open(io.BytesIO(product.image))
                img = img.resize((130, 180), pilImage.Resampling.LANCZOS)
                img = ImageTk.PhotoImage(img)
                img_label = tk.Label(item_frame, image=img)
                img_label.image = img
                img_label.place(x=150, y=10)

                # Display product description
                desc_h = tk.Label(item_frame, text = "Description: ",font = ("arial", 12, "bold")).place(x = 10,y = 195)
                desc_label = tk.Label(item_frame, text=product.description+".", font=("Arial", 12), wraplength=185)
                desc_label.place(x=115, y=195)

                # Display product price
                price_label = tk.Label(item_frame, text=f"Price: Rs{product.price}/= ", font=("Arial", 12, "bold"))
                price_label.place(x=10, y=70)

                # Display product stock
                stock_label = tk.Label(item_frame, text=f"Stock: {product.stock}", font=("Arial", 10, "bold"))
                stock_label.place(x=10, y=90)

                # Display product brand
                brand_label = tk.Label(item_frame, text=f"Brand: {product.brand}", font=("Arial", 10))
                brand_label.place(x=10, y=110)

            # Update the canvas scroll region to fit all product items
            self.product_items_frame.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
            
        def add_to_cart(self,product_id):
            product_id = product_id
            query = "SELECT user_id FROM User_credentials WHERE username = ?"
            c.execute(query, (loginpage.username,))
            result = c.fetchone()
            user_id = result[0]
            self.user_id = user_id

            # Check if the product is already in the cart for the user
            query = "SELECT * FROM cart WHERE user_id = ? AND product_id = ?"
            c.execute(query, (user_id, product_id))
            existing_item = c.fetchone()

            if existing_item:
                # If the product is already in the cart, update the quantity
                quantity = existing_item[2] + 1  # Increase the quantity by 1
                update_query = "UPDATE cart SET quantity = ? WHERE user_id = ? AND product_id = ?"
                c.execute(update_query, (quantity, user_id, product_id))
            else:
                # If the product is not in the cart, insert a new entry
                insert_query = "INSERT INTO cart (user_id, product_id, quantity) VALUES (?, ?, 1)"
                c.execute(insert_query, (user_id, product_id))

            # Commit the changes to the database
            conn.commit()

    #User application more features
    class User_app:
        def __init__(self, master):
            master.pack(side="bottom", fill="both", expand=True)
            self.master = master
            
            self.users_frame = tk.Frame(self.master, width=760, height=450, bd=2, relief="groove")
            self.users_frame.place(x=0, y=40)

            self.scrollbar = ttk.Scrollbar(self.users_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.canvas = tk.Canvas(self.users_frame, width=760, height=450, yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar.config(command=self.canvas.yview)

            self.master = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.master, anchor=tk.NW)

            self.show_user(self.master)
    #cart app for cart GUI and features
    class Cart_app:
        def __init__(self, master):
            master.pack()
            self.master = master
            
            self.products_frame = tk.Frame(self.master, width=633, height=430, bd=2, relief="groove")
            self.products_frame.place(x=0, y=55)

            self.scrollbar = ttk.Scrollbar(self.products_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

            self.canvas = tk.Canvas(self.products_frame, width=633 , height=430, yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar.config(command=self.canvas.yview)

            self.products_items_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.products_items_frame, anchor=tk.NW)

            self.show_cart()
            
        def show_cart(self):
            #show products in user's cart
            query = "SELECT SUM(CAST(REPLACE(p.price, ',', '') AS DECIMAL(10,2)) * c.quantity) AS total_bill FROM cart c JOIN products p ON c.product_id = p.product_id WHERE c.user_id = ?;"
            c.execute(query, (loginpage.user_id,))
            result = c.fetchone()
            
            if result[0] is not None:
                total_bill = result[0]
                loginpage.bill = [total_bill]
                
            conn = sqlite3.connect("e commerce.db")
            cursor = conn.cursor()
            #fetching the cart of user
            cursor.execute("SELECT * FROM cart where user_id = ?", (loginpage.user_id,))
            use = cursor.fetchall()
            # Convert fetched rows to Product objects
            products =[]
            for row in use:
                cursor.execute("select * from products where product_id  = ?", (row[1],))
                prod = cursor.fetchall()
                prod = prod[0]
                product = Admin_account.Product(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5], prod[6],prod[7])
                x = [product,row[2]]
                products.append(x)
            #to clear the display
            for widget in self.products_items_frame.winfo_children():
                widget.destroy()
            if products == []:
                loginpage.bill_Amount['text'] = '0'
                empty_label = tk.Label(self.products_items_frame, text = "YOUR CART IS EMPTY... ", font = ("Arial",15,"bold"),fg = 'red')
                empty_label.pack()
                return
            else:
                loginpage.bill_Amount['text'] = sum(loginpage.bill)
            for i, product in enumerate(products):
                # Create frame for each product item
                item_frame= tk.Frame(self.products_items_frame, width=310, height=300, bd=4, relief="solid")
                item_frame.grid(row=i//2, column=i%2, padx=5, pady=5)

                # Display product name
                name_label = tk.Label(item_frame, text="Name: "+product[0].name, font=("Arial", 12, "bold"),wraplength=120)
                name_label.place(x=10, y=10)

                # Display product image
                img = pilImage.open(io.BytesIO(product[0].image))
                img = img.resize((130, 180), pilImage.Resampling.LANCZOS)
                img = ImageTk.PhotoImage(img)
                img_label = tk.Label(item_frame, image=img)
                img_label.image = img
                img_label.place(x=150, y=10)

                # Display product description
                desc_h = tk.Label(item_frame, text = "Description: ",font = ("arial", 12, "bold")).place(x = 10,y = 195)
                desc_label = tk.Label(item_frame, text=product[0].description+".", font=("Arial", 12), wraplength=185)
                desc_label.place(x=115, y=195)

                # Display product price
                price_label = tk.Label(item_frame, text=f"Price: Rs{product[0].price}/= ", font=("Arial", 11, "bold"))
                price_label.place(x=13, y=50)

                # Display product Quantity
                x = product[0].product_id
                self.x_quantity  = product[1]
                self.quantity = tk.Label(item_frame, text=f"Quantity: {product[1]}", font=("Arial", 15, "bold"), fg = "#bbc2c7", bg = "black")
                self.quantity.place(x=25, y=100)

                # Display product brand
                brand_label = tk.Label(item_frame, text=f"Brand: {product[0].brand}", font=("Arial", 10))
                brand_label.place(x=10, y=70)

                self.billl_Amount = product[1]*product[0].price
                self.Amount = tk.Label(item_frame,text = f"Amount: {self.billl_Amount}", font = ("Comic Sans MS", 12, "bold"))
                self.Amount.place(x = 140, y= 235)
                
                plus_btn = tk.Button(item_frame, text="+", font=("Arial", 12, "bold"),
                                     command=lambda id=product[0].product_id, i=i, label=self.quantity,label2 = self.Amount: self.plus(i, id, label,label2),fg = "black",bg = '#57c962')
                plus_btn.place(x=40, y=140)


                minus_btn = tk.Button(item_frame, text = "-", font = ("Arial", 13, "bold"),
                                      command=lambda id=product[0].product_id, i=i, label=self.quantity, label2 = self.Amount: self.minus(i, id, label,label2),fg = "black",bg = '#579ac9')
                minus_btn.place(x = 95, y = 140)

                remove_btn = tk.Button(item_frame, text="Remove", font=("Arial", 13, "bold"),
                                       command=lambda id=product[0].product_id, i=i: self.remove_item(i, id),bg = '#a11a15',fg = 'black')
                remove_btn.place(x=40, y=240)
                
            self.products_items_frame.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
        # to remove item from cart
        def remove_item(self, num, product_id):
            loginpage.bill = []
            # Remove the item from the cart
            c.execute("DELETE FROM cart WHERE user_id = ? AND product_id = ?", (loginpage.user_id, product_id))
            conn.commit()

            # Refresh the cart display
            self.show_cart()
        #decrease item qty
        def minus(self, num, product_id, quantity_label, Amount_label):
            c.execute("SELECT price from products where product_id = ?", (product_id,))
            result = c.fetchone()
            price = int(result[0])
            current_value = int(quantity_label['text'].split(': ')[-1])
            if current_value == 1:
                messagebox.showinfo("Minimum Qty", "Minimum Quantity reached press the remove Button to remove item from cart...".upper())
            else:
                loginpage.bill.append(-price)
                loginpage.bill_Amount['text'] = sum(loginpage.bill)
                bill = price*(current_value-1)
                Amount_label['text'] = f"Amount: {bill}"
                quantity_label['text'] = f"Quantity: {current_value - 1}"
                c.execute("UPDATE cart SET quantity = ? WHERE user_id = ? AND product_id = ?",(current_value-1, loginpage.user_id,product_id))
                conn.commit()           
        #increase item quantity
        def plus(self, num, product_id, quantity_label, Amount_label):
            c.execute("SELECT price from products where product_id = ?", (product_id,))
            result = c.fetchone()
            print(type(result[0]))
            price = int(result[0])
            loginpage.bill.append(price)
            loginpage.bill_Amount['text'] = sum(loginpage.bill)
            current_value = int(quantity_label['text'].split(': ')[-1])
            bill = price*(current_value+1)
            Amount_label['text'] = f"Amount: {bill}"
            quantity_label['text'] = f"Quantity: {current_value + 1}"
            c.execute("UPDATE cart SET quantity = ? WHERE user_id = ? AND product_id = ?",(current_value+1, loginpage.user_id,product_id))
            conn.commit()
    #checking out
    def checkout(self):
        loginpage.label_thanks['text'] = f"Thank You For Choosing AMPLE ACCESS , {loginpage.username}!"
        loginpage.bill = []
        result = messagebox.askyesno("Confirmation", f"Are you sure to Checkout?")
        if not result:
            return
        query = "SELECT COUNT(*) AS cart_count FROM cart WHERE user_id = ?"
        c.execute(query, (self.user_id,))

        # Fetch the result
        result = c.fetchone()
        cart_count = result[0]

        # Check if the cart is empty
        if cart_count == 0:
            messagebox.showerror("Can't Checkout","YOUR CART IS EMPTY")
            return
        self.cart_frame.pack_forget()
        self.checkout_frame.pack()
        # Get the current date and time
        order_date = datetime.now().strftime("%d-%m-%Y")

        # Get the total amount from the cart
        c.execute("SELECT SUM(CAST(REPLACE(p.price, ',', '') AS DECIMAL(10,2)) * c.quantity) AS total_bill FROM cart c JOIN products p ON c.product_id = p.product_id WHERE c.user_id = ?;", (self.user_id,))
        total_amount = c.fetchone()[0]
    
        c.execute("SELECT address FROM User_credentials WHERE user_id = ?",(self.user_id,))
        address = c.fetchone()

        # Insert data into the orders table
        c.execute("INSERT INTO orders (user_id, order_date, total_amount, payment_status, shipping_address, shipping_method) VALUES (?, ?, ?, ?, ?, ?)",
                       (loginpage.user_id, order_date, total_amount, "PAID", f"{address[0]}", "Standard Shipping"))
        order_id = c.lastrowid

        c.execute("SELECT MAX(order_id) FROM orders")
        max_order_id = int(c.fetchone()[0])
        
        c.execute('INSERT INTO "transaction" (order_id, transaction_date, transaction_type, amount, payment_method, transaction_status) VALUES (?,?,?,?,?,?)',
                  (max_order_id,order_date,"ONLINE", total_amount, "VISA/MASTER CARD", "done"))
        
        # Retrieve cart items for user_id = 1
        c.execute("SELECT * FROM cart WHERE user_id = ?",(self.user_id,))
        cart_items = c.fetchall()

        # Insert data into the order_items table
        for cart_item in cart_items:
            item_id = cart_item[0]
            product_id = cart_item[1]
            quantity = cart_item[2]

            # Retrieve product attributes from products table
            c.execute("SELECT name, description, price FROM products WHERE product_id = ?", (product_id,))
            product_data = c.fetchone()
            name, description, price = product_data

            subtotal = quantity * price

            # Update stock in the products table
            c.execute("SELECT stock from products WHERE product_id = ?",(product_id,))
            stock = c.fetchone()
            
            new_stock = stock[0] - quantity
            c.execute("UPDATE products SET stock = ? WHERE product_id = ?", (new_stock, product_id))

            c.execute("INSERT INTO order_items (order_id, product_id, quantity, price, subtotal) VALUES (?, ?, ?, ?, ?)",
                           (order_id, product_id, quantity, price, subtotal))

        # Delete cart items for user_id = 1
        c.execute("DELETE FROM cart WHERE user_id = ?",(self.user_id,))

        # Commit the changes to the database
        conn.commit()
        self.label['text'] = f"It's Our Pleasure To Serve You... {self.username}"
        self.label3['text'] = f"Shipping Address: {address[0]}"
        self.label4['text'] = f"YOUR BILL : {total_amount}"
        self.label5['text'] = "HAPPY SHOPPINGG..❤"
        
    def added_to_cart(self):
        self.cart_frame.pack()
        self.checkout_frame.pack_forget()
        self.view_products_f.pack_forget()
        appp = self.Cart_app(self.cart_frame)
    #back from cart frame to view products frame
    def back_1(self):
        self.cart_frame.pack_forget()
        self.view_products_f.pack()
    def call(self,cat):
        app.show_products(cat)
    #associated with shop now button
    def turn_to_product(self):
        obj.intro.pack_forget()
        self.f1_introductory.pack()
    #associated with signup frame back button
    def f2tof1(self):
        self.f2_Signup.pack_forget()
        self.f1_introductory.pack()
    #associated with signup button
    def login_signup(self):
        self.f1_introductory.pack_forget()
        self.f2_Signup.pack()
    #fucntion to check whether the entered credentials are correct or wrong
    def validate_login(self,username, password):
        c = conn.cursor()
        c.execute('SELECT * FROM User_credentials WHERE username = ? AND password = ?', (username, password))
        result = c.fetchone()
        if result:
            return True
        else:
            return False
    def logout(self):
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_manager() == 'pack':
                widget.pack_forget()
        loginpage.f1_introductory.pack()
    def login(self):
        adminpage = Admin_account(root)
        self.bill = []
        username = self.username_entry.get().lower()
        password = self.pass_entry.get().lower()
        self.username = username
        self.password = password
        if username == "admin" and password == "exposure":
            self.username_entry.delete(0,END)
            self.pass_entry.delete(0,END)
            self.f1_introductory.pack_forget()
            adminpage.intro_admin.pack(side = TOP)
            adminpage.admin_features.pack(side = LEFT)
            adminpage.adm_dashboard.pack(side = RIGHT)
            adminpage.info_frame.place (x=15, y = 8)
            adminpage.info_frame_2.place (x = 402, y=8)
            adminpage.report.place(x = 15, y = 295)
            adminpage.type_text()
            return
        if self.validate_login(username, password):
            query = "SELECT user_id FROM User_credentials WHERE username = ?"
            c.execute(query, (self.username,))
            result = c.fetchone()
            user_id = result[0]
            self.user_id = user_id
            self.username_entry.delete(0,END)
            self.pass_entry.delete(0,END)
            self.f1_introductory.pack_forget()
            self.intro_user.pack()
            self.app = self.UserProductApp(self.view_products_f)
        elif username == "" and password == "":
            messagebox.showerror("warning", "please enter user id and password")
        elif username != "" and password == "":
            messagebox.showerror("warning", "please insert password")
        elif username == "" and password != "":
            messagebox.showerror("warning", "enter user ID")
        else:
            messagebox.showerror("warning", "please enter correct password and user id")
    #associated with sign-up
    def saveinfo(self):
        fname=self.Newuserfname.get()
        lname=self.Newuserlnameentry.get()
        useraddress=self.Newuseraddressentry.get()
        usrname=self.usernameentry.get()
        useremail=self.Newuseremailentry.get()
        password=self.Newuserpassentry.get()
        phonenumber=self.Newuserphentry.get()
        c.execute('SELECT MAX(user_id) FROM user_credentials')
        # fetch the result
        max_user_id = c.fetchone()[0]
        if max_user_id == None:
            max_user_id = 0
        if fname!="Type Firstname" and lname!="Type Last name" and useraddress!="Type Address" and usrname!="Type username" and useremail!="Type Your e-mail" and password!="Type Password" and phonenumber!="Type Phonenumber":
            if ("@gmail.com" in useremail or "@hotmail.com" in useremail or "cloud.neduet.edu.pk" in useremail) and len(phonenumber)==11:
                today = date.today()
                current_date = today.strftime("%d-%m-%Y")
                sql = "INSERT INTO User_credentials (user_id,first_name, Last_name, address, email_address, phone_no, username, password, created_date ) VALUES(?,?,?,?,?,?,?,?,?)"
                c.execute(sql, (max_user_id+1, fname.lower(), lname.lower(), useraddress.lower(), useremail.lower(),phonenumber.lower(),usrname.lower(), password.lower(), current_date))
                conn.commit()
                messagebox.showinfo("YOUR ACCOUNT CREATED SUCCESSFULLY🙂","username:"+usrname+"\npassword:"+password)
                for child in self.f2_Signup.winfo_children():
                    if isinstance(child, LabeledEntry):
                        child.delete(0, tk.END)
                self.f2_Signup.pack_forget()
                self.f1_introductory.pack()
            else:
                messagebox.showerror("ATTENTION🥺","PLEASE INPUT A VALID E-MAIL ADDRESS AND PHONE NUMBER")
        else:
            messagebox.showerror("ATTENTION🥺","PLEASE FILL ALL THE REQUIRED INFORMATION")
#admin features and all
class Admin_account:
    def __init__(self,obj1):
        end_date = date.today()
        start_date = end_date - timedelta(days=6)
        # Create a list of all dates in the last seven days
        date_range = [start_date + timedelta(days=i) for i in range(7)]
        # Initialize the orders_dates and orders lists with 0 for all dates
        orders_dates = [dt.day for dt in date_range]
        orders = [0] * len(date_range)

        
        self.c = 1
        self.root = obj.root
        self.obj1=obj1

        self.intro_admin = Frame(self.root, width = 1000, height = 100, bg = "black")

        #company name
        self.label_name = Label(self.intro_admin, text="\tAMPLE ACCESS", font = ('Algerian 40 bold'), bg = "black", fg = "white")
        self.label_name.place(x=10+20,y=0)
        #tagline
        self.label_tag = Label(self.intro_admin, text = "Here Is The One Stop Solution To All Your Needs.", font = ('Algerian 12 bold'), bg = "black", fg = "gray")
        self.label_tag.place(x=240+20,y=55)

##        logo
        img = tk.PhotoImage(file = "splogor.png")
        self.label4 = tk.Label(self.intro_admin,image = img)
        self.label4.image = img
        self.label4.place(x=10,y=10)

        self.admin_features = Frame(self.root, width = 215, height = 500, bg = "lightgrey")

        self.adm_dashboard = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.account_management = tk.Button(self.admin_features, text = "Delete Products",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.account_management)
        self.account_management.place(x=0, y=20)
        
        self.account_management_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        #for graph 1
        self.info_frame = Frame(self.adm_dashboard, width = 370, height = 272, bg = "#ebe7df")

        #for graph 2
        self.info_frame_2 = Frame(self.adm_dashboard, width = 370, height = 272, bg = "#ebe7df")

        # Execute the query to retrieve orders for the last seven days
        c.execute("SELECT SUBSTR(order_date, 1, 2) AS day, COUNT(*) FROM orders WHERE order_date BETWEEN ? AND ? GROUP BY day", (start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")))
        orders_data = c.fetchall()
        # Update the orders list with actual order counts
        for row in orders_data:
            order_date = int(row[0])
            order_count = row[1]
            index = orders_dates.index(order_date)
            orders[index] = order_count


        figg, ay = plt.subplots(figsize=(3.9, 2.2), facecolor='#ebe7df')
        
        ay.plot(orders_dates,orders,marker = 0)

        ay.set_title('Orders Data Stats (Weekly)')
        ay.set_ylabel('Total orders')
        ay.set_xlabel('Dates')

        canvas = FigureCanvasTkAgg(figg, master=self.info_frame_2)
        canvas.draw()
        canvas.get_tk_widget().place(x = 5, y = 15)

        self.xlabel = Label(self.info_frame_2, text= "Date", font = "Roboto 10 bold",fg = "black", bg = "#ebe7df").place(x=180, y = 240)
       
        self.report = tk.Text(self.adm_dashboard, width =  75, height = 8, font = ("Comic Sans MS", 12, "bold"),fg = "blue", bg  = "#e6e2d8")
        
        self.report_h = Label(self.report, text = "✍ REPORT AND SUGGESTIONS: ", font = "Helvetica 14 bold",fg = "black" , bg = "#e6e2d8" ).place(x = 0, y = 0)

        ## needed variables for total users and total orders
        #implementing AI for report and suggestions
        c.execute("SELECT COUNT(*) FROM orders WHERE order_date BETWEEN ? AND ?", (start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")))
        total_orders = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM User_credentials WHERE created_date BETWEEN ? AND ?", (start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")))
        total_users = c.fetchone()[0]

        average_sales_per_day = format(total_orders / 7, ".1f")
        average_users_per_day = format(total_users / 7, ".1f")

        if total_orders == 0:
            sugg = "There were no sales in the last 7 days."
        elif total_orders < 10:
            sugg = "Sales are lower than expected. Consider running a promotion to drive sales."
        elif total_orders >= 10 and total_orders < 20:
            sugg = "Sales are on track. Keep up the good work!"
        elif total_orders > 20:
            sugg = "Sales are higher than expected. Congratulations!"
        if total_users == 0:
            rew = "There were no new users in the last 7 days."
        elif total_users < 10:
            rew = "New user sign-ups are lower than expected. Consider improving your marketing strategy."
        elif total_users >= 10 and total_new_users < 20:
            rew = "New user sign-ups are on track. Keep up the good work!"
        elif total_users > 20:
            rew = "New user sign-ups are higher than expected. Congratulations!"
            
        self.reportcontent=f"\nANALYSIS FOR LAST 7 DAYS\n------------------------\nTotal Sales: {total_orders}\t\t\t\tTotal New Users: {total_users}\nAverage Sales Per Day: {average_sales_per_day}\t\t\t\tAverage New Users Per Day: {average_users_per_day}\nSUGGESTIONS AND REVIEW: {sugg} and {rew}"

        self.revenuel = Label(self.info_frame, text= "🧑 New Users", font = "Roboto 18 bold",fg = "black", bg = "#ebe7df").place(x=10, y = 10)
    
        users = [0] * len(date_range)

        # Execute the query to retrieve orders for the last seven days
        c.execute("SELECT SUBSTR(created_date, 1, 2) AS day, COUNT(*) FROM User_credentials WHERE created_date BETWEEN ? AND ? GROUP BY day", (start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")))
        users_data = c.fetchall()

        # Update the orders list with actual order counts
        for row in users_data:
            user_date = int(row[0])
            user_count = row[1]
            index = orders_dates.index(user_date)
            users[index] = user_count
        fig, ax = plt.subplots(figsize=(3.9, 2.2), facecolor='#ebe7df')

        #plot the sales data as a bar graph
        ax.bar(orders_dates,users)

        # set the chart title and axis labels
        ax.set_title('New Registered Users(Weekly)')
        ax.set_xlabel('Date')
        ax.set_ylabel('No Of Users')

        canvas = FigureCanvasTkAgg(fig, master=self.info_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x= 5, y = 15)

        self.xlabel = Label(self.info_frame, text= "Date", font = "Roboto 10 bold",fg = "black", bg = "#ebe7df").place(x=180, y = 240)
        #doing delete products parrt...
        self.searchproductslabel_1 = Label (self.account_management_frame, text = "Delete Products...".upper(), font = ('Algerian 25 bold'), bg = "lightblue", fg = "black")
        self.searchproductslabel_1.place(x=25, y=10)

        self.srch_l = Label(self.account_management_frame, text = "Enter Product Name: ",font = ('Roboto 18 bold'), bg = "lightblue")
        self.srch_l.place( x= 20, y=50)

        self.srch_e2 = Entry(self.account_management_frame, width = 25, font = "Roboto 18 bold")
        self.srch_e2.place(x = 290, y = 50)
        self.srch_e2.bind('<KeyRelease>', self.show_suggestions)

        self.search_b = tk.Button(self.account_management_frame, text="Search", command=lambda field = self.srch_e2, frame = self.account_management_frame : self.display_product(field,frame), fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)
        self.search_b.place( x = 335, y =100)

        self.suggestion_listbox2 = tk.Listbox(self.account_management_frame,width = 25)
        self.suggestion_listbox2.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.delete_b = tk.Button(self.account_management_frame, text = "Delete Product", command = self.delete,fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)

        self.view_products = tk.Button(self.admin_features, text = "   View Products    ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.view_products)
        self.view_products.place(x=0, y=80)

        self.view_products_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.add_products = tk.Button(self.admin_features, text = "   Add Products    ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.add_products)
        self.add_products.place(x=0, y=140)
        
        self.add_products_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.addproductslabel_1 = Label (self.add_products_frame, text = "ADD NEW PRODUCT NOW", font = ('Algerian 25 bold'), bg = "lightblue", fg = "black")
        self.addproductslabel_1.place(x=25, y=10)
        
        self.search_products = tk.Button(self.admin_features, text = "   Search Products    ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.search_products)
        self.search_products.place(x=0, y=200)

        self.search_products_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.searchproductslabel_1 = Label (self.search_products_frame, text = "Search And Update Your Inventory Now".upper(), font = ('Algerian 25 bold'), bg = "lightblue", fg = "black")
        self.searchproductslabel_1.place(x=25, y=10)

        self.view_users = tk.Button(self.admin_features, text = "   View Customers    ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.view_users, height = 1)
        self.view_users.place(x=0, y=260)

        self.view_users_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.viewuserslabel_1 = Label (self.view_users_frame, text = "Our Valuable Customers...🖤", font = ('Algerian 25 bold'), bg = "lightblue", fg = "black")
        self.viewuserslabel_1.place(x=120, y=0)

        self.view_order = tk.Button(self.admin_features, text = "   View Orders    ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.view_order)
        self.view_order.place(x=0, y=320)
        #view order
        self.view_order_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.vieworderlabel_1 = Label (self.view_order_frame, text = "This is the View Orders page", font = ('Algerian 25 bold'), bg = "lightblue", fg = "black")
        self.vieworderlabel_1.place(x=25, y=10)

        canvas = tk.Canvas(self.view_order_frame, width=760, height=500)
        canvas.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(self.view_order_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        self.orders_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.orders_frame, anchor="nw")
            
        self.view_sales = tk.Button(self.admin_features, text = "    Top Products   ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.view_sales)
        self.view_sales.place(x=0, y=380)

        self.view_sales_frame = Frame(self.root, width = 785, height = 500, bg = "lightblue")

        self.image2 = PhotoImage(file = "star.png")

        self.label3 = Label(self.view_sales_frame,text=" "*20)
        self.label3.config(image = self.image2)
        # to have the top products
        c.execute("""
            SELECT oi.product_id, SUM(oi.quantity * oi.price) AS revenue
            FROM order_items AS oi
            INNER JOIN orders AS o ON oi.order_id = o.order_id
            WHERE o.order_date BETWEEN ? AND ?
            GROUP BY oi.product_id
            ORDER BY revenue DESC
            LIMIT 3
        """, (start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")))

        # Fetch the results
        results = c.fetchall()

        # Store the product IDs and revenue in variables
        item_no1 = results[0][0] if len(results) >= 1 else None
        item_no2 = results[1][0] if len(results) >= 2 else None
        item_no3 = results[2][0] if len(results) >= 3 else None
        revenue1 = results[0][1] if len(results) >= 1 else 0
        revenue2 = results[1][1] if len(results) >= 2 else 0
        revenue3 = results[2][1] if len(results) >= 3 else 0
        items = [(item_no1,revenue1), (item_no2, revenue2), (item_no3,revenue3)]
        # Fetch product information for the top selling items
        product_info = {}
        for item_no in items:
            c.execute("SELECT name, price, brand, product_image, description FROM products WHERE product_id=?", (item_no[0],))
            result = c.fetchone()
            result = result + (item_no[1],)
            if result:
                product_info[item_no] = result
        # Create boxes for each top selling item
        row = 0
        for item_no, info in product_info.items():
            # Create a box for the item
            item_frame = tk.Frame(self.view_sales_frame, width=770, height=155, relief="solid", bd=5, bg = "#ddd1b3")
            item_frame.grid(row=row, column=0, padx=5, pady=5)

            # Retrieve the image data from the database
            image_data = info[3]
            image = pilImage.open(io.BytesIO(image_data))

            # Resize the image
            image = image.resize((110, 133))
            photo = ImageTk.PhotoImage(image)

            # Create a label to display the image
            label_image = tk.Label(item_frame, image=photo)
            label_image.image = photo
            label_image.place(x = 645, y = 2)

            # Create labels for the product information
            label_name = tk.Label(item_frame, text=f"***REVENUE: ", font=("Helvetica", 15, "bold"), bg = "black", fg = "#fbb931" )
            label_name.place(x = 200, y =0)
            
            label_name = tk.Label(item_frame, text=f"*TOP SELLING PRODUCT #{row+1}*", font=("Helvetica", 15, "bold"), bg = "black", fg = "#fbb931" )
            label_name.place(x = 200, y =0)
            
            label2_name = tk.Label(item_frame, text="Product Name: " + info[0], font=("Helvetica", 14), bg = "#ddd1b3")
            label2_name.place(x = 10, y =30)

            label2_name = tk.Label(item_frame, text="***REVENUE: " + str(info[-1]) + "***", font=("Helvetica", 15, "bold"), bg = "#ddd1b3")
            label2_name.place(x = 320, y =60)

            label_price = tk.Label(item_frame, text="Price: Rs" + str(info[1]), font=("Helvetica", 14), bg ="#ddd1b3")
            label_price.place(x  = 10, y = 50+5)

            label_brand = tk.Label(item_frame, text="Brand: " + info[2], font=("Helvetica", 14),bg = "#ddd1b3")
            label_brand.place(x = 10, y = 70+8)

            label_description = tk.Label(item_frame, text="Description: " + info[4], font=("Helvetica", 14), wraplength=650, bg = "#ddd1b3")
            label_description.place(x = 10, y= 100)

            row += 1
        
        self.adm_logout = tk.Button(self.admin_features, text = "       LogOut       ",font = ("Comic Sans MS", 13, "bold"),width = 21,bg="blue" ,fg="yellow", command = self.logout)
        self.adm_logout.place(x=0, y=440)

        
        c.execute("SELECT name FROM products")
        results  = c.fetchall()

        self.product_names = [result[0] for result in results]

        #creating add product interface

        self.labels = ["Name", "Description", "Price", "Category", "Image", "Stock", "Brand"]
        self.entries = []
        self.categories = ["SPORTS", "GARMENTS", "APPLIANCES", "ELECTRONICS"]
        self.category_var = tk.StringVar(value="Click to select the category")
        self.category_menu = tk.OptionMenu(self.add_products_frame, self.category_var, *self.categories)
        self.category_menu.config(width=47, height=2)
        self.browse_button = tk.Button(self.add_products_frame, text="Browse...", command=self.browse_file_add, width = 45 )
        self.add_button = tk.Button(self.add_products_frame, text="Add Product", command=self.add_product, width = 25)
        
        count = 70
        for label in self.labels:
            label_widget = tk.Label(self.add_products_frame, text=label, font = ('Roboto 18 bold'), bg = "lightblue")
            if label == "Category":
                self.category_menu.place(x = 155, y = count)
            elif label == "Image":
                self.browse_button.place(x = 155, y = count + 10)
            else:
                entry_widget = tk.Entry(self.add_products_frame, width = 25, font = "Roboto 18 bold")
                self.entries.append(entry_widget)
                entry_widget.place(x = 155, y = count)
            label_widget.place(x = 15, y = count)
            count += 40
        self.add_button.place( x = 150, y = 400)
        #add product int end

        #creating the search products interface
        self.srch_l = Label(self.search_products_frame, text = "Enter Product Name: ",font = ('Roboto 18 bold'), bg = "lightblue")
        self.srch_l.place( x= 20, y=50)

        self.srch_e = Entry(self.search_products_frame, width = 25, font = "Roboto 18 bold")
        self.srch_e.place(x = 290, y = 50)
        self.srch_e.bind('<KeyRelease>', self.show_suggestions)

        self.search_b = tk.Button(self.search_products_frame, text="Search", command = lambda field = self.srch_e, frame = self.search_products_frame : self.display_product(field, frame), fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)
        self.search_b.place( x = 335, y =100)
        self.update_b = tk.Button(self.search_products_frame,text = "Update database",command = self.save_changes,fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)

        self.suggestion_listbox = tk.Listbox(self.search_products_frame,width = 25)
        self.suggestion_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.edit_b = tk.Button(self.search_products_frame, text = "Edit Data", command = self.edit,fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)
        self.browse_button_1 = tk.Button(self.search_products_frame, text="Browse...", command=self.browse_file_srch, width = 20 )
# Got Remaining with view customers view orders view sales
#typing animation
    def type_text(self):
        analysis_text = "\nANALYZING THE DATA..."
        typing_text = self.reportcontent
        
        for _ in range(3):
            self.report.config(state=tk.NORMAL)
            self.report.insert(tk.END, analysis_text)
            self.report.config(state=tk.DISABLED)
            self.report.update()
            time.sleep(0.2)
            
            self.report.config(state=tk.NORMAL)
            self.report.delete(1.0, tk.END)
            self.report.config(state=tk.DISABLED)
            self.report.update()
            time.sleep(0.5)
        
        # Clear the text frame
        self.report.config(state=tk.NORMAL)
        self.report.delete(1.0, tk.END)
        self.report.config(state=tk.DISABLED)
        self.report.update()
        time.sleep(1)
            
        # Type the main text
        for char in typing_text:
            self.report.config(state=tk.NORMAL)
            self.report.insert(tk.END, char)
            self.report.config(state=tk.DISABLED)
            self.report.update()
            time.sleep(0.05)
        
        self.report.config(state=tk.NORMAL)
        self.report.insert(tk.END, "\nHAVE A GOOD DAY.!")
        self.report.config(state=tk.DISABLED)
    #picture browsing...
    def browse_file_add(self):
        self.browse_file(self.add_products_frame)
    def browse_file_srch(self):
        self.browse_file(self.search_products_frame)
    #add product helping function
    def browse_file(self,frame):
        filetypes = (("PNG files", "*.png"),("JPEG files", "*.jpg"))
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.image_path = filename
            self.browse_button.config(text="Uploaded", fg = "green")
            self.browse_button_1.config(text="Uploaded", fg = "green")
            self.image_frame = Frame(frame, width=130, height=180)
            x = self.display_img(self.image_path,self.image_frame)
            with pilImage.open(self.image_path) as img:
                img = img.resize((130, 180))
                img_bytes = io.BytesIO()
                img.save(img_bytes,format = 'PNG')
                self.binary_data = img_bytes.getvalue()
            if frame == self.search_products_frame:
                self.image_frame.place(x = 345, y =145)
            else:
                self.image_frame.place(x = 520, y =125)
                self.preview_l = Label(frame, text = "Preview",font = ("Comic Sans MS", 13, "bold"), bg = "black", fg = "white")
                self.preview_l.place(x = 545, y = 95)
   
     #add product helping function
    def add_product(self):
        data = []
        product_name = self.entries[0].get()
        c.execute("SELECT name FROM products WHERE name=?", (product_name,))
        result = c.fetchone()
        if result:
            messagebox.showerror("Error", "A product with this name is already added")
            return
        for i in range(7):
            if i > 4:
                ins = self.entries[i-2].get()
                data.append(ins)
            elif i != self.labels.index("Category") and i != self.labels.index("Image"):
                ins = self.entries[i].get()
                data.append(ins)
            else :
                if i == self.labels.index("Category"):
                    ins = self.category_var.get()
                    data.append(ins)
                elif i == self.labels.index("Image"):
                    image_data = self.image_path
                    image = pilImage.open(image_data).convert("RGB")
                    
                    # Resize the image
                    new_size = (130, 180)
                    image = image.resize(new_size)

                    with io.BytesIO() as output:
                        image.save(output, format="JPEG")
                        image_data = output.getvalue()
                    data.append(image_data)
        data.append(datetime.now().strftime("%d-%m-%Y"))
        c.execute("SELECT Max(product_id) from products")
        result = c.fetchone()
        data.insert(0,int(result[0])+1)
        c.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?)", tuple(data))
        conn.commit()
        for entry in self.entries:
            entry.delete(0,tk.END)    
        #search products helping function
        self.image_frame.place_forget()
        self.preview_l.place_forget()
        messagebox.showinfo("Success", "The product has been added to the database.")
#search products helper suggestion
    def show_suggestions(self,event):
        if self.suggestion_listbox.size() > 0:
            self.suggestion_listbox.delete(0, 'end')
        if self.suggestion_listbox2.size() > 0:
            self.suggestion_listbox2.delete(0, 'end')

        text = self.srch_e.get()
        text2 = self.srch_e2.get()
        if text:
            matches = [word for word in self.product_names if word.startswith(text)]
            for match in matches:
                self.suggestion_listbox.insert(tk.END, match)
                self.suggestion_listbox.configure(state ='normal')
                
        elif text2:
            # Find all words that start with the text
            matches = [word for word in self.product_names if word.startswith(text2)]
            for match in matches:
                self.suggestion_listbox2.insert(tk.END, match)
                self.suggestion_listbox2.configure(state ='normal')
        if self.srch_e.get() == "" or ('matches' not in locals() or matches == []):
            self.suggestion_listbox.place_forget()
        if self.srch_e2.get() == "" or ('matches' not in locals() or matches == []):
            self.suggestion_listbox2.place_forget()
        else:
            self.suggestion_listbox.place(x = 290, y = 70)
            self.suggestion_listbox2.place(x = 290, y = 70)
    #to have clicked suggestion on listbox
    def on_listbox_select(self,event):
        selection = event.widget.curselection()
        if selection:
            selected_suggestion = event.widget.get(selection[0])
        
            # set the entry box to the selected suggestion
            text = self.srch_e.get()
            text2 = self.srch_e2.get()
            if text:
                self.srch_e.delete(0, tk.END)
                self.srch_e.insert(0, selected_suggestion)
                self.suggestion_listbox.place_forget()
                self.suggestion_listbox2.place_forget()
            if text2:
                self.srch_e2.delete(0, tk.END)
                self.srch_e2.insert(0, selected_suggestion)
                self.suggestion_listbox2.place_forget()
                self.suggestion_listbox.place_forget()
    #deleting the product
    def delete(self):
        name = self.srch_e2.get()
        result = messagebox.askyesno("Confirmation", f"Are you sure to delete {name} ?")
        exclude = ['!label','!label2', '!button', '!entry','!listbox','!button3','!button2','!button4']
        for widget in self.account_management_frame.winfo_children():
            if str(widget.winfo_name()) in exclude:
                if str(widget.winfo_name()) in ['!button3','!button2','!button4']:
                    widget.place_forget()
                pass
            else:
                widget.destroy()
        self.srch_e2.delete(0,END)
        if result:
            self.product_names.remove(name)
            sql = "DELETE FROM products WHERE name = ?"
            result = c.execute(sql, (name,))
            tk.messagebox.showinfo("SUCCESS!!", f"Database Of Product {name} deleted..! ")
    #searching product
    def search(self,name):
        conn = sqlite3.connect("e commerce.db")
        c = conn.cursor()
        sql = "SELECT * FROM products WHERE name =?"
        result = c.execute(sql,(name,))
        for r in result:
            row =list(r)
        conn.commit()
        product = Admin_account.Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return product
    #editing product info.
    def edit(self):
        for key in self.variables:
            if key != "image" and key != "product_id":
                self.entries[key].config(state='normal')
        self.edit_b.place_forget()
        self.update_b.place(x = 80,y = 400)
        self.browse_button_1.place(x = 345, y = 350)
        
    # Create a function to save the changes made to the fields
    def save_changes(self):
        for key in self.variables:
            if key!="image":
                self.variables[key] = self.entries[key].get()
            else:
                if hasattr(adminpage, 'binary_data'):
                    self.variables['image'] = self.binary_data
        query = "UPDATE products SET name = ?, description = ?, price = ?, product_image = ?, stock = ?, brand = ? WHERE product_id =?"
        c.execute(query,(self.variables['name'], self.variables['description'], self.variables['price'], self.variables['image'], self.variables['stock'], self.variables['brand'],self.variables['product_id']))
        conn.commit()
        exclude = ['!label','!label2', '!button', '!entry','!listbox','!button3','!button2','!button4'] 
        for widget in self.search_products_frame.winfo_children():
            if str(widget.winfo_name()) in exclude:
                if str(widget.winfo_name()) in ['!button3','!button2','!button4']:
                    widget.place_forget()
                pass
            else:
                widget.destroy()
        self.srch_e.delete(0,END)
        tk.messagebox.showinfo("seccess", "Database Updated")

    #displaying searched product
    def display_product(self, field, frame):
        product = self.search(field.get())
        self.prod = product
        
        self.variables  = {"product_id": product.product_id,"name": product.name,"price": product.price,"category": product.category,"description": product.description,"image": product.image,"stock": product.stock,"brand": product.brand}

        self.image_frame = Frame(frame, width=130, height=180)
        self.image_frame.place(x = 345, y =145)

        self.entries = {}
        count = 1
        for key in self.variables:
            if key != "image":
                entry_label = Label(frame, text=key+": ",font = "arial 13 bold",bg = "lightblue")
                entry_label.place(x = 10, y = 120+(25*count))
                entry = Entry(frame, width=20,font = "arial 13 bold")
                entry.insert(END, self.variables[key])
                entry.config(state='disabled')
                self.entries[key] = entry
                entry.place(x = 150,y =120+(25*count))
                count+=1
            else:
                image_label = Label(frame, text = "Image",font = "georgia 12 bold").place(x=385, y=325)
                self.display_img(product.image,self.image_frame)
                self.update = 1
        if frame == self.account_management_frame:
            self.delete_b.place(x = 80,y = 400)
        else:
            self.edit_b.place(x = 80, y = 400)

   #dispplay image helper     
    def display_img(self,imag,frame):
        
        if type(imag) != bytes:
            image = pilImage.open(imag)
            # Convert the image to bytes format
            img = image
        else:
            img = pilImage.open(io.BytesIO(imag))
        img = img.resize((130, 180), pilImage.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(frame, image=img)
        img_label.image = img
        img_label.place(x=0, y=0)


    class Product:
        def __init__(self, product_id, name, description, price, category, image, stock, brand): 
            self.product_id = product_id
            self.name = name
            self.description = description
            self.price = price
            self.image = image
            self.category = category
            self.stock = stock
            self.brand = brand
    class ProductApp:
        def __init__(self, master):
            master.pack()
            self.master = master

            self.product_list = []

            # Create buttons for each category
            self.sports_button = tk.Button(self.master, text="SPORTS", command=lambda: self.show_products("SPORTS"), fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)
            self.sports_button.place(x=60, y=5)

            self.garments_button = tk.Button(self.master, text="GARMENTS", command=lambda: self.show_products("GARMENTS"),fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"),width = 14)
            self.garments_button.place(x=80+150+10, y=5)

            self.appliances_button = tk.Button(self.master, text="APPLIANCES", command=lambda: self.show_products("APPLIANCES"),fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"), width = 14)
            self.appliances_button.place(x=80+300+40, y=5)

            self.electronics_button = tk.Button(self.master, text="ELECTRONICS", command=lambda: self.show_products("ELECTRONICS"),fg = "white", bg = "#474545",font = ("Comic Sans MS", 12, "bold"), width = 14)
            self.electronics_button.place(x=80+450+60, y=5)

            # Create product display area
            self.product_frame = tk.Frame(self.master, width=760, height=450, bd=2, relief="groove")
            self.product_frame.place(x=10, y=50)

            # Create scrollbar for product display area
            self.scrollbar = ttk.Scrollbar(self.product_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Create canvas for product display area
            self.canvas = tk.Canvas(self.product_frame, width=750, height=450, yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar.config(command=self.canvas.yview)

            # Create frame for product items
            self.product_items_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.product_items_frame, anchor=tk.NW)

            self.show_products("SPORTS")
        def fetch_products(self, category):
            # Fetch products from database
            conn = sqlite3.connect("C:\DISK D\FE SPRING\OOP\e commerce.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE category=?", (category,))
            rows = cursor.fetchall()
            conn.close()

            # Convert fetched rows to Product objects
            products = []
            for row in rows:
                product = Admin_account.Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                products.append(product)

            return products
        def show_products(self, category):
            # Clear previous product items
            for widget in self.product_items_frame.winfo_children():
                widget.destroy()

            # Fetch products for selected category
            self.product_list = self.fetch_products(category)

            # Create product items
            if self.product_list == []:
                empty_label = tk.Label(self.product_items_frame, text = "NO PRODUCTS TO SHOW... ", font = ("Arial",12,"bold"))
                empty_label.place(x = 10, y =10)
                return
                
            for i, product in enumerate(self.product_list):
                # Create frame for each product item
                item_frame = tk.Frame(self.product_items_frame, width=750, height=190, bd=2, relief="groove")
                item_frame.grid(row=i, column=0, padx=5, pady=5)
                #display product id as well
                id_label = tk.Label(item_frame, text = "Product ID: "+str(product.product_id), font = ("Arial",12,"bold"))
                id_label.place(x = 10, y =160)

                # Display product name
                name_label = tk.Label(item_frame, text="Name: "+product.name, font=("Arial", 12, "bold"),wraplength=120)
                name_label.place(x=10, y=10)

                # Display product image
                img = pilImage.open(io.BytesIO(product.image))
                img = img.resize((130, 180), pilImage.Resampling.LANCZOS)
                img = ImageTk.PhotoImage(img)
                img_label = tk.Label(item_frame, image=img)
                img_label.image = img
                img_label.place(x=150, y=0)

                # Display product description
                desc_h = tk.Label(item_frame, text = "Description: ",font = ("arial", 12, "bold")).place(x = 300,y = 15)
                desc_label = tk.Label(item_frame, text=product.description+".", font=("Arial", 12), wraplength=360)
                desc_label.place(x=300, y=40)

                # Display product price
                price_label = tk.Label(item_frame, text=f"Price: {product.price} Rs", font=("Arial", 12, "bold"))
                price_label.place(x=600, y=10)

                # Display product stock
                stock_label = tk.Label(item_frame, text=f"Stock: {product.stock}", font=("Arial", 10, "bold"))
                stock_label.place(x=300, y=160)

                # Display product brand
                brand_label = tk.Label(item_frame, text=f"Brand: {product.brand}", font=("Arial", 10))
                brand_label.place(x=600, y=160)

            # Update the canvas scroll region to fit all product items
            self.product_items_frame.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))
    class User:
        def __init__ (self,user_id,first_name,Last_name, address, email_address, phone_number, username, password):
            self.user_id = user_id
            self.first_name  = first_name
            self.last_name = Last_name
            self.address = address
            self.email_address = email_address
            self.phone = phone_number
            self.username = username
            self.password = password
    class User_app:
        def __init__(self, master):
            master.pack(side="bottom", fill="both", expand=True)
            self.master = master
            
            self.users_frame = tk.Frame(self.master, width=760, height=450, bd=2, relief="groove")
            self.users_frame.place(x=0, y=40)

            self.scrollbar = ttk.Scrollbar(self.users_frame, orient=tk.VERTICAL)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.canvas = tk.Canvas(self.users_frame, width=760, height=450, yscrollcommand=self.scrollbar.set)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            self.scrollbar.config(command=self.canvas.yview)

            self.master = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=self.master, anchor=tk.NW)

            self.show_user(self.master)
            
        def show_user(self,frame):
            for widget in frame.winfo_children():
                widget.destroy()
            conn = sqlite3.connect("C:\DISK D\FE SPRING\OOP\e commerce.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM User_credentials")
            use = cursor.fetchall()
            conn.close()

            # Convert fetched rows to Product objects
            users =[]
            for row in use:
                user = Admin_account.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7])
                users.append(user)
            if users == []:
                empty_label = tk.Label(frame, text = "NO Users TO SHOW... ", font = ("Arial",12,"bold"))
                empty_label.place(x = 10, y =50)
                return
                
            for i, user in enumerate(users):
                # Create frame for each product item
                item_frame = tk.Frame(frame, width=370, height=230, bd=3, borderwidth=3, relief="solid")
                item_frame.grid(row=i//2, column=i%2, padx=5, pady=5)
                
                img = ImageTk.PhotoImage(file  = "profile.png")

                img_label = tk.Label(item_frame, image=img)
                img_label.image = img
                img_label.place(x=280, y=5)
                
                #display user id as well
                id_label = tk.Label(item_frame, text = "User ID: "+str(user.user_id), font = ("Arial",12,"bold"))
                id_label.place(x = 10, y =160)
                # Display user name
                name_label = tk.Label(item_frame, text="Name: "+user.first_name+" "+user.last_name, font=("Arial", 12, "bold"))
                name_label.place(x=10, y=10)
                #Display product description
                address_l = tk.Label(item_frame, text = "address: "+user.address,font = ("arial", 12, "bold"),wraplength= 280).place(x = 10,y = 140)
                email_label = tk.Label(item_frame, text="email address: "+user.email_address, font=("Arial", 12))
                email_label.place(x=10, y=65)

                phone_label = tk.Label(item_frame, text="Phone Number: "+str(user.phone), font=("Arial", 12))
                phone_label.place(x=10, y=90)

                username_label = tk.Label(item_frame, text="Username: "+user.username, font=("Arial", 12,'bold'), fg = "grey")
                username_label.place(x=10, y=110)
                
            frame.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def load_orders(self):
        conn = sqlite3.connect("e commerce.db")
        c = conn.cursor()        
        c.execute('''SELECT orders.order_id, orders.order_date, orders.total_amount,
                      orders.shipping_address, User_credentials.first_name, User_credentials.Last_name,
                      GROUP_CONCAT(products.name, ', ') AS item_names
                      FROM orders
                      INNER JOIN User_credentials ON orders.user_id = User_credentials.user_id
                      INNER JOIN order_items ON orders.order_id = order_items.order_id
                      INNER JOIN products ON order_items.product_id = products.product_id
                      GROUP BY orders.order_id''')
        orders = c.fetchall()
        conn.close()
        return orders
    #orders display
    def create_order_box(self,i,frame, order):
        order_box = tk.Frame(frame, width=750, height=120, bd=3, borderwidth=3, relief="solid")
        order_box.grid(row=i, column = 1, pady=5, padx = 5)
        
        order_id_lbl = tk.Label(order_box, text=f"Order ID:{order[0]}", font = ("Comic Sans MS",14, "bold"), fg = "blue")
        order_id_lbl.place(x = 350, y =5)

        date_lbl = tk.Label(order_box, text=f"Date:{order[1]}", font = ("Comic Sans MS",12, "bold"))
        date_lbl.place(x = 10, y = 5)
        
        total_lbl = tk.Label(order_box, text=f"Total Amount:{order[2]}", font = ("Comic Sans MS",12, "bold"))
        total_lbl.place(x = 500, y = 5)
        
        address_lbl = tk.Label(order_box, text=f"Shipping Address:{order[3]}", font = ("Comic Sans MS",12, "bold"))
        address_lbl.place(x = 10, y = 40)
        
        user_lbl = tk.Label(order_box, text=f"User:{order[4]} {order[5]}", font = ("Comic Sans MS",13, "bold"))
        user_lbl.place(x = 500, y =40)

        items_lbl = tk.Label(order_box, text=f"Items:{order[6]}", font = ("Comic Sans MS",13, "bold"), fg = "grey")
        items_lbl.place(x = 20, y = 80)
        
    def logout(self):
        result = messagebox.askyesno("Confirmation", "Are you Sure?")
        if not result:
            return
        for widget in root.winfo_children():
            if isinstance(widget, tk.Frame) and widget.winfo_manager() == 'pack':
                widget.pack_forget()
        loginpage.f1_introductory.pack()
    def account_management(self):
        self.adm_dashboard.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.search_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.entries = {}
        exclude = ['!label','!label2', '!button', '!entry','!listbox','!button3','!button2','!button4']
        for widget in self.account_management_frame.winfo_children():
            if str(widget.winfo_name()) in exclude:
                if str(widget.winfo_name()) in ['!button3','!button2','!button4']:
                    widget.place_forget()
                pass
            else:
                widget.destroy()
        self.srch_e2.delete(0,END)
        self.account_management_frame.pack()
    def add_products(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.search_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.add_products_frame.pack()
    def view_products(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.search_products_frame.pack_forget()
        app = self.ProductApp(self.view_products_frame)
        
    def search_products(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.entries = {}
        exclude = ['!label','!label2', '!button', '!entry','!listbox','!button3','!button2','!button4'] 
        for widget in self.search_products_frame.winfo_children():
            if str(widget.winfo_name()) in exclude:
                if str(widget.winfo_name()) in ['!button3','!button2','!button4']:
                    widget.place_forget()
                pass
            else:
                widget.destroy()
        self.srch_e.delete(0,END)
        self.search_products_frame.pack()
    def view_users(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.search_products_frame.pack_forget()
        app = self.User_app(self.view_users_frame)
    def view_order(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.view_sales_frame.pack_forget()
        self.search_products_frame.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack()
        orders = self.load_orders()
        for i,order in enumerate(orders):
            self.create_order_box(i,self.orders_frame, order)  
    def view_sales(self):
        self.adm_dashboard.pack_forget()
        self.account_management_frame.pack_forget()
        self.add_products_frame.pack_forget()
        self.view_products_frame.pack_forget()
        self.search_products_frame.pack_forget()
        self.view_users_frame.pack_forget()
        self.view_order_frame.pack_forget()
        self.view_sales_frame.pack()

root=Tk()
obj=introductory_page(root)
obj.intro.pack()
loginpage = user_account(obj)
##adminpage = Admin_account(root)

root.configure(background="grey")
root.mainloop()
