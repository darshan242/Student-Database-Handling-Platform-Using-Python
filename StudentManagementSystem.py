def ConnectDB():

    def SubmitDB():
        global var,cursor
        Enteredhost=hostval.get()
        Entereduser=userval.get()
        Enteredpassword=passwval.get()

        try:
            var=pymysql.connect(host=Enteredhost,user=Entereduser,password=Enteredpassword)
            cursor=var.cursor()
        except:
            messagebox.showerror('Notification','Data is Incorrect')
            return
        
        try:
            createdb='create database Student_Database_Management_System1'
            cursor.execute(createdb)
            usedb='use Student_Database_Management_System1'
            cursor.execute(usedb)
            createtable='create table Student(ID int ,stud_name varchar(50),mobile_no varchar(50) ,email varchar(50),city varchar(50),DateOfBirth varchar(50),PRIMARY KEY(ID))'
            cursor.execute(createtable)
            messagebox.showinfo('Notification','Database Created And Now You Are Connected....',parent=dbroot)
        except:
             usedb='use Student_Database_Management_System1'
             cursor.execute(usedb)
             messagebox.showinfo('Notification','You Are Connected To Database....',parent=dbroot)
        dbroot.destroy()
            

        

        
    dbroot=tkinter.Toplevel()#to create frame within a active frame
    dbroot.title('Connect To Database')
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.config(background='LemonChiffon2')
    dbroot.iconbitmap('student3_118006.ico')
    #dbroot.resizable(False,False)

    ##################################### Lables In dbrootr frame

    hostlable=tkinter.Label(dbroot,text='Enter Host : ',font=('Tahoma',15),background='LemonChiffon2')
    hostlable.place(x=10,y=10)
    
    hostval=tkinter.StringVar()#To accept the entry value into user variable
    hostentry=tkinter.Entry(dbroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='LemonChiffon3',textvariable=hostval)
    hostentry.place(x=180,y=10)
    

    userlable=tkinter.Label(dbroot,text='Enter User : ',font=('Tahoma',15),background='LemonChiffon2')
    userlable.place(x=10,y=70)
    
    userval=tkinter.StringVar()
    userentry=tkinter.Entry(dbroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='LemonChiffon3',textvariable=userval)
    userentry.place(x=180,y=70)

    passwlable=tkinter.Label(dbroot,text='Enter Password : ',font=('Tahoma',15),background='LemonChiffon2')
    passwlable.place(x=10,y=130)
    
    passwval=tkinter.StringVar()
    passwentry=tkinter.Entry(dbroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='LemonChiffon3',textvariable=passwval)
    passwentry.place(x=180,y=130)

    submitbtn=tkinter.Button(dbroot,text='Submit',font=('Tahoma',15,'bold'),background='LemonChiffon2',activebackground='LemonChiffon3',command=SubmitDB)
    submitbtn.place(x=205,y=185)


    dbroot.mainloop()

def CurrentTime():
    time_str=time.strftime("%H:%M:%S")
    date_str=time.strftime("%d/%m/%Y")
    clock.config(text='Date : '+date_str+'\n'+'Time : '+time_str)
    clock.after(20,CurrentTime)######-------------->To execute current time which is a function for clock frame after every 20s

