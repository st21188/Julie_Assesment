##############################################################################
#This program is to ensure a good data collection of Julie's Party Hire Store#
##############################################################################

#import tkinter so we can make a GUI
from tkinter import *
import random
import re

#quit command
def quit():
    main_window.destroy()

#print details of all the customers
def print_customer_details ():
    global total_entries, name_count



    #Create the column headings
    name_count =0
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Full Name").grid(column=1, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Receipt Number").grid(column=2, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Item").grid(column=3, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Number of Item/s").grid(column=4, row=10)

    #add each item in the list onto its own row
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4,row=name_count+11)
        main_window.geometry("")
        name_count += 1

#Check the inputs are all valid
def append_details ():
    global customer_details, entry_name, entry_name_first, entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_item, entry_item_blank, entry_quantity, entry_quantity_blank, entry_quantity_limit, entry_quantity_letter, total_entries

#Check that Full Name is not blank, set error text if blank  
    if len(re.findall(r'\w+', entry_name.get())) == 0:
        entry_name_blank.destroy()
        entry_name_first.destroy()
        entry_name_blank = Label(main_window,fg="red", text="Sorry - this can't be blank, please enter the customers Full Name")
        entry_name_blank.grid(row=4, column=2)

 #Check if only first name is entered in the full name entry          
    if 0 < len(re.findall(r'\w+', entry_name.get())) < 2:
        entry_name_blank.destroy()
        entry_name_first.destroy()
        entry_name_first = Label(main_window, text="Only First name is entered. Enter the customer's Full Name", fg="red")
        entry_name_first.grid(row=4, column=2)
        entry_name_blank.destroy()
       
    if len(re.findall(r'\w+', entry_name.get())) > 1:
        entry_name_blank.destroy()
        entry_name_first.destroy()
   

#Check that Receipt Number is not blank, set error text if blank    
    if len(re.findall(r'\w+', entry_receipt.get())) == 0 :
        entry_receipt_blank.destroy()
        entry_receipt_string.destroy()
        entry_receipt_special.destroy()
        entry_receipt_blank = Label(main_window,fg="red", text="Sorry - this can't be blank, please enter the Receipt Number") .grid(column=5,row=4)
   
#Check if there's a letter in the receipt number entry
    if len(re.findall(r'\w+', entry_receipt.get())) != 0:  
        if entry_receipt.get().strip().isdecimal() == False:
            entry_receipt_blank.destroy()
            entry_receipt_string.destroy()
            entry_receipt_special.destroy()
            receipt_no_string = Label(main_window, text="A letter is entered. Enter the Receipt Number only", fg="red") .grid(row=4, column=5)
   
    if len(re.findall(r'\w+', entry_receipt.get())) != 0:    
        if entry_receipt.get().strip().isalnum() == False:
            entry_receipt_blank.destroy()
            entry_receipt_string.destroy()
            entry_receipt_special.destroy()
            entry_receipt_string = Label(main_window, text="A special character or a space is entered. Enter the Receipt Number only", fg="red") .grid(row=4, column=5)

    if entry_receipt.get().strip().isdecimal() == True:
        entry_receipt_blank.destroy()
        entry_receipt_string.destroy()
        entry_receipt_special.destroy()
     


 #Check that Item is not blank, set error text if blank    
    if len(re.findall(r'\w+', entry_item.get())) == 0:
        entry_item_blank.destroy()
        Label(main_window,fg="red", text="Sorry - this can't be blank, please enter the Item that was hired") .grid(column=2,row=6)
     
    if len(re.findall(r'\w+', entry_item.get())) > 0:
        entry_item_blank.destroy()

    #Check the number of item/s is not blank and between 1 and 500, set error text if blank  
    if len(re.findall(r'\w+', entry_quantity.get())) == 0:
        entry_quantity_blank.destroy()
        entry_quantity_letter.destroy()
        entry_quantity_limit.destroy()
        entry_quantity_blank = Label(main_window, text="Sorry - this can't be blank, please enter the number of item/s hired", fg="red") .grid(row=6, column=5)

#check if quantity is blank
    if len(re.findall(r'\w+', entry_quantity.get())) != 0:  
        entry_quantity_blank.destroy()
        entry_quantity_letter.destroy()
        entry_quantity_limit.destroy()
       
        #if quanity is not blank then try converting it to an int
        try:
             inter = int(entry_quantity.get())
             if 500 < int(entry_quantity.get()) or int(entry_quantity.get()) < 0:
                entry_quantity_blank.destroy()
                entry_quantity_letter.destroy()
                entry_quantity_limit.destroy()
                entry_quantity_limit = Label(main_window, text="Invalid value is entered. Please enter a number between 1 - 500", fg="red") .grid(row=6, column=5)

                if 501 > int(entry_quantity.get()) > 0:
                    entry_quantity_blank.destroy()
                    entry_quantity_letter.destroy()
                    entry_quantity_limit.destroy()

        #if quantity cannot be converted to an int then display a custom error message    
        except ValueError:
            entry_quantity_letter = Label(main_window, text="Invalid value is entered. Only enter the Quantity", fg="red") .grid(row=6, column=5)
           
