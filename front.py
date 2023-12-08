import back
import backend
from tkinter import *

def Doctors():
    def get_selected_row_D(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e31.delete(0, END)
        e31.insert(END, selected_tuple[3])
        e32.delete(0, END)
        e32.insert(END, selected_tuple[4])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[5])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[6])

    def add_command():
        back.addD(e1.get(), e2.get(), e31.get(), e32.get(), e4.get(), e5.get(),e6.get())
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e31.get(), e32.get(), e4.get(), e5.get()))

    def delete_command():
        back.delD(e6.get())

    def view_command():
        t.delete(0, END)
        t.insert(END, "ID    Name       Department OPD time from  to  Room no. Phone no.")
        for row in back.selD(-1):
            t.insert(END, row)

    r1 = Tk()
    fd = Frame(r1, width=w, height=h, bg="#FEB29F")
    fd.propagate(0)
    fd.pack()

    e1 = StringVar()
    b = StringVar()
    c1 = IntVar()
    c2 = IntVar()
    d = IntVar()
    e = IntVar()
    x = StringVar()

    l1 = Label(fd, text="ID            :")
    l2 = Label(fd, text="Name          :")
    l3 = Label(fd, text="Department      :")
    l31 = Label(fd, text="OPD Timing from :")
    l32 = Label(fd, text="to")
    l4 = Label(fd, text="Room no.        :")
    l5 = Label(fd, text="Phone no.       :")

    e1 = Entry(fd, width=100, textvariable=e1)
    e2 = Entry(fd, width=100, textvariable=b)
    e3 = Entry(fd, width=100, textvariable=c1)
    e31 = Entry(fd, width=30, textvariable=c2)
    e32 = Entry(fd, width=30)
    e4 = Entry(fd, width=100, textvariable=d)
    e5 = Entry(fd, width=100, textvariable=e)

    l1.place(x=100, y=70)
    l2.place(x=100, y=100)
    l3.place(x=100, y=130)
    l31.place(x=100, y=160)
    l32.place(x=480, y=160)
    l4.place(x=100, y=190)
    l5.place(x=100, y=220)

    e1.place(x=250, y=70)
    e2.place(x=250, y=100)
    e3.place(x=250, y=130)
    e31.place(x=250, y=160)
    e32.place(x=530, y=160)
    e4.place(x=250, y=190)
    e5.place(x=250, y=220)

    B1 = Button(fd, text="Add Entry", command=add_command, relief=RAISED)
    e6 = Entry(fd, width=50, textvariable=x)
    B2 = Button(fd, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fd, text="View all", command=view_command, relief=RAISED)
    B1.place(x=200, y=250)
    e6.place(x=300, y=280)
    B2.place(x=200, y=280)
    B3.place(x=200, y=310)

    t = Listbox(fd, height=100, width=100)
    t.place(x=200, y=350)

    t.bind('<<ListboxSelect>>', get_selected_row_D)

def Appointments():
    def get_selected_row_A(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[5])

    def add_command():
        backend.addA(e1.get(), e2.get(), e3.get(), e4.get())
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e3.get(), e4.get()))

    def delete_command():
        backend.delA(e5.get())

    def view_command():
        t.delete(0, END)
        t.insert(END, "ID    Name                Doctor           Timing    Phone no.")
        for row in backend.selA(-1):
            t.insert(END, row)

    r2 = Tk()
    fa = Frame(r2, width=w, height=h, bg="#B4F4FE")
    fa.propagate(0)
    fa.pack()

    a = StringVar()
    b = StringVar()
    c = IntVar()
    d = IntVar()

    x = StringVar()
    l1 = Label(fa, text="ID             :")
    l2 = Label(fa, text="Patient Name   :")
    l3 = Label(fa, text="Doctor         :")
    l4 = Label(fa, text="Timing         :")
    l5 = Label(fa, text="Phone no.      :")

    e1 = Entry(fa, width=100, textvariable=a)
    e2 = Entry(fa, width=100, textvariable=b)
    e3 = Entry(fa, width=100, textvariable=c)
    e4 = Entry(fa, width=100, textvariable=d)

    l1.place(x=100, y=70)
    l2.place(x=100, y=100)
    l3.place(x=100, y=130)
    l4.place(x=100, y=160)
    l5.place(x=100, y=190)

    e1.place(x=250, y=70)
    e2.place(x=250, y=100)
    e3.place(x=250, y=130)
    e4.place(x=250, y=160)

    B1 = Button(fa, text="Add Entry", command=add_command, relief=RAISED)
    e5 = Entry(fa, width=50, textvariable=x)
    B2 = Button(fa, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fa, text="View all", command=view_command, relief=RAISED)

    t = Listbox(fa, height=100, width=100)

    B1.place(x=200, y=220)
    e5.place(x=300, y=250)
    B2.place(x=200, y=250)
    B3.place(x=200, y=280)

    t.place(x=200, y=320)
    t.bind('<<ListboxSelect>>', get_selected_row_A)