def EntryField1():
    def AddStud():
        stud_ID=EFIDval.get()
        stud_name=EFNameval.get()
        mob=EFMobval.get()
        stud_mail=EFEmailval.get()
        stud_city=EFCityval.get()
        stud_dob=EFDOBval.get()
        try:
            Entry='insert into Student values (%s,%s,%s,%s,%s,%s)'
            cursor.execute(Entry,(stud_ID,stud_name,mob,stud_mail,stud_city,stud_dob))
            var.commit()
            response=messagebox.askyesnocancel('Notification','Student Of ID {} Added Successfully...Do Yo Want To Clear Form?.'.format(stud_ID),parent=EFroot)
            if(response==True):
                EFIDval.set(' ')
                EFNameval.set(' ')
                EFMobval.set(' ')
                EFEmailval.set(' ')
                EFCityval.set(' ')
                EFDOBval.set(' ')
        except:
            messagebox.showerror('Notification','Id Already Exists!!!')
        strr='select * from Student'
        cursor.execute(strr)
        output_data=cursor.fetchall()
        ResultTable.delete(*ResultTable.get_children())
        for i in output_data:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5]]
            ResultTable.insert('','end',values=vv)
    


    EFroot=tkinter.Toplevel()#to create frame within a active frame
    EFroot.title('Student Database Management System')
    EFroot.grab_set()#frame will not go in background utill intended operation is done
    EFroot.geometry('500x400+300+130')
    EFroot.config(background='honeydew2')
    EFroot.iconbitmap('student3_118006.ico')

    ######################################### EF1 lable-------------

    EFIDlable=tkinter.Label(EFroot,text='Enter ID : ',font=('Tahoma',15),background='honeydew2')
    EFIDlable.place(x=10,y=10)
    
    EFIDval=tkinter.StringVar()#To accept the entry value into user variable
    EFIDentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFIDval)
    EFIDentry.place(x=170,y=10)


    EFNamelable=tkinter.Label(EFroot,text='Enter Name : ',font=('Tahoma',15),background='honeydew2')
    EFNamelable.place(x=10,y=60)
    
    EFNameval=tkinter.StringVar()#To accept the entry value into user variable
    EFNameentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFNameval)
    EFNameentry.place(x=170,y=60)


    EFMoblable=tkinter.Label(EFroot,text='Enter Mobile : ',font=('Tahoma',15),background='honeydew2')
    EFMoblable.place(x=10,y=110)
    
    EFMobval=tkinter.StringVar()#To accept the entry value into user variable
    EFMobentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFMobval)
    EFMobentry.place(x=170,y=110)


    EFEmaillable=tkinter.Label(EFroot,text='Enter Email : ',font=('Tahoma',15),background='honeydew2')
    EFEmaillable.place(x=10,y=160)
    
    EFEmailval=tkinter.StringVar()#To accept the entry value into user variable
    EFEmailentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFEmailval)
    EFEmailentry.place(x=170,y=160)


    EFCitylable=tkinter.Label(EFroot,text='Enter Your City : ',font=('Tahoma',15),background='honeydew2')
    EFCitylable.place(x=10,y=210)
    
    EFCityval=tkinter.StringVar()#To accept the entry value into user variable
    EFCityentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFCityval)
    EFCityentry.place(x=170,y=210)

    EFDOBlable=tkinter.Label(EFroot,text='Enter D.O.B : ',font=('Tahoma',15),background='honeydew2')
    EFDOBlable.place(x=10,y=260)
    
    EFDOBval=tkinter.StringVar()#To accept the entry value into user variable
    EFDOBentry=tkinter.Entry(EFroot,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='honeydew3',textvariable=EFDOBval)
    EFDOBentry.place(x=170,y=260)

    EFSubmit=tkinter.Button(EFroot,text='Submit',font=('Tahoma',15,'bold'),relief='groove',border=2,borderwidth=5,background='coral',activebackground='light coral',command=AddStud)
    EFSubmit.place(x=200,y=325)

