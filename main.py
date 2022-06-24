#This program is to ensure good data collection of Julie's Party Hire Store#

#import tkinter
from tkinter import *
import random
import re

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