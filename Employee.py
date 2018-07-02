from tkinter import *
from tkinter import ttk
import sqlite3

class Detail:

    db_name='database.db'

    def __init__(self, root):

        self.root = root
        self.root.title ('Employee Detail')

        Top = Frame(root, width = 1350, height = 100, bd = 14, relief = 'raise')
        Top.pack(side=TOP)

        TopLabelTitle = Label(Top, font = ('arial', 50, 'bold'), text = "EMPLOYEE DETAILS", bd = 5, width = 32, justify = 'center')
        TopLabelTitle.grid(row = 0, column = 0)

        leftFrame = Frame(root, width= 800, height= 650, bd = 5, relief='raise')
        leftFrame.pack(side = LEFT)

        rightFrame = Frame(root, width=470, height = 650, bd = 5, relief = 'raise')
        rightFrame.pack(side = RIGHT)

        frameL = LabelFrame (leftFrame, text = 'Add new record', font=('arial 15 bold'))
        frameL.grid (row = 1, column =0)

        rightFrameTop = Frame(rightFrame, width = 470, height = 450, bd = 8, relief = 'raise')
        rightFrameTop.pack(side = TOP)

        rightFrameBottom = Frame(rightFrame, width = 470, height = 250, bd = 8, relief = 'raise')
        rightFrameBottom.pack(side =BOTTOM)

        Label (frameL, text = 'Name:', width = 18, height = 1, font=('arial 15 bold')).grid (row = 1)
        self.name = Entry (frameL, font=('arial 15 bold'))
        self.name.grid(row = 1, column = 2)

        Label (frameL, text = 'ID :', width = 18, height = 3, font=('arial 15 bold')).grid (row = 1, column = 4 )
        self.id = Entry (frameL, font=('arial 15 bold'))
        self.id.grid(row = 1, column = 5)

        Label (frameL, text = 'Mobile Number :', width = 18, height = 3, font=('arial 15 bold')).grid(row = 2)
        self.mobile = Entry (frameL, font=('arial 15 bold'))
        self.mobile.grid(row = 2, column = 2)

        Label (frameL, text = 'Email :', width = 18, height = 3, font=('arial 15 bold')).grid (row = 2, column = 4 )
        self.email = Entry (frameL, font=('arial 15 bold'))
        self.email.grid(row = 2, column = 5)

        Label (frameL, text = 'Date of Birth :', width = 18, height = 4, font=('arial 15 bold')).grid(row = 3)
        self.DateOfBirth = Entry (frameL, font=('arial 15 bold'))
        self.DateOfBirth.grid(row = 3, column = 2)

        Label (frameL, text = 'Date of Joining :', width = 18, height = 4, font=('arial 15 bold')).grid (row = 3, column = 4 )
        self.DateOfJoining = Entry (frameL, font=('arial 15 bold'))
        self.DateOfJoining.grid(row = 3, column = 5)

        Label (frameL, text = 'Country', width = 18, height = 4, font=('arial 15 bold')).grid(row = 4)
        self.country = Entry (frameL, font=('arial 15 bold'))
        self.country.grid(row = 4, column = 2)

        Label (frameL, text = 'State', width = 18, height = 4, font=('arial 15 bold')).grid (row = 4, column = 4 )
        self.state = Entry (frameL, font=('arial 15 bold'))
        self.state.grid(row = 4, column = 5)

        Label (frameL, text = 'City', width = 18, height = 4, font=('arial 15 bold')).grid(row = 5)
        self.city = Entry (frameL, font=('arial 15 bold'))
        self.city.grid(row = 5, column = 2)

        Label (frameL, text = 'Zip Code', width = 18, height = 2, font=('arial 15 bold')).grid (row = 5, column = 4 )
        self.zip = Entry (frameL, font=('arial 15 bold'))
        self.zip.grid(row = 5, column = 5)

        ttk.Button (frameL, text = 'Add Record', command = self.adding).grid (row = 6, columnspan = 6)
        self.message = Label (frameL, text = '', fg = 'red', font=('arial 15 bold'))
        self.message.grid(row = 0, columnspan =5 )

        self.tree=ttk.Treeview (rightFrameTop,height = 20, columns = ("Name","ID","Mobile","Email","Date Of Birth","Date Of Joining","Country","State","City","Zip Code"))
        self.tree.pack ()
        scrollbar_horizontal = ttk.Scrollbar(rightFrameTop, orient='horizontal', command = self.tree.xview)      
        scrollbar_horizontal.pack(side='bottom', fill=X)    
        self.tree.heading('#0', text = 'Name', anchor = W)
        self.tree.heading('#1', text = 'ID', anchor = W)
        self.tree.heading('#2', text = 'Mobile', anchor = W)
        self.tree.heading('#3', text = 'Email', anchor = W)
        self.tree.heading('#4', text = 'Date Of Birth', anchor = W)
        self.tree.heading('#5', text = 'Date Of Joining', anchor = W)
        self.tree.heading('#6', text = 'Country', anchor = W)
        self.tree.heading('#7', text = 'State', anchor = W)
        self.tree.heading('#8', text = 'City', anchor = W)
        self.tree.heading('#9', text = 'Zip Code', anchor = W)
        
        
        ttk.Button (rightFrameBottom, text = 'View Record', command = self.ViewRecord).grid (row = 1, column = 0)
        ttk.Button (rightFrameBottom, text = 'Delete Record', command = self.deleting).grid (row = 1, column = 2)
        ttk.Button (rightFrameBottom, text = 'Edit', command = self.editing).grid (row = 1, column = 1)

        self.viewing_record()
        
        
    def run_query (self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute (query, parameters)
            conn.commit()
        return query_result

    def viewing_record (self):
        record = self.tree.get_children()
        for element in record:
            self.tree.delete(element)
        query = 'SELECT * FROM Employee ORDER BY name DESC'
        db_row = self.run_query (query)
        for row in db_row:
            self.tree.insert ('', 0, text = (row[0]), values = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    def validation (self):
        return len (self.name.get ()) != 0 and len (self.id.get ()) != 0 and len (self.mobile.get()) !=0 and len (self.email.get()) !=0 and len (self.DateOfBirth.get()) !=0 and len (self.DateOfJoining.get()) !=0 and len (self.country.get()) !=0 and len (self.state.get()) !=0 and len (self.city.get()) !=0 and len (self.zip.get()) !=0

#----------------------------------------------Adding Record-----------------------------------------------------------------------------------------

    def adding (self):
        if self.validation ():
            query = 'INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.name.get(), self.id.get(), self.mobile.get(), self.email.get(), self.DateOfBirth.get(), self.DateOfJoining.get(), self.country.get(), self.state.get(), self.city.get(), self.zip.get())
            self.run_query (query, parameters)
            self.message ['text'] = 'Record {} added'.format (self.name.get())
            self.name.delete(0, END)
            self.id.delete(0, END)
            self.mobile.delete(0, END)
            self.email.delete(0, END)
            self.DateOfBirth.delete(0, END)
            self.DateOfJoining.delete(0, END)
            self.country.delete(0, END)
            self.state.delete(0, END)
            self.city.delete(0, END)
            self.zip.delete(0, END)
        else:
            self.message['text'] = 'Some fields are empty'
        self.viewing_record()    


#--------------------------------------------deleting Record-------------------------------------------------------------------------------

    def deleting (self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection ())['values'][0]
        except IndexError as e:
            self.message['text'] = 'please, select recode !!'
            return

        self.message['text'] = ''
        name = self.tree.item (self.tree.selection ())['text']
        query = 'DELETE FROM Employee WHERE name = ?'
        self.run_query(query,(name, ))
        self.message['text'] = 'Recode {} deleted'.format(name)
        self.viewing_record()


#--------------------------------Editing Record-------------------------------------------------------------------------

    def editing(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, Select Record'

        old_name = self.tree.item(self.tree.selection())['text']
        old_id = self.tree.item(self.tree.selection())['values'][0]
        old_mobile = self.tree.item(self.tree.selection())['values'][1]
        old_email = self.tree.item(self.tree.selection())['values'][2]
        old_DateOfBirth = self.tree.item(self.tree.selection())['values'][3]
        old_DateOfJoining = self.tree.item(self.tree.selection())['values'][4]
        old_country = self.tree.item(self.tree.selection())['values'][5]
        old_state = self.tree.item(self.tree.selection())['values'][6]
        old_city = self.tree.item(self.tree.selection())['values'][7]
        old_zip = self.tree.item(self.tree.selection())['values'][8]

        self.edit_wind = Toplevel()
        self.edit_wind.title('Editing')

        Label(self.edit_wind, text = 'Old Name:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly').grid(row = 0, column = 2)
        Label(self.edit_wind, text = 'New name:').grid(row = 0, column = 3)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 0, column = 4)

        Label(self.edit_wind, text = 'Old ID:').grid(row = 1, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_id), state = 'readonly').grid(row = 1, column = 2)
        Label(self.edit_wind, text = 'New ID:').grid(row = 1, column = 3)
        new_id = Entry(self.edit_wind)
        new_id.grid(row = 1, column = 4)

        Label(self.edit_wind, text = 'Old Mobile:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_mobile), state = 'readonly').grid(row = 2, column = 2)
        Label(self.edit_wind, text = 'New Mobile:').grid(row = 2, column = 3)
        new_mobile = Entry(self.edit_wind)
        new_mobile.grid(row = 2, column = 4)

        Label(self.edit_wind, text = 'Old Email:').grid(row = 3, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_email), state = 'readonly').grid(row = 3, column = 2)
        Label(self.edit_wind, text = 'New Email:').grid(row = 3, column = 3)
        new_email = Entry(self.edit_wind)
        new_email.grid(row = 3, column = 4)

        Label(self.edit_wind, text = 'Old DateOfBirth:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_DateOfBirth), state = 'readonly').grid(row = 4, column = 2)
        Label(self.edit_wind, text = 'New DateOfBirth:').grid(row = 4, column = 3)
        new_DateOfBirth = Entry(self.edit_wind)
        new_DateOfBirth.grid(row = 4, column = 4)

        Label(self.edit_wind, text = 'Old DateOfJoining:').grid(row = 5, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_DateOfJoining), state = 'readonly').grid(row = 5, column = 2)
        Label(self.edit_wind, text = 'New DateOfBirth:').grid(row = 5, column = 3)
        new_DateOfJoining = Entry(self.edit_wind)
        new_DateOfJoining.grid(row = 5, column = 4)
        
        Label(self.edit_wind, text = 'Old Country:').grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_country), state = 'readonly').grid(row = 6, column = 2)
        Label(self.edit_wind, text = 'New Country:').grid(row = 6, column = 3)
        new_country = Entry(self.edit_wind)
        new_country.grid(row = 6, column = 4)

        Label(self.edit_wind, text = 'Old State:').grid(row = 7, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_state), state = 'readonly').grid(row = 7, column = 2)
        Label(self.edit_wind, text = 'New State:').grid(row = 7, column = 3)
        new_state = Entry(self.edit_wind)
        new_state.grid(row = 7, column = 4)

        Label(self.edit_wind, text = 'Old City:').grid(row = 8, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_city), state = 'readonly').grid(row = 8, column = 2)
        Label(self.edit_wind, text = 'New City:').grid(row = 8, column = 3)
        new_city = Entry(self.edit_wind)
        new_city.grid(row = 8, column = 4)

        Label(self.edit_wind, text = 'Old Zip:').grid(row = 9, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_zip), state = 'readonly').grid(row = 9, column = 2)
        Label(self.edit_wind, text = 'New Zip:').grid(row = 9, column = 3)
        new_zip = Entry(self.edit_wind)
        new_zip.grid(row = 9, column = 4)

        ttk.Button(self.edit_wind, text = 'Save Changes', command = lambda:self.edit_records(new_name.get(),old_name, new_id.get(), old_id, new_mobile.get(), old_mobile, new_email.get(), old_email, new_DateOfBirth.get(), old_DateOfBirth, new_DateOfJoining.get(), old_DateOfJoining, new_country.get(), old_country, new_state.get(), old_state, new_city.get(), old_city, new_zip.get(), old_zip)).grid(row = 10,columnspan = 6)

        self.edit_wind.mainloop()

    def edit_records(self, new_name, old_name, new_id, old_id, new_mobile, old_mobile, new_email, old_email, new_DateOfBirth, old_DateOfBirth, new_DateOfJoining, old_DateOfJoining, new_country, old_country, new_state, old_state, new_city, old_city, new_zip, old_zip):
        query = 'UPDATE Employee SET name = ?, id = ?, mobile = ?, email = ?, DateOfBirth = ?, DateOfJoining = ?, country = ?, state = ?, city = ?, zip = ?  WHERE name = ? AND id = ? AND mobile = ? AND email = ? AND DateOfBirth = ? AND DateOfJoining = ? AND country = ? AND state = ? AND city = ? AND zip = ?'
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} changed'.format (name)
        self.viewing_record()


