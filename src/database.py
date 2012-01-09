import sqlite3


class DataBase(object):

   # private dbPath = "/home/terah/git/pyProgramming/AddressBook/database"

    def __init__(self):

        self.conn = sqlite3.connect('/home/terah/git/pyProgramming/AddressBook/database')
        self.c = self.conn.cursor()


#    def __destructor__(self):
#
#        # Save (commit) the changes
#        conn.commit()
#
#        # We can also close the cursor if we are done with it
#        c.close()
#

    def getC(self):

        return self.c

    def getName(self):

        self.c.execute(''' SELECT FirstName, LastName
                FROM AddressBook ''')

    def getAddress(self):

        self.c.execute(''' SELECT Address
                FROM AddressBook ''')

    def getPhone(self):

        self.c.execute(''' SELECT Phone
                FROM AddressBook ''')

    def getEmail(self):

        self.c.execute(''' SELECT Email
                FROM AddressBook ''')

    def getNotes(self):

        self.c.execute(''' SELECT Notes
                FROM AddressBook ''')
    def getAll(self):
        self.c.execute(''' SELECT *
                FROM AddressBook ''')