#Remember to fix issues with .isdecimal identifying spaces

#append details if all requirements are met
    if len(re.findall(r'\w+', entry_name.get())) > 1:
        if entry_receipt.get().strip().isdecimal() == True:
            if len(re.findall(r'\w+', entry_item.get())) > 0:
                    if entry_quantity.get().strip().isdecimal() == True:
                         if 501 > int(entry_quantity.get()) > 0:
                            customer_details.append([entry_name.get().title(),entry_receipt.get(),entry_item.get(),entry_quantity.get()])
                            entry_name.delete(0,'end')
                            entry_receipt.delete(0,'end')
                            entry_item.delete(0,'end')
                            entry_quantity.delete(0,'end')
                            total_entries +=  1


#delete a row from the list
def delete_row ():
    #these are the global variables that are used
    global customer_details, delete_item, total_entries, name_count
    #find which row is to be deleted and delete it
    del customer_details[int(delete_item.get())]
    total_entries -= 1
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="                    ").grid(column=0,row=name_count+10)
    Label(main_window, text="                    ").grid(column=1,row=name_count+10)
    Label(main_window, text="                    ").grid(column=2,row=name_count+10)
    Label(main_window, text="                    ").grid(column=3,row=name_count+10)
    Label(main_window, text="                    ").grid(column=4,row=name_count+10)
    #print all the items in the list
    print_customer_details()

#create the buttons and labels
def GUI():

    #these are the global variables that are used
    global customer_details, entry_name, entry_name_first, entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_item, entry_item_blank, entry_quantity, entry_quantity_blank, entry_quantity_limit, entry_quantity_letter, total_entries, delete_item
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location

    Label(main_window, text="Full Name:") .grid(column=1,row=3,pady=10, sticky=E)
    entry_name = Entry(main_window)
    entry_name.grid(column=2,row=3)

    Label(main_window, text="Receipt Number:") .grid(column=4,row=3,pady=10, sticky=E)
    entry_receipt = Entry(main_window)
    entry_receipt.grid(column=5,row=3)

    Button(main_window,fg="dark red", text="Quit",command=quit,width = 10) .grid(column=5, row=12,pady=3, sticky=E)
    Button(main_window,text="Append Details",command=append_details) .grid(column=2,row=7,pady=(10,30), sticky=E)
    Button(main_window,text="Print Details",command=print_customer_details,width = 10) .grid(column=5,row=7,pady=(10,30), sticky=E)

    Label(main_window, text="Item Hired:") .grid(column=1,row=5,pady=10, sticky=E)
    entry_item = Entry(main_window)
    entry_item.grid(column=2,row=5)

    Label(main_window, text="Number of Item/s:") .grid(column=4,row=5,pady=10, sticky=E)
    entry_quantity = Entry(main_window)
    entry_quantity.grid(column=5,row=5)

    Label(main_window, text="Row #") .grid(column=1,row=8,sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=2,row=8)

    Button(main_window,text="Delete Row",command=delete_row,width = 10) .grid(column=5,row=8,pady=3, sticky=E)
    Label(main_window, text="               ") .grid(column=2,row=0)


def placeholder():
    global entry_name_first, entry_name_blank, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_item_blank, entry_quantity_blank, entry_quantity_letter, entry_quantity_limit
    entry_name_blank = Label(main_window, text="")
    entry_name_first = Label(main_window, text="")
    entry_receipt_string = Label(main_window, text="")
    entry_receipt_blank = Label(main_window, text="")
    entry_receipt_special = Label(main_window, text="")
    entry_item_blank = Label(main_window, text="")
    entry_quantity_blank = Label(main_window, text="")
    entry_quantity_letter = Label(main_window, text="")
    entry_quantity_limit = Label(main_window, text="")

#start the program running
def main():

    #these are the global variables that are used
    global main_window
    global customer_details, entry_name,entry_receipt,entry_item,entry_quantity, total_entries

    #create empty list for camp details and empty variable for entries in the list
    customer_details = []
    total_entries = 0

    #create the GUI and start it up
    main_window =Tk()
    GUI()
    placeholder()

    main_window.title("Tracking Program")

    main_window.mainloop()
   
   
main()
