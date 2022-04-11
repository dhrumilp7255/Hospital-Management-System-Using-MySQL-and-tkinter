from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector as sql

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref =StringVar()
        self.Dose = StringVar()
        self.Numberoftablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.Dailydose = StringVar()
        self.Sideeffect = StringVar()
        self.Furtherinfo = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedicine = StringVar()
        self.PatientID = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DOB = StringVar()
        self.PatientAddr = StringVar()

        lbltitle = Label(self.root,bd=20,relief = RIDGE ,text="HOSPITAL MANAGEMENT SYSTEM",fg="dark blue",bg="grey",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #---------------DATAFRAME----------------
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        #left dataframe
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("arial",12,"bold"),text="Patient Information",fg="purple")
        DataframeLeft.place(x=8,y=5,width=1000,height=350)
        #right dataframe
        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("arial",12,"bold"),text="Prescription",fg="purple")
        DataframeRight.place(x=1015,y=5,width=480,height=350)

        #--------------BUTTONS FRAME---------------
        Buttonframe = Frame(self.root, bd=15, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # --------------DETAILS FRAME---------------
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        #--------------LABELS-----------------------
        lblNameTablet=Label(DataframeLeft,text="Names of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        #------------COMBOBOX for name of tablets------------------------
        comNametablet=ttk.Combobox(DataframeLeft,state="readonly",font=("arial",12,"bold"),textvariable=self.Nameoftablets,width=33)

        comNametablet["values"]=("Crocin","Azithromicin","Vicks action","Dolo","Dexon")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        # ------------Labels---------------------------
        lblref = Label(DataframeLeft, text="Reference No:", font=("arial", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial", 12, "bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft, text="Dose:", font=("arial", 12, "bold"), padx=2,pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, text="No of Tablets:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Numberoftablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, text="Lot:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, text="Expiry Date:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Expdate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2,pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Dailydose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblsideEffect = Label(DataframeLeft, text="Side Effect:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Sideeffect, width=35)
        txtsideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, text="Further Information:", font=("arial", 12, "bold"), padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Furtherinfo, width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, text="Blood Pressure:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DrivingUsingMachine, width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblstorage = Label(DataframeLeft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblstorage.grid(row=2, column=2, sticky=W)
        txtstorage = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.StorageAdvice, width=35)
        txtstorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, text="Medication:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.HowToUseMedicine, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, text="Patient ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientID, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, text="NHS Number:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, text="Patient Name:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateofBirth = Label(DataframeLeft, text="D.O.B:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblDateofBirth.grid(row=7, column=2, sticky=W)
        txtDateofBirth = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DOB, width=35)
        txtDateofBirth.grid(row=7, column=3)

        lblPatientAdd = Label(DataframeLeft, text="Patient Address:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientAdd.grid(row=8, column=2, sticky=W)
        txtPatientAdd = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientAddr, width=35)
        txtPatientAdd.grid(row=8, column=3)

        #------------prescription textbox---------------------
        self.txtPrescription=Text(DataframeRight,font=("arial", 12, "bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #---------------Buttons------------------------------
        btnPrescription=Button(Buttonframe,text="Prescription",command=self.Prescription,fg="dark blue",bg="grey",font=("arial",8,"bold"),width=34,height=2,padx=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data",command=self.iPrescriptionData, fg="dark blue", bg="grey", font=("arial", 8, "bold"),
                                 width=34, height=2, padx=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update",command=self.update, fg="dark blue", bg="grey", font=("arial", 8, "bold"),
                                 width=34, height=2, padx=2)
        btnUpdate.grid(row=0, column=2)

        btnClear = Button(Buttonframe, text="Delete",command=self.delete, fg="dark blue", bg="grey", font=("arial", 8, "bold"),
                           width=34, height=2, padx=2)
        btnClear.grid(row=0, column=3)

        btnExit = Button(Buttonframe, text="Clear",command=self.clear, fg="dark blue", bg="grey", font=("arial", 8, "bold"),
                          width=34, height=2, padx=2)
        btnExit.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit",command=self.exit, fg="dark blue", bg="grey", font=("arial", 8, "bold"),
                         width=34, height=2, padx=2)
        btnExit.grid(row=0, column=5)

        #----------------------Table-------------------------------

        #----------------------Scrollbar---------------------------

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot"
                                                              ,"issuedate","expdate","dailydose"
                                                              ,"storage","nhsnumber","pname","dob",
                                                              "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)


        #-------------------------Functionality----------------------------------
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "" :
            messagebox.showerror("Error","All fields are required")

        else:
            conn = sql.connect(host="localhost",username="root",password="#YOUR PASSWORD",database="hospitaldata")
            my_cursor=conn.cursor()
            my_cursor.execute("INSERT INTO hosital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.Numberoftablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.Expdate.get(),
                self.Dailydose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DOB.get(),
                self.PatientAddr.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        conn = sql.connect(host="localhost", username="root", password="#YOUR PASSWORD", database="hospitaldata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hosital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def update(self):
        conn = sql.connect(host="localhost", username="root", password="#YOUR PASSWORD", database="hospitaldata")
        my_cursor = conn.cursor()
        my_cursor.execute("update hosital set Name_of_tablets=%s,dose= %s,Numberoftablets= %s,lot= %s,issuedate=%s,expdate=%s,dailydose=%s,storage= %s,nhsnumber=%s,patientname= %s,DOB= %s,patientaddress=%s where Reference_no= %s",(
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.Numberoftablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.Expdate.get(),
                self.Dailydose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DOB.get(),
                self.PatientAddr.get(),
                self.ref.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been Updated")

    def get_cursor(self,event):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0]),
        self.ref.set(row[1]),
        self.Dose.set(row[2]),
        self.Numberoftablets.set(row[3]),
        self.Lot.set(row[4]),
        self.Issuedate.set(row[5]),
        self.Expdate.set(row[6]),
        self.Dailydose.set(row[7]),
        self.StorageAdvice.set(row[8]),
        self.nhsNumber.set(row[9]),
        self.PatientName.set(row[10]),
        self.DOB.set(row[11]),
        self.PatientAddr.set(row[12]),


    def Prescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.Numberoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get() +"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get() +"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get() +"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.Dailydose.get() +"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.Sideeffect.get() +"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.Furtherinfo.get() +"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get() +"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.DrivingUsingMachine.get() +"\n")
        self.txtPrescription.insert(END,"Patient ID"+self.PatientID.get() +"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.nhsNumber.get() +"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get() +"\n")
        self.txtPrescription.insert(END,"DOB:\t\t\t"+self.DOB.get() +"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddr.get() +"\n")

    def delete(self):
        conn = sql.connect(host="localhost", username="root", password="#YOUR PASSWORD", database="hospitaldata")
        my_cursor = conn.cursor()
        query="delete from hosital where Reference_no= %s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Deleted","Patient Information is deleted Successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.Dailydose.set("")
        self.Sideeffect.set("")
        self.Furtherinfo.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedicine.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.PatientAddr.set("")

    def exit(self):
        Exit=messagebox.askyesno("Hospital Management System","Do you want to exit?")
        if Exit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()