# def Patients():
#     def get_selected_row_P(event):
#         global selected_tuple
#         index = int(t.curselection()[0])
#         selected_tuple = t.get(index)
#         e1.delete(0, END)
#         e1.insert(END, selected_tuple[1])
#         e2.delete(0, END)
#         e2.insert(END, selected_tuple[2])
#         e3.delete(0, END)
#         e3.insert(END, selected_tuple[3])
#         e4.delete(0, END)
#         e4.insert(END, selected_tuple[3])

#     def add_command():
#         backend.addP(e1.get(), e2.get(), e3.get(),e4.get())
#         t.delete(0, END)
#         t.insert(END, (e1.get(), e2.get(), e3.get()))

#     def delete_command():
#         backend.delP(e4.get())

#     def view_command():
#         t.delete(0, END)
#         t.insert(END, "ID    Name            Phone no.       I/O")
#         for row in backend.selP(-1):
#             t.insert(END, row)

#     r3 = Tk()
#     fp = Frame(r3, width=w, height=h, bg="#C3FF68")
#     fp.propagate(0)
#     fp.pack()

#     a = StringVar()
#     b = IntVar()
#     c = StringVar()

#     x = StringVar()
#     l1 = Label(fp, text="ID            :")
#     l2 = Label(fp, text="Name          :")
#     l3 = Label(fp, text="Phone no.     :")
#     l4 = Label(fp, text="I/O           :")

#     e1 = Entry(fp, width=100, textvariable=a)
#     e2 = Entry(fp, width=100, textvariable=b)
#     e3 = Entry(fp, width=100, textvariable=c)
#     e4 = Entry(fp, width=100, textvariable=d)


#     l1.place(x=100, y=70)
#     l2.place(x=100, y=100)
#     l3.place(x=100, y=130)
#     l4.place(x=100, y=160)

#     e1.place(x=250, y=70)
#     e2.place(x=250, y=100)
#     e3.place(x=250, y=130)
#     e4.place(x=250, y=160)

#     B1 = Button(fp, text="Add Entry", command=add_command, relief=RAISED)
#     e4 = Entry(fp, width=50, textvariable=x)
#     B2 = Button(fp, text="Delete Entry", command=delete_command, relief=RAISED)
#     B3 = Button(fp, text="View all", command=view_command, relief=RAISED)

#     t = Listbox(fp, height=100, width=100)

#     B1.place(x=200, y=190)
#     e4.place(x=300, y=220)
#     B2.place(x=200, y=220)
#     B3.place(x=200, y=250)

#     t.place(x=200, y=290)
#     t.bind('<<ListboxSelect>>', get_selected_row_P)

def Patients():
    def get_selected_row_P(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[0])  # Corrected index
        e2.delete(0, END)
        e2.insert(END, selected_tuple[1])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[3])

    def add_command():
        backend.addP(e1.get(), e2.get(), e3.get(), e4.get())
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e3.get(), e4.get()))

    def delete_command():
        backend.delP(e1.get())  # Assuming ID is used for deletion

    def view_command():
        t.delete(0, END)
        t.insert(END, "ID    Name            Phone no.       I/O")
        for row in backend.selP(-1):
            t.insert(END, row)

    r3 = Tk()
    fp = Frame(r3, width=w, height=h, bg="#C3FF68")
    fp.propagate(0)
    fp.pack()

    a = StringVar()
    b = StringVar()
    c = StringVar()
    d = StringVar()  # Added this variable

    x = StringVar()
    l1 = Label(fp, text="ID            :")
    l2 = Label(fp, text="Name          :")
    l3 = Label(fp, text="Phone no.     :")
    l4 = Label(fp, text="I/O           :")

    e1 = Entry(fp, width=100, textvariable=a)
    e2 = Entry(fp, width=100, textvariable=b)
    e3 = Entry(fp, width=100, textvariable=c)
    e4 = Entry(fp, width=100, textvariable=d)

    l1.place(x=100, y=70)
    l2.place(x=100, y=100)
    l3.place(x=100, y=130)
    l4.place(x=100, y=160)

    e1.place(x=250, y=70)
    e2.place(x=250, y=100)
    e3.place(x=250, y=130)
    e4.place(x=250, y=160)

    B1 = Button(fp, text="Add Entry", command=add_command, relief=RAISED)
    B2 = Button(fp, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fp, text="View all", command=view_command, relief=RAISED)

    t = Listbox(fp, height=100, width=100)

    B1.place(x=200, y=190)
    B2.place(x=200, y=220)
    B3.place(x=200, y=250)

    t.place(x=200, y=290)
    t.bind('<<ListboxSelect>>', get_selected_row_P)