def EntryField2():
    def SearchStud():
        searchid=EF2IDval.get()
        searchstr='select * from student where ID=%s'
        cursor.execute(searchstr,searchid)
        searchoutput=cursor.fetchall()
        ResultTable.delete(*ResultTable.get_children())
        for i in searchoutput:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5]]
        ResultTable.insert('','end',values=vv)

        
    EF2root=tkinter.Toplevel()
    EF2root.title('Student Database Management System')
    EF2root.geometry('400x150+300+200')
    EF2root.config(background='lightsalmon2')
    EF2root.iconbitmap('student3_118006.ico')
    EF2root.resizable(False,False)
    EF2root.grab_set()
    ########################### Entry Field For search------
    EF2IDlable=tkinter.Label(EF2root,text=' Enter ID Of: '+'\n'+'The Student',font=('Tahoma',15),background='lightsalmon2',anchor='n')
    EF2IDlable.place(x=10,y=10)
    
    EF2IDval=tkinter.StringVar()#To accept the entry value into user variable
    EF2IDentry=tkinter.Entry(EF2root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lightsalmon3',textvariable=EF2IDval)
    EF2IDentry.place(x=140,y=20)


    EF2Submit=tkinter.Button(EF2root,text='Submit',relief='groove',font=('Tahoma',15,'bold'),background='lightsalmon3',activebackground='lightsalmon2',command=SearchStud)
    EF2Submit.place(x=160,y=80)



def EntryField3():
    def DeletehStud():
        searchid=EF3IDval.get()
        searchstr='delete from student where ID=%s'
        cursor.execute(searchstr,searchid)
        messagebox.showinfo('Notification','Student Of Id {} is Deleted!!!'.format(searchid))
        resp=messagebox.askokcancel('Notification','Do Yo Want To Delete All the Records Of Database?')
        if(resp==True):
            deletestr='delete from student'
            cursor.execute(deletestr)
            var.commit()
            messagebox.showinfo('Notification','Data Deletion Successful')
        else:
            EF3root.destroy()

    EF3root=tkinter.Toplevel()
    EF3root.title('Student Database Management System')
    EF3root.geometry('400x150+300+200')
    EF3root.config(background='light slate gray')
    EF3root.iconbitmap('student3_118006.ico')
    EF3root.resizable(False,False)
    EF3root.grab_set()
    ########################### Entry Field For search------
    EF3IDlable=tkinter.Label(EF3root,text=' Enter ID Of: '+'\n'+'The Student',font=('Tahoma',15),background='slate gray',anchor='n')
    EF3IDlable.place(x=10,y=10)
    
    EF3IDval=tkinter.StringVar()#To accept the entry value into user variable
    EF3IDentry=tkinter.Entry(EF3root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='slate gray',textvariable=EF3IDval)
    EF3IDentry.place(x=140,y=20)


    EF3Submit=tkinter.Button(EF3root,text='Delete',relief='groove',font=('Tahoma',15,'bold'),background='light slate gray',activebackground='slate gray',command=DeletehStud)
    EF3Submit.place(x=160,y=80)





def EntryField4():
    def updatestud():
        stud_ID=EF4IDval.get()
        stud_name=EF4Nameval.get()
        mob=EF4Mobval.get()
        stud_mail=EF4Emailval.get()
        stud_city=EF4Cityval.get()
        stud_dob=EF4DOBval.get()
        try:
            searchid=EF4IDval.get()
            searchstr='delete from student where ID=%s'
            cursor.execute(searchstr,searchid)
            Entry='insert into Student values (%s,%s,%s,%s,%s,%s)'
            cursor.execute(Entry,(stud_ID,stud_name,mob,stud_mail,stud_city,stud_dob))
            var.commit()
            response=messagebox.askyesnocancel('Notification','Student Of ID {} Updated Successfully...Do Yo Want To Clear Form?.'.format(stud_ID),parent=EF4root)
            if(response==True):
                EF4IDval.set(' ')
                EF4Nameval.set(' ')
                EF4Mobval.set(' ')
                EF4Emailval.set(' ')
                EF4Cityval.set(' ')
                EF4DOBval.set(' ')
        except:
            messagebox.showerror('Notification','Id Already Exists!!!')
        strr='select * from Student'
        cursor.execute(strr)
        output_data=cursor.fetchall()
        ResultTable.delete(*ResultTable.get_children())
        for i in output_data:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5]]
            ResultTable.insert('','end',values=vv)

    EF4root=tkinter.Toplevel()
    EF4root.title('Student Database Management System')
    EF4root.grab_set()#frame will not go in background utill intended operation is done
    EF4root.geometry('500x400+300+130')
    EF4root.config(background='lavender')
    EF4root.iconbitmap('student3_118006.ico')
    EF4root.resizable(False,False)


    ############################# Entry Field to update Info-----------

    EF4IDlable=tkinter.Label(EF4root,text='Enter ID : ',font=('Tahoma',15),background='lavender')
    EF4IDlable.place(x=10,y=10)
    
    EF4IDval=tkinter.StringVar()#To accept the entry value into user variable
    EF4IDentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4IDval)
    EF4IDentry.place(x=170,y=10)


    EF4Namelable=tkinter.Label(EF4root,text='Enter Name : ',font=('Tahoma',15),background='lavender')
    EF4Namelable.place(x=10,y=60)
    
    EF4Nameval=tkinter.StringVar()#To accept the entry value into user variable
    EF4Nameentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4Nameval)
    EF4Nameentry.place(x=170,y=60)


    EF4Moblable=tkinter.Label(EF4root,text='Enter Mobile : ',font=('Tahoma',15),background='lavender')
    EF4Moblable.place(x=10,y=110)
    
    EF4Mobval=tkinter.StringVar()#To accept the entry value into user variable
    EF4Mobentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4Mobval)
    EF4Mobentry.place(x=170,y=110)


    EF4Emaillable=tkinter.Label(EF4root,text='Enter Email : ',font=('Tahoma',15),background='lavender')
    EF4Emaillable.place(x=10,y=160)
    
    EF4Emailval=tkinter.StringVar()#To accept the entry value into user variable
    EF4Emailentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4Emailval)
    EF4Emailentry.place(x=170,y=160)


    EF4Citylable=tkinter.Label(EF4root,text='Enter Your City : ',font=('Tahoma',15),background='lavender')
    EF4Citylable.place(x=10,y=210)
    
    EF4Cityval=tkinter.StringVar()#To accept the entry value into user variable
    EF4Cityentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4Cityval)
    EF4Cityentry.place(x=170,y=210)

    EF4DOBlable=tkinter.Label(EF4root,text='Enter D.O.B : ',font=('Tahoma',15),background='lavender')
    EF4DOBlable.place(x=10,y=260)
    
    EF4DOBval=tkinter.StringVar()#To accept the entry value into user variable
    EF4DOBentry=tkinter.Entry(EF4root,font=('Tahoma',15),border=5,borderwidth=2,relief='solid',bg='lavender blush',textvariable=EF4DOBval)
    EF4DOBentry.place(x=170,y=260)

    EF4Submit=tkinter.Button(EF4root,text='Submit',font=('Tahoma',15,'bold'),relief='groove',border=2,borderwidth=5,background='coral',activebackground='light coral',command=updatestud)
    EF4Submit.place(x=200,y=325)


