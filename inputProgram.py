'''This program lets the user input:
Company Name, Job Title, Required Languages/Frameworks,
Salary, Address,
average monthly rent in the area,
distance (miles) from home,
and current application status
'''

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])
        e7.delete(0, END)
        e7.insert(END, selected_tuple[7])
        e8.delete(0, END)
        e8.insert(END, selected_tuple[8])
    except IndexError:
        pass

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(company_text.get(), title_text.get(), requirements_text.get(), address_text.get(), salary_text.get(), rent_text.get(), distance_text.get(), status_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(company_text.get(), title_text.get(), requirements_text.get(), address_text.get(), salary_text.get(), rent_text.get(), distance_text.get(), status_text.get())
    list1.delete(0, END)
    list1.insert(END, (company_text.get(), title_text.get(), requirements_text.get(), address_text.get(), salary_text.get(), rent_text.get(), distance_text.get(), status_text.get()))
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def update_command():
    backend.update(selected_tuple[0], company_text.get(), title_text.get(), requirements_text.get(), address_text.get(), salary_text.get(), rent_text.get(), distance_text.get(), status_text.get())
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

#creation of window object
window=Tk()

window.wm_title("Job Search Helper")

l1=Label(window, text="Company Name")
l1.grid(row=0, column=0)

l2=Label(window, text="Job Title")
l2.grid(row=0, column=2)

l3=Label(window, text="Wanted Languages/Frameworks")
l3.grid(row=1, column=0)

l4=Label(window, text="Address")
l4.grid(row=1, column=2)

l5=Label(window, text="Salary")
l5.grid(row=2, column=0)

l6=Label(window, text="Average Rent")
l6.grid(row=2, column=2)

l7=Label(window, text="Distance (MI)")
l7.grid(row=3, column=0)

l8=Label(window, text="Application Status")
l8.grid(row=3, column=2)

#creation of entry buttons
company_text=StringVar()
e1=Entry(window, textvariable=company_text)
e1.grid(row=0, column=1)

title_text=StringVar()
e2=Entry(window, textvariable=title_text)
e2.grid(row=0, column=3)

requirements_text=StringVar()
e3=Entry(window, textvariable=requirements_text)
e3.grid(row=1, column=1)

address_text=StringVar()
e4=Entry(window, textvariable=address_text)
e4.grid(row=1, column=3)

salary_text=StringVar()
e5=Entry(window, textvariable=salary_text)
e5.grid(row=2, column=1)

rent_text=StringVar()
e6=Entry(window, textvariable=rent_text)
e6.grid(row=2, column=3)

distance_text=StringVar()
e7=Entry(window, textvariable=distance_text)
e7.grid(row=3, column=1)

status_text=StringVar()
e8=Entry(window, textvariable=status_text)
e8.grid(row=3, column=3)

#forming the listbox, scrollbar
list1=Listbox(window, height=10, width=50)
list1.grid(row=4, column=0, rowspan=6, columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=6, sticky='e')

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

#adding functionality to the buttons: mapping them to their respective functions
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=4, column=3)

b2=Button(window, text="Search", width=12, command=search_command)
b2.grid(row=5, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=6, column=3)

b4=Button(window, text="Update Entry", width=12, command=update_command)
b4.grid(row=7, column=3)

b5=Button(window, text="Delete Entry", width=12, command=delete_command)
b5.grid(row=8, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=9, column=3)

window.mainloop()