def Medicine():
    def get_selected_row_M(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])

    def add_command():
        backend.addM(e1.get(), e2.get(), e3.get())
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e3.get()))

    def delete_command():
        backend.delM(e4.get())

    def view_command():
        t.delete(0, END)
        t.insert(END, "M_ID   Medicine Name   Quantity   Price")
        for row in backend.selM(-1):
            t.insert(END, row)

    r4 = Tk()
    fm = Frame(r4, width=w, height=h, bg="#FFDCB2")
    fm.propagate(0)
    fm.pack()

    a = IntVar()
    b = StringVar()
    c = IntVar()

    x = StringVar()
    l1 = Label(fm, text="M_ID          :")
    l2 = Label(fm, text="Medicine Name :")
    l3 = Label(fm, text="Quantity      :")
    l4 = Label(fm, text="Price         :")

    e1 = Entry(fm, width=100, textvariable=a)
    e2 = Entry(fm, width=100, textvariable=b)
    e3 = Entry(fm, width=100, textvariable=c)

    l1.place(x=100, y=70)
    l2.place(x=100, y=100)
    l3.place(x=100, y=130)
    l4.place(x=100, y=160)

    e1.place(x=250, y=70)
    e2.place(x=250, y=100)
    e3.place(x=250, y=130)

    B1 = Button(fm, text="Add Entry", command=add_command, relief=RAISED)
    e4 = Entry(fm, width=50, textvariable=x)
    B2 = Button(fm, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fm, text="View all", command=view_command, relief=RAISED)

    t = Listbox(fm, height=100, width=100)

    B1.place(x=200, y=190)
    e4.place(x=300, y=220)
    B2.place(x=200, y=220)
    B3.place(x=200, y=250)

    t.place(x=200, y=290)
    t.bind('<<ListboxSelect>>', get_selected_row_M)

def Pharmacy():
    def get_selected_row_Pha(event):
        global selected_tuple
        index = int(t.curselection()[0])
        selected_tuple = t.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[0])  # Corrected index
        e2.delete(0, END)
        e2.insert(END, selected_tuple[1])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[3])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[4])  # Corrected index

    def add_command():
        backend.addPh(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())  # Corrected function name
        t.delete(0, END)
        t.insert(END, (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))

    def delete_command():
        backend.delPh(e4.get())  # Corrected function name

    def view_command():
        t.delete(0, END)
        t.insert(END, "P_ID   MED1   MED2   MED3   MED4")
        for row in backend.selPh(-1):  # Corrected function name
            t.insert(END, row)

    r5 = Tk()
    fpha = Frame(r5, width=w, height=h, bg="#FFD700")
    fpha.propagate(0)
    fpha.pack()

    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()

    x = StringVar()
    l1 = Label(fpha, text="P_ID  :")
    l2 = Label(fpha, text="MED1  :")
    l3 = Label(fpha, text="MED2  :")
    l4 = Label(fpha, text="MED3  :")
    l5 = Label(fpha, text="MED4  :")

    e1 = Entry(fpha, width=100, textvariable=a)
    e2 = Entry(fpha, width=100, textvariable=b)
    e3 = Entry(fpha, width=100, textvariable=c)
    e4 = Entry(fpha, width=100, textvariable=d)
    e5 = Entry(fpha, width=100, textvariable=x)  # Corrected variable

    l1.place(x=100, y=70)
    l2.place(x=100, y=100)
    l3.place(x=100, y=130)
    l4.place(x=100, y=160)
    l5.place(x=100, y=190)

    e1.place(x=250, y=70)
    e2.place(x=250, y=100)
    e3.place(x=250, y=130)
    e4.place(x=250, y=160)
    e5.place(x=250, y=190)

    B1 = Button(fpha, text="Add Entry", command=add_command, relief=RAISED)
    e6 = Entry(fpha, width=50, textvariable=x)
    B2 = Button(fpha, text="Delete Entry", command=delete_command, relief=RAISED)
    B3 = Button(fpha, text="View all", command=view_command, relief=RAISED)

    t = Listbox(fpha, height=100, width=100)

    B1.place(x=200, y=220)
    e6.place(x=300, y=250)
    B2.place(x=200, y=250)
    B3.place(x=200, y=280)

    t.place(x=200, y=320)
    t.bind('<<ListboxSelect>>', get_selected_row_Pha)