def showAll():
    showallcommand='select * from student'
    cursor.execute(showallcommand)
    output=cursor.fetchall()
    ResultTable.delete(*ResultTable.get_children())
    for i in output:
        showutput=[i[0],i[1],i[2],i[3],i[4],i[5],]
        ResultTable.insert('','end',values=showutput)


def exportdata():
    savebox=filedialog.asksaveasfilename()
    #print(savebox)############---------------->To print the pathe of current storage location
    childResTable=ResultTable.get_children()#######---------->Get data present in result table
    exp_id,exp_name,exp_mob,exp_mail,exp_city,exp_dob=[],[],[],[],[],[]
    for i in childResTable:
        content=ResultTable.item(i)
        unit=content['values']
        exp_id.append(unit[0]),exp_name.append(unit[1]),exp_mob.append(unit[2]),exp_mail.append(unit[3]),exp_city.append(unit[4]),exp_dob.append(unit[5])

    file_heading=['ID','Name','Mobile No','E-mail','City','Date Of Birth']
    df=pd.DataFrame(list(zip(exp_id,exp_name,exp_mob,exp_mail,exp_city,exp_dob)),columns=file_heading)
    filepath='{}.csv'.format(savebox)
    df.to_csv(filepath,index=False)
    messagebox.showinfo('Notification','Data Successfully Exported {} location'.format(filepath))


