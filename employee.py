from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class Employee:
  def __init__(self, root):
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title('Krayrpol Employee Management System')

    # Variables
    self.var_com=StringVar()
    self.name=StringVar()
    self.surname=StringVar()
    self.birthdate=StringVar()
    self.phone=StringVar()
    self.email=StringVar()
    self.id_proof=StringVar()
    self.id_proofcomb=StringVar()
    self.visa_expiry=StringVar()
    self.position=StringVar()
    self.address=StringVar()
    self.hire_date=StringVar()
    self.end_date=StringVar()
    self.salary=StringVar()
    self.country=StringVar()



    # title
    lbl_title = Label(self.root, text='KRAYRPOL AGENCJA PRACA', font=('times new roman', 37, 'bold'), fg='darkblue',
                      bg='white')
    lbl_title.place(x=0, y=0, width=1530, height=80)
    # logo
    img_logo = Image.open('/Users/suman/Downloads/Frame 2.jpg')
    img_logo = img_logo.resize((80, 80), Image.ANTIALIAS)
    self.photo_logo = ImageTk.PhotoImage(img_logo)

    self.logo = Label(self.root, image=self.photo_logo)
    self.logo.place(x=270, y=0, width=80, height=80)
    # Image Frame
    img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
    img_frame.place(x=0, y=80, width=1530, height=265)

    # 1st image
    img1 = Image.open('/Users/suman/Downloads/img1.jpg')
    img1 = img1.resize((750, 260), Image.ANTIALIAS)
    self.photo1 = ImageTk.PhotoImage(img1)

    self.img_1 = Label(self.root, image=self.photo1)
    self.img_1.place(x=300, y=85, width=750, height=260)

    # Main Frame
    Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
    Main_frame.place(x=10, y=280, width=1500, height=560)

    # upper Frame
    upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information',
                             font=('times new roman', 11, 'bold'), fg='red')
    upper_frame.place(x=10, y=10, width=1480, height=350)
    #Labels and Entry Fields

    lbl_company =Label(upper_frame,text='Company:',font=('arial', 11, 'bold'))
    lbl_company.grid(row=0,column=0,padx=2,sticky=W)

    combo_company=ttk.Combobox(upper_frame,textvariable=self.var_com,font=('arial', 12, 'bold'),width=17,state='readonly')
    combo_company['value']=('select Company','Mpack Sp. z o. o','EWA Smolny','Akpol','Algas','Hyundai')
    combo_company.current(0)
    combo_company.grid(row=0,column=1, padx=2, pady=10,sticky=W)

    # Name
    lbl_name=Label(upper_frame,font=('arial',12,'bold'),text='Name:')
    lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

    txt_name=ttk.Entry(upper_frame,textvariable=self.name,width=22, font=('arial',11,'bold'))
    txt_name.grid(row=0, column=3,padx=2, pady=7)

    # SurName
    lbl_surname=Label(upper_frame,font=('arial',12,'bold'),text='Surname:')
    lbl_surname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

    txt_surname=ttk.Entry(upper_frame,textvariable=self.surname,width=22, font=('arial',11,'bold'))
    txt_surname.grid(row=1, column=3,padx=2, pady=7)

    # Dob
    lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text='BirthDate:')
    lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

    txt_dob=ttk.Entry(upper_frame,textvariable=self.birthdate,width=22, font=('arial',11,'bold'))
    txt_dob.grid(row=2, column=3,padx=2, pady=7)

    # Position
    lbl_position=Label(upper_frame,font=('arial',12,'bold'),text='Position:')
    lbl_position.grid(row=1,column=0,sticky=W,padx=2,pady=7)

    txt_position=ttk.Entry(upper_frame,textvariable=self.position,width=22, font=('arial',11,'bold'))
    txt_position.grid(row=1, column=1,padx=2, pady=7)

    # Address
    lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:')
    lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

    txt_address=ttk.Entry(upper_frame,textvariable=self.address,width=22, font=('arial',11,'bold'))
    txt_address.grid(row=2, column=1,padx=2, pady=7)

    # hiredate
    lbl_hiredate=Label(upper_frame,font=('arial',12,'bold'),text='Hire Date:')
    lbl_hiredate.grid(row=3,column=0,sticky=W,padx=2,pady=7)

    txt_hiredate=ttk.Entry(upper_frame,textvariable=self.hire_date,width=22, font=('arial',11,'bold'))
    txt_hiredate.grid(row=3, column=1,padx=2, pady=7)

    # contract ends
    lbl_enddate=Label(upper_frame,font=('arial',12,'bold'),text='Expires:')
    lbl_enddate.grid(row=4,column=0,sticky=W,padx=2,pady=7)

    txt_enddate=ttk.Entry(upper_frame,textvariable=self.end_date,width=22, font=('arial',11,'bold'))
    txt_enddate.grid(row=4, column=1,padx=2, pady=7)

    # Salary
    lbl_salary=Label(upper_frame,font=('arial',12,'bold'),text='Salary:')
    lbl_salary.grid(row=5,column=0,sticky=W,padx=2,pady=7)

    txt_salary=ttk.Entry(upper_frame,textvariable=self.salary,width=22, font=('arial',11,'bold'))
    txt_salary.grid(row=5, column=1,padx=2, pady=7)

    #Id
    combo_id=ttk.Combobox(upper_frame,textvariable=self.id_proofcomb,font=('arial', 12, 'bold'),width=17,state='readonly')
    combo_id['value']=('Select ID','Passport','Dowód osobisty','Travel Document','Other Id')
    combo_id.current(0)
    combo_id.grid(row=5,column=2, padx=2, pady=10,sticky=W)

    txt_id=ttk.Entry(upper_frame,textvariable=self.id_proof,width=22, font=('arial',11,'bold'))
    txt_id.grid(row=5, column=3,padx=2, pady=7)

    # phone
    lbl_tel=Label(upper_frame,font=('arial',12,'bold'),text='Phone:')
    lbl_tel.grid(row=3,column=2,sticky=W,padx=2,pady=7)

    txt_tel=ttk.Entry(upper_frame,textvariable=self.phone,width=22, font=('arial',11,'bold'))
    txt_tel.grid(row=3, column=3,padx=2, pady=7)
    # email
    lbl_email = Label(upper_frame, font=('arial', 12, 'bold'), text='Email:')
    lbl_email.grid(row=4, column=2, sticky=W, padx=2, pady=7)

    txt_email = ttk.Entry(upper_frame, textvariable=self.email,width=22, font=('arial', 11, 'bold'))
    txt_email.grid(row=4, column=3, padx=2, pady=7)

    # country
    lbl_country = Label(upper_frame, font=('arial', 12, 'bold'), text='Nationality:')
    lbl_country.grid(row=6, column=0, sticky=W, padx=2, pady=7)

    txt_country = ttk.Entry(upper_frame,textvariable=self.country, width=22, font=('arial', 11, 'bold'))
    txt_country.grid(row=6, column=1, padx=2, pady=7)

    # visa
    lbl_visa = Label(upper_frame, font=('arial', 12, 'bold'), text='Visa Expires:')
    lbl_visa.grid(row=6, column=2, sticky=W, padx=2, pady=7)

    txt_visa = ttk.Entry(upper_frame,textvariable=self.visa_expiry, width=22, font=('arial', 11, 'bold'))
    txt_visa.grid(row=6, column=3, padx=2, pady=7)

    # button Frame
    button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
    button_frame.place(x=1290, y=10, width=170, height=160)

    btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial', 15, 'bold'),width=13,bg='green',fg='Blue')
    btn_add.grid(row=0,column=0, padx=1, pady=5)

    btn_update=Button(button_frame,text='Update',font=('arial', 15, 'bold'),width=13,bg='green',fg='Blue')
    btn_update.grid(row=1,column=0, padx=1, pady=5)

    btn_delete=Button(button_frame,text='Delete',font=('arial', 15, 'bold'),width=13,bg='green',fg='Blue')
    btn_delete.grid(row=2,column=0, padx=1, pady=5)

    btn_clear=Button(button_frame,text='Clear',font=('arial', 15, 'bold'),width=13,bg='green',fg='Blue')
    btn_clear.grid(row=3,column=0, padx=1, pady=5)

    # down Frame
    down_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table',
                             font=('times new roman', 11, 'bold'), fg='red')
    down_frame.place(x=10, y=310, width=1480, height=270)
    # search Frame
    search_frame = LabelFrame(down_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information',
                             font=('times new roman', 11, 'bold'), fg='red')
    search_frame.place(x=0, y=0, width=1472, height=270)

    search_by = Label(search_frame,font=('arial', 15, 'bold'),text='Search by:',fg='white',bg='red')
    search_by.grid(row=0, column=0,sticky=W,padx=5)

    #search
    self.var_com_search=StringVar()

    com_txt_search=ttk.Combobox(search_frame,state='readonly',font=('arial', 12, 'bold'),width=18)
    com_txt_search['value']=("Select Option","name","nationality","company")
    com_txt_search.current(0)
    com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

    txt_search=ttk.Entry(search_frame,width=22, font=('arial', 15, 'bold'))
    txt_search.grid(row=0, column=2, padx=5)

    btn_search=Button(search_frame, text="Search",font=('arial', 15, 'bold'))
    btn_search.grid(row=0,column=3,padx=5)

    btn_showAll=Button(search_frame,text="Show All",font=('arial', 15, 'bold'))
    btn_showAll.grid(row=0, column=4, padx=5)

    #=========== Employee table =======================
    # Table Frame
    table_frame = Frame(down_frame, bd=3, relief=RIDGE)
    table_frame.place(x=0, y=60, width=1470, height=170)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.employee_table=ttk.Treeview(table_frame,column=('com','name','surname','birthdate','phone','email','id_proof','visa_expiry','position','address','hire_date','end_date','salary','country',),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=self.employee_table.xview())
    scroll_y.config(command=self.employee_table.yview())

    self.employee_table.heading('com',text='Company')
    self.employee_table.heading('name',text='Name')
    self.employee_table.heading('surname',text='Surname')
    self.employee_table.heading('birthdate',text='Birth Date')
    self.employee_table.heading('phone',text='Phone')
    self.employee_table.heading('email',text='Email')
    self.employee_table.heading('id_proof',text='ID')
    self.employee_table.heading('visa_expiry',text='Visa Expiry')
    self.employee_table.heading('position',text='Position')
    self.employee_table.heading('address',text='Address')
    self.employee_table.heading('hire_date',text='Hire Date')
    self.employee_table.heading('end_date',text='End Date')
    self.employee_table.heading('salary',text='Salary')
    self.employee_table.heading('country',text='Nationality')

    self.employee_table['show']='headings'
    self.employee_table.column("com",width=100)
    self.employee_table.column("name",width=100)
    self.employee_table.column("surname",width=100)
    self.employee_table.column("birthdate",width=100)
    self.employee_table.column("phone",width=100)
    self.employee_table.column("email",width=100)
    self.employee_table.column("id_proof",width=100)
    self.employee_table.column("visa_expiry",width=100)
    self.employee_table.column("position",width=100)
    self.employee_table.column("address",width=100)
    self.employee_table.column("hire_date",width=100)
    self.employee_table.column("end_date",width=100)
    self.employee_table.column("salary",width=100)
    self.employee_table.column("country",width=100)

    self.employee_table.pack(fill=BOTH,expand=1)
   # self.fetch_data()

  # ================= Function Declaration ================
  def add_data(self):
    if self.var_com.get()=="" or self.id_proof.get()=="":
      messagebox.showerror('Error', 'All Fields are required')

    else:
      try:
        conn= mysql.connect.connect(host='locolhost',username='root', password='Test123', database='my data')
        my_cursor=conn.cursor()
        my_cursor.execute('insert into Tablename values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                  self.var_com.get(),
                                                                                                  self.name.get(),
                                                                                                  self.surname.get(),
                                                                                                  self.birthdate.get(),
                                                                                                  self.phone.get(),
                                                                                                  self.email.get(),
                                                                                                  self.id_proofcomb.get(),
                                                                                                  self.id_proof.get(),
                                                                                                  self.visa_expiry.get(),
                                                                                                  self.position.get(),
                                                                                                  self.address.get(),
                                                                                                  self.hire_date.get(),
                                                                                                  self.end_date.get(),
                                                                                                  self.salary.get(),
                                                                                                  self.country.get()
                                                                                                      ))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Employee has been added!',parent=self.root)
      except Exception as es:
        messagebox.showerror('Error',f'Due To: {str(es)}',parent=self.root)


#














if __name__ == "__main__":
  root = Tk()
  obj = Employee(root)
  root.mainloop()