#-------------------------------------------------------View Record-------------------------------------------------------------------------------------


    def ViewRecord(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, Select Record'

        old_name = self.tree.item(self.tree.selection())['text']
        old_id = self.tree.item(self.tree.selection())['values'][0]
        old_mobile = self.tree.item(self.tree.selection())['values'][1]
        old_email = self.tree.item(self.tree.selection())['values'][2]
        old_DateOfBirth = self.tree.item(self.tree.selection())['values'][3]
        old_DateOfJoining = self.tree.item(self.tree.selection())['values'][4]
        old_country = self.tree.item(self.tree.selection())['values'][5]
        old_state = self.tree.item(self.tree.selection())['values'][6]
        old_city = self.tree.item(self.tree.selection())['values'][7]
        old_zip = self.tree.item(self.tree.selection())['values'][8]

        self.edit_wind = Toplevel()
        self.edit_wind.title('Editing')

        Label(self.edit_wind, text = 'Name:', font=('arial 10 bold')).grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_name), state = 'readonly', font=('arial 15 bold')).grid(row = 0, column = 2)
        
        Label(self.edit_wind, text = 'ID:', font=('arial 10 bold')).grid(row = 1, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_id), state = 'readonly', font=('arial 15 bold')).grid(row = 1, column = 2)
        
        Label(self.edit_wind, text = 'Mobile:', font=('arial 10 bold')).grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_mobile), state = 'readonly', font=('arial 15 bold')).grid(row = 2, column = 2)
        
        Label(self.edit_wind, text = 'Email:', font=('arial 10 bold')).grid(row = 3, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_email), state = 'readonly', font=('arial 15 bold')).grid(row = 3, column = 2)
        
        Label(self.edit_wind, text = 'DateOfBirth:', font=('arial 10 bold')).grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_DateOfBirth), state = 'readonly', font=('arial 15 bold')).grid(row = 4, column = 2)
        
        Label(self.edit_wind, text = 'DateOfJoining:', font=('arial 10 bold')).grid(row = 5, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_DateOfJoining), state = 'readonly', font=('arial 15 bold')).grid(row = 5, column = 2)
        
        Label(self.edit_wind, text = 'Country:', font=('arial 10 bold')).grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_country), state = 'readonly', font=('arial 15 bold')).grid(row = 6, column = 2)
        
        Label(self.edit_wind, text = 'State:', font=('arial 10 bold')).grid(row = 7, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_state), state = 'readonly', font=('arial 15 bold')).grid(row = 7, column = 2)
        
        Label(self.edit_wind, text = 'City:', font=('arial 10 bold')).grid(row = 8, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_city), state = 'readonly', font=('arial 15 bold')).grid(row = 8, column = 2)
        
        Label(self.edit_wind, text = 'Zip:', font=('arial 10 bold')).grid(row = 9, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_zip), state = 'readonly', font=('arial 15 bold')).grid(row = 9, column = 2)

        self.edit_wind.mainloop()


def main():
    root = Tk()
    root.geometry("1350x750+0+0")
    root.title("Employee Dtailes")
    root.configure(background='blue')
    application = Detail (root)
    root.mainloop()


if __name__ == '__main__':
    main()
