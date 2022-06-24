#This program is to ensure good data collection of Julie's Party Hire Store#

#import tkinter
from tkinter import *
import random
import re


#quit command
def quit():
    main_window.destroy()

# print details of customers
def print_customer_details ():
    global total_entries, name_count


    #Create column headings 
    name_count =0
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Full Name").grid(column=1, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Receipt Number").grid(column=2, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Item").grid(column=3, row=10)
    Label(main_window, font=("Helvetica 10 bold"), text="Number of Item/s").grid(column=4, row=10)

    #add each item into list and row
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4,row=name_count+11)
        main_window.geometry("")
        name_count += 1



#delete list
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




#main program
def main():

    #global variables
    global main_window
    global customer_details, entry_name, entry_receipt, entry_item, entry_quantity, total_entries

    #create list
    customer_details = []
    total_entries = 0

    # GUI
    main_window = Tk()
    GUI()

    main_window.title("Tracking Program")

    main_window.mainloop()

main()