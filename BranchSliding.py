from tkinter import *
import tkinter.messagebox
from tkinter import ttk;
from tkinter import filedialog
import pandas as pd
import Database

def main():
    root=Tk()
    app=Window1(root)
    
class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("College Project")
        self.master.geometry("800x630+250+20")
        
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        self.frame.config(bg="white")

        self.batch=StringVar()
        self.session=StringVar()
        self.uploadcsv=StringVar()

        self.titleLabel=Label(self.frame,text="Branch Sliding",font=("Arial",25,"bold"),relief="flat",bg="white")
        self.titleLabel.grid(row=0,column=0,columnspan=2,pady=30)

        self.menubar=Menu(self.master)
        self.master.config(menu=self.menubar)

        self.filemenu=Menu(self.menubar)
        self.menubar.add_cascade(label="      Home     ",menu=self.filemenu)
        
        self.insertmenu=Menu(self.filemenu)
        self.filemenu.add_cascade(label="Insert Record      ",menu=self.insertmenu)
        self.insertmenu.add_command(label=" Student Table    ")
        
        self.openmenu=Menu(self.filemenu)
        self.filemenu.add_cascade(label="View Record    ",menu=self.openmenu)
        self.openmenu.add_command(label=" Student Table    ")
        
        self.updatemenu=Menu(self.filemenu)
        self.filemenu.add_cascade(label="Update Record      ",menu=self.updatemenu)
        self.updatemenu.add_command(label=" Student Table    ")
        
        self.deletemenu=Menu(self.filemenu)
        self.filemenu.add_cascade(label="Delete Record    ",menu=self.deletemenu)
        self.deletemenu.add_command(label="  Student Table    ")
        
        self.filemenu.add_command(label="Close  ")
        self.filemenu.add_command(label="Exit     ")

        self.surroundFrame=Frame(self.frame,relief="raised",bd=5,bg="white",width=200)
        self.surroundFrame.grid(row=1,column=0,padx=50,pady=60)

        self.titleLabel=Label(self.surroundFrame,text="Enter Details",font=("Arial",18,"bold"),relief="flat",bg="white")
        self.titleLabel.grid(row=0,column=0,columnspan=8)

        self.sessionLabel=Label(self.surroundFrame,text="Session  :",font=("Arial",15,"bold"),relief="flat",bg="white",justify="left")
        self.sessionLabel.grid(row=1,column=0,padx=30,pady=20)

        self.sessionbox=ttk.Combobox(self.surroundFrame,width=11,font=("Arial",12),justify="center",values=["2014-2015","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022"],textvariable=self.session)
        self.sessionbox.grid(row=1,column=1,padx=30,pady=20)

        self.batchLabel=Label(self.surroundFrame,text="Batch  :",font=("Arial",15,"bold"),relief="flat",bg="white")
        self.batchLabel.grid(row=1,column=2,padx=30,pady=20)

        self.batchbox=ttk.Combobox(self.surroundFrame,width=11,font=("Arial",12),justify="center",values=["2014-2015","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022"],textvariable=self.batch)
        self.batchbox.grid(row=1,column=3,padx=30,pady=20)

        def openfile():
             self.filename=filedialog.askopenfilename(initialdir="'/",title="Select File",filetypes=(("CSV files","*.csv"),("all files","*.*")))
             self.uploadcsv.set(self.filename)
             self.uploadEntry.config(state=DISABLED)

        self.uploadButton=Button(self.surroundFrame,text="Upload CSV",font=("Arial",12,"bold"),relief="raised",bg="white",activebackground="white",command=openfile)
        self.uploadButton.grid(row=2,column=0,padx=30,pady=20)

        self.uploadEntry=Entry(self.surroundFrame,font=("Arial",13),relief="raised",bg="white",bd=1,width=49,textvariable=self.uploadcsv)
        self.uploadEntry.grid(row=2,column=1,columnspan=6,padx=20)

        def slideBranch():
            csvfilepath=self.uploadcsv.get()
            csvdataframe=pd.read_csv(csvfilepath)
            csvdatalist=csvdataframe.values.tolist()
            #validation
            #print(csvdatalist)
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
                """print(newRoll3)
                print(newRoll4)
                print(newRoll5)
                print(newRoll6)
                print(newRoll7)
                print(newRoll8)
                print(" ")"""
                #Database.updateRecord(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection)
                Database.updateData(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection)

        self.changeButton=Button(self.surroundFrame,text="Slide Branch",font=("Arial",12,"bold"),relief="raised",bg="white",activebackground="white",command=slideBranch)
        self.changeButton.grid(row=3,column=0,columnspan=6,padx=30,pady=20)
        
if __name__=="__main__":
    main()