def exitcommand():
    selection=messagebox.askyesnocancel('Warning','Do You Want To Exit?')
    if(selection):
        root.destroy()





import time
import tkinter
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas as pd
root=tkinter.Tk()
root.title('Student Management System')
root.geometry('1174x700+200+50')
root.config(background='light slate gray')
root.resizable(False,False)
root.iconbitmap('student3_118006.ico')
##########################################Frames---------------

EntryFrame=tkinter.Frame(root,background='blanched almond',relief='groove',borderwidth=5)
EntryFrame.place(x=10,y=80,width=500,height=600)


EF1=tkinter.Button(root,text='1. Add Student',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=EntryField1)
EF1.place(x=100,y=110)

EF2=tkinter.Button(root,text='2. Search Student',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=EntryField2)
EF2.place(x=100,y=190)

EF3=tkinter.Button(root,text='3. Delete Student',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=EntryField3)
EF3.place(x=100,y=270)

EF4=tkinter.Button(root,text='4. Update Student',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=EntryField4)
EF4.place(x=100,y=350)

EF5=tkinter.Button(root,text='5. Show All Student',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=showAll)
EF5.place(x=100,y=430)

EF6=tkinter.Button(root,text='6. Export Data',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=exportdata)
EF6.place(x=100,y=510)

EF7=tkinter.Button(root,text='7. Exit',font=('Tahoma',20,'bold'),relief='ridge',borderwidth=4,width=17,background='dark slate gray',activeforeground='slate gray',activebackground='honeydew3',command=exitcommand)
EF7.place(x=100,y=590)








ResultFrame=tkinter.Frame(root,background='blanched almond',relief='groove',borderwidth=5)
ResultFrame.place(x=550,y=80,width=620,height=600)

############################## table creation in Result Frame---------------------


head_style=ttk.Style()  #For styling the heading of table in resultframe
head_style.configure('Treeview.Heading',font=('Tahoma',15,'bold'),foreground='salmon1')
head_style.configure('Treeview',font=('Tahoma',15,'bold'),foreground='salmon1')

x_bar=tkinter.Scrollbar(ResultFrame,orient='horizontal')  #------------->for creating scrollbar
#y_bar=tkinter.Scrollbar(ResultFrame,orient='vertical')

ResultTable=Treeview(ResultFrame,columns=('ID','Name','Mobile No','E-mail','City','D.O.B'),xscrollcommand=x_bar.set) #-------->For Creating result table

x_bar.pack(side='bottom',fill='x')
x_bar.config(command=ResultTable.xview)
#y_bar.pack(side='right',fill='y')
#y_bar.config(command=ResultTable.yview)
ResultTable.heading('ID',text='ID')
ResultTable.heading('Name',text='Name')
ResultTable.heading('Mobile No',text='Mobile No')
ResultTable.heading('E-mail',text='E-mail')
ResultTable.heading('City',text='City')
ResultTable.heading('D.O.B',text='D.O.B')
ResultTable['show']='headings' #----------------->For Eliminating extra column by default shown in treeview table
ResultTable.column('ID',width=100)#--------------->To Change the size of the column

ResultTable.pack(fill='both',expand=1)






############################################ CenterDIV--------

CenterDiv=tkinter.Label(root,text='Student Database Management System',font=('Tahoma',25,'bold'),relief='ridge',borderwidth=4,width=35,background='dark slate gray')
CenterDiv.place(x=260,y=5)

############################################  ClockDiv-------

clock=tkinter.Label(root,font=('Tahoma',15,'bold'),background='light slate gray')
clock.place(x=5,y=5)
CurrentTime()

############################################ DB Button------

button=tkinter.Button(root,text='LogIn',font=('Tahoma',15,'bold'),border=5,borderwidth=5,bg='light slate gray',activebackground='dark slate gray',activeforeground='lavender',command=ConnectDB)
button.place(x=1050,y=5)



root.mainloop()