# def Pharmacy():
#     def get_selected_row_Pha(event):
#         global selected_tuple
#         index = int(t.curselection()[0])
#         selected_tuple = t.get(index)
#         e1.delete(0, END)
#         e1.insert(END, selected_tuple[1])
#         e2.delete(0, END)
#         e2.insert(END, selected_tuple[2])
#         e3.delete(0, END)
#         e3.insert(END, selected_tuple[3])
#         e4.delete(0, END)
#         e4.insert(END, selected_tuple[3])
#         e5.delete(0, END)
#         e5.insert(END, selected_tuple[3])


#     def add_command():
#         backend.addPh(e1.get(), e2.get(), e3.get(),e4.get(),e5.get())
#         t.delete(0, END)
#         t.insert(END, (e1.get(), e2.get(), e3.get()))

#     def delete_command():
#         backend.delPha(e4.get())

#     def view_command():
#         t.delete(0, END)
#         t.insert(END, "P_ID   MED1   MED2   MED3   MED4")
#         for row in backend.selPh(-1):
#             t.insert(END, row)

#     r5 = Tk()
#     fpha = Frame(r5, width=w, height=h, bg="#FFD700")
#     fpha.propagate(0)
#     fpha.pack()

#     a = IntVar()
#     b = IntVar()
#     c = IntVar()
#     d = IntVar()

#     x = StringVar()
#     l1 = Label(fpha, text="P_ID  :")
#     l2 = Label(fpha, text="MED1  :")
#     l3 = Label(fpha, text="MED2  :")
#     l4 = Label(fpha, text="MED3  :")
#     l5 = Label(fpha, text="MED4  :")

#     e1 = Entry(fpha, width=100, textvariable=a)
#     e2 = Entry(fpha, width=100, textvariable=b)
#     e3 = Entry(fpha, width=100, textvariable=c)
#     e4 = Entry(fpha, width=100, textvariable=d)
#     e = Entry(fpha, width=100, textvariable=e)

#     l1.place(x=100, y=70)
#     l2.place(x=100, y=100)
#     l3.place(x=100, y=130)
#     l4.place(x=100, y=160)
#     l5.place(x=100, y=190)

#     e1.place(x=250, y=70)
#     e2.place(x=250, y=100)
#     e3.place(x=250, y=130)
#     e4.place(x=250, y=160)

#     B1 = Button(fpha, text="Add Entry", command=add_command, relief=RAISED)
#     e5 = Entry(fpha, width=50, textvariable=x)
#     B2 = Button(fpha, text="Delete Entry", command=delete_command, relief=RAISED)
#     B3 = Button(fpha, text="View all", command=view_command, relief=RAISED)

#     t = Listbox(fpha, height=100, width=100)

#     B1.place(x=200, y=220)
#     e5.place(x=300, y=250)
#     B2.place(x=200, y=250)
#     B3.place(x=200, y=280)

#     t.place(x=200, y=320)
#     t.bind('<<ListboxSelect>>', get_selected_row_Pha)


w, h = 800, 500
r = Tk(screenName="Hospital Management")
r.geometry("%dx%d+0+0" % (w, h))
f = Frame(r, width=w, height=h, bg="#181589")  # Dark blue
f.propagate(0)
f.pack()

B1 = Button(f, text="Doctors", command=Doctors, relief=RAISED)
B2 = Button(f, text="Appointments", command=Appointments, relief=RAISED)
B3 = Button(f, text="Patients", command=Patients, relief=RAISED)
B4 = Button(f, text="Medicine", command=Medicine, relief=RAISED)
B5 = Button(f, text="Pharmacy", command=Pharmacy, relief=RAISED)

B1.place(x=100, y=50)
B2.place(x=250, y=50)
B3.place(x=400, y=50)
B4.place(x=550, y=50)
B5.place(x=700, y=50)

r.mainloop()
