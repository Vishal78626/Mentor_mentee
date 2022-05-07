#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="root",
    password="linux",
    host="localhost",
    database="mentormentee")
cur = conn.cursor() 

#retrieving information 
# some_name = "Kiran" 
cur.execute("SELECT MenteeID FROM Mentee where MenteeID=1")
#  WHERE name=?", (some_name,)) 

for MenteeID in cur: 
    print(f"MenteeID: {MenteeID}")
    
# #insert information 
# try: 
#     cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB")) 
# except mariadb.Error as e: 
#     print(f"Error: {e}")

# conn.commit() 
# print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()