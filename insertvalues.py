import sqlite3
conn = sqlite3.connect('company.db')

print("connected")


conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
            VALUES(1,'Andrew','Atom',21,200000.0,'Manager')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
             VALUES(2,'Martha','Anita',22,500000.0,'Secretary')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK) \
             VALUES(3,'Ariana','Grande',20,13400000.0,'CEO')");


conn.commit()

print("Successfully inserted values in Company1 table")

conn.close()