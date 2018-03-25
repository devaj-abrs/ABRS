#getting data from user
Id = input('enter your id: ')
print 'Which book would u like to  have :',Id
Book = input('enter book name: ')

#link up with sqlite3
import sqlite3
conn = sqlite3.connect(db_ABRS)   #establishing connection with the database 
                                    #file name db_file
c = conn.cursor
def read_from_db():                 #reading data from database

    location = input c.execute('"SELECT * FROM "ABRS.DB"  WHERE "book" = %S" %book')
    #fetch the value corresponding to the book name and store that in 'location' variable
    for row in c.fetch():           
        print(location)
    #split the values in location into X,Y & Z
    x,y,z = location.split(",")
