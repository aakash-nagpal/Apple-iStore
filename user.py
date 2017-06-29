#!/usr/bin/python
# -*- coding:utf-8 -*- #

import random, datetime, getpass

class user:
    # uname = ""
    # upass = ""
    def __init__(self, uname, upass):
        self.uname = uname
        self.upass = upass

    # Function to write user details
    def user_details(self):
        with open("/home/aakash/Documents/MyTask/Admin/userdata.csv", "a") as f:
            f.write(self.uname + ",")
            f.write(self.upass + "\n")

    # Function to verify legitimacy of user
    def verify_user(self):
        flag = 0
        with open("/home/aakash/Documents/MyTask/Admin/userdata.csv", "r") as f:
            data = f.readlines()
            for lines in data:
                line = lines.split(",")
                if self.uname == line[0] and self.upass == line[1].rstrip("\n"):
                    print "You are successfully logged in."
                    flag = 1
                    self.action()
        if flag == 0:
            print "Please enter valid credentials"
    
    def action(self):
        print "1. Wanna buy a phone?"
        print "2. Wanna repair a phone?"
        uchoice = input("Enter your choice : ")
        if uchoice == 1:
            self.buy_phone()
        if uchoice == 2:
            self.repair_phone()


# Function to generate bill
    def billing(self, uchoice):
        with open("/home/aakash/Documents/MyTask/Admin/phonelist.csv","r") as f:
            data = f.readlines()
            qty = input("Enter quantity : ")
            for lines in data:
                line = lines.split(",")
                if uchoice == int(line[0]):
                    bill_amount = int(line[3]) * qty
            print "Amount : ₹", bill_amount
        f.close()

    # Function to order phone
    def buy_phone(self):
        i = 0
        with open("/home/aakash/Documents/MyTask/Admin/phonelist.csv","r") as f:
            phone_models = []
            data = f.readlines()
            for lines in data:
                line = lines.split(",")
                phone_models.append(line[1] + " " + line[2])
            for i in range(len(phone_models)):
                print i + 1, phone_models[i]
            uchoice = input("\nSelect model : ")
            a = str(datetime.datetime.now()).split(" ")
            with open("/home/aakash/Documents/MyTask/Admin/user_history.csv", "a") as f2:
                f2.write(self.uname + "," + "Order"+ "," + a[0] + "," + phone_models[uchoice - 1] + "," + None + "," +"Successful\n")
        f.close()
        f2.close()
        self.billing(uchoice)

# Function to place request for repair
    def repair_phone(self):
        with open("/home/aakash/Documents/MyTask/Admin/phonelist.csv","r") as f:
            with open("/home/aakash/Documents/MyTask/Admin/user_history.csv", "a") as f2:
                phone_models = []
                data = f.readlines()
                for lines in data:
                    line = lines.split(",")
                    phone_models.append(line[1] + " " + line[2])
                for i in range(len(phone_models)):
                    print i + 1, phone_models[i]
                phone = input("Select your phone model : ")
                c = random.randint(100,1000)
                print "Your complaint number is : ", c
                a = str(datetime.datetime.now()).split(" ")
                f2.write(self.uname + "," + "Repair" + "," + a[0] + "," + phone_models[phone - 1] + "," + str(c) + "," + "Pending\n")
        f2.close()
        f.close()


print("1. New user")
print("2. Existing user")
user_choice = input("Enter your choice : ")
uname = raw_input("Enter Username : ")
upass = getpass.getpass("Enter Password : ")
a = user(uname, upass)
if user_choice == 1:
    a.user_details()
elif user_choice == 2:
    a.verify_user()
else:
    print "Wrong input"
