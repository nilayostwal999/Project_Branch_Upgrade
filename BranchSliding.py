from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from pandas import read_csv
from PIL import ImageTk,Image
from mysql.connector import connect
import webbrowser

root=Tk()

class LoginWindow:
    def __init__(self,master):
        self.master=master
        self.master.title("College Project")
        self.master.geometry("800x670+250+5")
        
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.config(bg="white")

        self.username=StringVar()
        self.password=StringVar()

        self.logoImage=ImageTk.PhotoImage(Image.open("IETDAVVlogo.jpg"))

        self.collegeLabel1=Label(self.frame,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY(I.E.T)",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel1.grid(row=0,column=0,columnspan=2,pady=6)

        self.collegeLabel2=Label(self.frame,text="DAVV,INDORE",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel2.grid(row=1,column=0,columnspan=2)

        self.logoLabel=Label(self.frame,image=self.logoImage,font=("Arial",25,"bold"),relief="flat",bg="white")
        self.logoLabel.grid(row=2,column=0,columnspan=2,pady=10)    

        self.titleLabel=Label(self.frame,text="User Login",font=("Arial",16,"bold"),relief="flat",bg="white",fg="darkblue")
        self.titleLabel.grid(row=3,column=0,columnspan=2,pady=15)

        self.surroundFrame=Frame(self.frame,relief="raised",bd=5,bg="white",width=200)
        self.surroundFrame.grid(row=4,column=0,padx=50)

        self.UserLabel=Label(self.surroundFrame,text="Username  :",font=("Arial",15,"bold"),relief="flat",bg="white",justify="left")
        self.UserLabel.grid(row=1,column=0,padx=30,pady=20)

        self.UserEntry=Entry(self.surroundFrame,font=("Arial",15,"bold"),relief="raised",bd=2,justify="center",bg="white",textvariable=self.username)
        self.UserEntry.grid(row=1,column=1,padx=30,pady=20)
        self.UserEntry.focus()

        self.PasswordLabel=Label(self.surroundFrame,text="Password  :",font=("Arial",15,"bold"),relief="flat",bg="white",justify="left")
        self.PasswordLabel.grid(row=2,column=0,padx=30,pady=20)

        self.PasswordEntry=Entry(self.surroundFrame,font=("Arial",15,"bold"),relief="raised",bd=2,justify="center",show="*",bg="white",textvariable=self.password)
        self.PasswordEntry.grid(row=2,column=1,padx=30,pady=20)

        def userLogin():
            username=self.username.get()
            password=self.password.get()

            if list(username)==list("") or list(password)==list(""):
                tkinter.messagebox.showinfo("Login Window","Field(s) cannot be left blank")

            else:
                if list(username)==list("admin") and list(password)==list("admin123"):
                    self.username.set("")
                    self.password.set("")
                    self.UserEntry.focus()
                    self.newWindow=Toplevel(self.master)
                    self.app=PanelWindow(self.newWindow)
                    self.master.withdraw()

                else:
                    tkinter.messagebox.showinfo("Login Window","Usename or Password is invalid!!\n\nPlease Try Again")
                    self.username.set("")
                    self.password.set("")
                    self.UserEntry.focus()

        self.LoginButton=Button(self.surroundFrame,text="Login",width=13,font=("Arial",12,"bold"),relief="raised",bg="white",fg="darkblue",activebackground="white",activeforeground="darkblue",command=userLogin)
        self.LoginButton.grid(row=3,column=0,columnspan=2,padx=30,pady=20)

class PanelWindow:
    def __init__(self,master):
        self.master=master
        self.master.title("Access Panel")
        self.master.geometry("800x670+250+5")
        
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.config(bg="white")

        self.username=StringVar()
        self.password=StringVar()

        self.logoImage=ImageTk.PhotoImage(Image.open("IETDAVVlogo.jpg"))

        self.collegeLabel1=Label(self.frame,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY(I.E.T)",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel1.grid(row=0,column=0,columnspan=2,pady=6)

        self.collegeLabel2=Label(self.frame,text="DAVV,INDORE",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel2.grid(row=1,column=0,columnspan=2)

        self.logoLabel=Label(self.frame,image=self.logoImage,font=("Arial",25,"bold"),relief="flat",bg="white")
        self.logoLabel.grid(row=2,column=0,columnspan=2,pady=10)    

        self.titleLabel=Label(self.frame,text="Access Panel",font=("Arial",16,"bold"),relief="flat",bg="white")
        self.titleLabel.grid(row=3,column=0,columnspan=2,pady=15)

        self.surroundFrame=Frame(self.frame,relief="raised",bd=5,bg="white",width=200)
        self.surroundFrame.grid(row=4,column=0,padx=50)

        def copySchemePage():
            webbrowser.open("http://localhost:8085/result/script/copy%20scheme's%20subjects.php")

        self.copySchemeButton = Button(self.surroundFrame, text="Copy Scheme's Subjects",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=copySchemePage)
        self.copySchemeButton.grid(row=0,column=0,padx=10,pady=15)

        def schemePage():
            webbrowser.open("http://localhost:8085/result/schemeSubject")

        self.schemeButton = Button(self.surroundFrame, text="Scheme Subject",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=schemePage)
        self.schemeButton.grid(row=0,column=1,padx=10,pady=15)

        def promotionTestPage():
            webbrowser.open("http://localhost:8085/result/promotionTest")

        self.promotionTestButton = Button(self.surroundFrame, text="Promotion Test",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=promotionTestPage)
        self.promotionTestButton.grid(row=0,column=2,padx=10,pady=15)

        def promotionPage():
            webbrowser.open("http://localhost:8085/result/")

        self.promotionButton = Button(self.surroundFrame, text="Promote Student",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=promotionPage)
        self.promotionButton.grid(row=1,column=0,padx=10,pady=15)

        def branchSlide():
             self.newWindow=Toplevel(self.master)
             self.app=BranchSlideWindow(self.newWindow)

        self.branchSlideButton = Button(self.surroundFrame, text="Branch Slide",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=branchSlide)
        self.branchSlideButton.grid(row=1,column=1,padx=10,pady=15)

        def examRegistrationPage():
            webbrowser.open("http://localhost:8085/result/examRegisteration")

        self.examRegistrationButton = Button(self.surroundFrame, text="Exam Registration",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=examRegistrationPage)
        self.examRegistrationButton.grid(row=1,column=2,padx=10,pady=15)

        def summaryUploadPage():
            webbrowser.open("C:\\Users\\Admin\\Desktop\\summary upload.bat")

        self.summaryUploadButton = Button(self.surroundFrame, text="Summary Upload",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=summaryUploadPage)
        self.summaryUploadButton.grid(row=2,column=0,padx=10,pady=15)

        def dataEntryPage():
            webbrowser.open("D:\\Xampp\\htdocs\\summary wise student data entry")

        self.studentEntryButton = Button(self.surroundFrame, text="Student Data Entry",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=dataEntryPage)
        self.studentEntryButton.grid(row=2,column=1,padx=10,pady=15)

        def exImportPage():
            webbrowser.open("http://localhost:8085/result/exImport")

        self.exImportButton = Button(self.surroundFrame, text="Ex Import",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=exImportPage)
        self.exImportButton.grid(row=2,column=2,padx=10,pady=15)

        def gradeCardPage():
            webbrowser.open("http://localhost:8085/result/gradeCard")
            
        self.gradeCardButton = Button(self.surroundFrame, text="Grade Card",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=gradeCardPage)
        self.gradeCardButton.grid(row=3,column=0,padx=10,pady=15)

        def CLCIndexPage():
            webbrowser.open("http://localhost:8085/result/clcIndex")

        self.CLCIndexButton = Button(self.surroundFrame, text="CLC Index",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=CLCIndexPage)
        self.CLCIndexButton.grid(row=3,column=1,padx=10,pady=15)

        def provisionalIndexPage():
            webbrowser.open("http://localhost:8085/result/provisionalIndex")
        
        self.provisionalIndexButton = Button(self.surroundFrame, text="Provisional Index",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=provisionalIndexPage)
        self.provisionalIndexButton.grid(row=3,column=2,padx=10,pady=15)

        def changeSchemeTypePage():
            webbrowser.open("http://localhost:8085/result/changeSchemeType")
        
        self.changeSchemeTypeButton = Button(self.surroundFrame, text="Change Scheme Type",width=20, font=("arial",13,"bold"),relief="raised", bd=2, bg="white", fg="darkblue",activebackground="white",activeforeground="darkblue",command=changeSchemeTypePage)
        self.changeSchemeTypeButton.grid(row=4,column=0,padx=10,pady=15)

class BranchSlideWindow:
    def __init__(self,master):
        self.master=master
        self.master.title("College Project")
        self.master.geometry("800x670+250+5")
        
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.config(bg="white")

        self.batch=StringVar()
        self.session=StringVar()
        self.uploadcsv=StringVar()

        self.logoImage=ImageTk.PhotoImage(Image.open("IETDAVVlogo.jpg"))

        self.collegeLabel1=Label(self.frame,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY(I.E.T)",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel1.grid(row=0,column=0,columnspan=2,pady=6)

        self.collegeLabel2=Label(self.frame,text="DAVV,INDORE",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel2.grid(row=1,column=0,columnspan=2)

        self.logoLabel=Label(self.frame,image=self.logoImage,relief="flat",bg="white")
        self.logoLabel.grid(row=2,column=0,columnspan=2,pady=10)    

        self.titleLabel=Label(self.frame,text="Branch Sliding",font=("Arial",16,"bold"),relief="flat",bg="white",fg="darkblue")
        self.titleLabel.grid(row=3,column=0,columnspan=2,pady=15)

        self.surroundFrame=Frame(self.frame,relief="raised",bd=5,bg="white",width=200)
        self.surroundFrame.grid(row=4,column=0,padx=50)

        self.titleLabel=Label(self.surroundFrame,text="Enter Details",font=("Arial",15,"bold"),relief="flat",bg="white")
        self.titleLabel.grid(row=0,column=0,columnspan=8,pady=10)

        self.sessionLabel=Label(self.surroundFrame,text="Session  :",font=("Arial",15,"bold"),relief="flat",bg="white",justify="left")
        self.sessionLabel.grid(row=1,column=0,padx=30,pady=20)

        def fetchSessionList():
            conn=connect(host="localhost",database="branch_slide",user="root",passwd="")
            curobj=conn.cursor()
            curobj.execute("SELECT name FROM session")
            rows=curobj.fetchall()
            conn.close()
            return rows

        record=fetchSessionList()
        sessionList=[]
        for session in record:
            sessionList.append(session[0])
        
        self.sessionbox=ttk.Combobox(self.surroundFrame,width=11,font=("Arial",12),justify="center",values=sessionList,textvariable=self.session)
        self.sessionbox.grid(row=1,column=1,padx=30,pady=20)

        self.batchLabel=Label(self.surroundFrame,text="Batch  :",font=("Arial",15,"bold"),relief="flat",bg="white")
        self.batchLabel.grid(row=1,column=2,padx=30,pady=20)

        self.batchbox=ttk.Combobox(self.surroundFrame,width=11,font=("Arial",12),justify="center",values=["2014","2015","2016","2017","2018","2019"],textvariable=self.batch)
        self.batchbox.grid(row=1,column=3,padx=30,pady=20)

        def openfile():
             self.filename=filedialog.askopenfilename(initialdir="'/",title="Select File",filetypes=(("CSV files","*.csv"),("all files","*.*")))
             self.uploadcsv.set(self.filename)
             self.uploadEntry.config(state=DISABLED)

        self.uploadButton=Button(self.surroundFrame,text="Upload CSV",font=("Arial",12,"bold"),relief="raised",bg="white",activebackground="white",command=openfile)
        self.uploadButton.grid(row=2,column=0,padx=30,pady=20)

        self.uploadEntry=Entry(self.surroundFrame,font=("Arial",13),relief="raised",bg="white",bd=1,width=49,textvariable=self.uploadcsv)
        self.uploadEntry.grid(row=2,column=1,columnspan=6,padx=20)

        def fetchBranch(enrollmentNumber):
            conn=connect(host='localhost',database='branch_slide',user='root',passwd='')
            curobj=conn.cursor()
            curobj.execute("SELECT branch_code FROM student WHERE enroll_no='%s'"%(enrollmentNumber))
            oldBranch=curobj.fetchall()
            conn.close()
            return oldBranch[0][0]

        def updateData(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection):
            conn=connect(host='localhost',database='branch_slide',user='root',passwd='')
            curobj=conn.cursor()
            query = "update student set branch_code='%s',roll_no_3='%s',roll_no_4='%s',roll_no_5='%s',roll_no_6='%s',roll_no_7='%s',roll_no_8='%s',section_id='%d' WHERE enroll_no='%s'"%(newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection,enrollmentNumber)
            curobj.execute(query)
            conn.commit()
            conn.close()
            return curobj.rowcount

        def slideBranch():
            csvfilepath=self.uploadcsv.get()
            session=self.session.get()
            batch=self.batch.get()

            if len(csvfilepath)==0 or len(session)==0 or len(batch)==0:
                tkinter.messagebox.showinfo("Branch Slide","Field(s) cannot be left blank ")

            else:
                csvdataframe=read_csv(csvfilepath)
                csvdatalist=csvdataframe.values.tolist()
                updatecount=0
                totalcount=len(csvdatalist)
                detailList=[]
                
                #validation
                
                for row in csvdatalist:
                    enrollmentNumber=row[1]
                    newBranch=row[4]
                    newrollNumber=row[5]
                    newBranchcode=newrollNumber[:3]
                    newLastrollnumber=newrollNumber[4:]
                    newRoll3=newrollNumber
                    newRoll4=newBranchcode+"4"+newLastrollnumber;
                    newRoll5=newBranchcode+"5"+newLastrollnumber;
                    newRoll6=newBranchcode+"6"+newLastrollnumber;
                    newRoll7=newBranchcode+"7"+newLastrollnumber;
                    newRoll8=newBranchcode+"8"+newLastrollnumber;
                    newsection=row[6]

                    #Fetching the old Branch
                    oldBranch=fetchBranch(enrollmentNumber)

                    #Branch Sliding
                    rowsaffected=updateData(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection)
                    updatecount+=rowsaffected

                    #Fetching the New Branch
                    newBranch=fetchBranch(enrollmentNumber)

                    detailList.append([enrollmentNumber,oldBranch,newBranch])

                proceed=tkinter.messagebox.askyesno("Branch Slide","  Branch Slide Successful.\n  Total Number Of Records        : "+str(totalcount)+"\n  Number Of Records Updated  : "+str(updatecount)+"\n\n  Do you want to view the branch update details ? ")
                if proceed>0:
                    self.newWindow=Toplevel(self.master)
                    self.app=UpdateDetailsWindow(self.newWindow,detailList)
                    self.master.withdraw()

        self.changeButton=Button(self.surroundFrame,text="Slide Branch",font=("Arial",12,"bold"),relief="raised",bg="white",activebackground="white",command=slideBranch)
        self.changeButton.grid(row=3,column=0,columnspan=6,padx=30,pady=20)

class UpdateDetailsWindow:
    def __init__(self,master,detailList):
        self.master=master
        self.detailList=detailList
        self.master.title("College Project")
        self.master.geometry("800x670+250+5")
        
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.config(bg="white")

        self.logoImage=ImageTk.PhotoImage(Image.open("IETDAVVlogo.jpg"))

        self.collegeLabel1=Label(self.frame,text="INSTITUTE OF ENGINEERING AND TECHNOLOGY(I.E.T)",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel1.grid(row=0,column=0,columnspan=2,pady=6)

        self.collegeLabel2=Label(self.frame,text="DAVV,INDORE",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.collegeLabel2.grid(row=1,column=0,columnspan=2)

        self.logoLabel=Label(self.frame,image=self.logoImage,relief="flat",bg="white")
        self.logoLabel.grid(row=2,column=0,columnspan=2,pady=10)

        self.titleLabel=Label(self.frame,text="Branch Update Details",font=("Arial",15,"bold"),relief="flat",bd=2,bg="white",fg="green")
        self.titleLabel.grid(row=3,column=0,columnspan=2,pady=10)

        self.surroundFrame=Frame(self.frame,relief="ridge",bd=2,bg="white",width=300)
        self.surroundFrame.grid(row=4,column=0,columnspan=2,padx=20,pady=5)

        columnList=["Enrollment Number","Old Branch","New Branch"]

        self.style=ttk.Style()
        self.style.configure("mystyle.Treeview",font=("Arial",10,"bold"))
        self.style.configure("mystyle.Treeview.Heading",font=("Arial",13,"bold"),foreground="blue")
        self.style.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':'nswe'})])

        self.scrollbar=Scrollbar(self.surroundFrame)
        self.scrollbar.pack(side=RIGHT)
        
        self.TreeView=ttk.Treeview(self.surroundFrame,show="headings",column=columnList,height=10,style="mystyle.Treeview",yscrollcommand=self.scrollbar.set)
        self.TreeView.pack(side=LEFT,pady=5)
        self.scrollbar.config(command=self.TreeView.yview)

        for i in range(0,1):
            column=columnList[i]
            self.TreeView.heading(column,text=column.title())
            self.TreeView.column(column,width=170,anchor="center")  

        for i in range(1,len(columnList)):
            column=columnList[i]
            self.TreeView.heading(column,text=column.title())
            self.TreeView.column(column,width=140,anchor="center")

        for i in range(0,len(detailList),2):
            row=detailList[i]
            self.TreeView.insert("",END,values=row)
            self.TreeView.insert("",END,values=" ")

        for i in range(1,len(detailList),2):
            row=detailList[i]
            self.TreeView.insert("",END,values=row)
            self.TreeView.insert("",END,values=" ")
    
app=LoginWindow(root)    
root.mainloop()
