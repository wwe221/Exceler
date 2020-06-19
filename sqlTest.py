import sqlite3
import sqlite3

# SQLite DB 연결
conn = sqlite3.connect("Yesan.db")
cur = conn.cursor()

global Yesan
global Pum
global Spend
Yesan = '''CREATE TABLE "Yesan" (
	"Team"	TEXT,
	"Busy"	TEXT,
	"Budget"	INTEGER,
	PRIMARY KEY("Team","Busy")
)'''
Pum = '''CREATE TABLE "Pum" (
	"Numb"	TEXT,
	"Team"	TEXT,
	"Busy"	TEXT,
	"Desc"	TEXT,
	"Budget"	INTEGER,
	PRIMARY KEY("Numb"),
	FOREIGN KEY("Busy") REFERENCES "Yesan"("Busy"),
	FOREIGN KEY("Team") REFERENCES "Yesan"("Team")
)'''
Spend = '''CREATE TABLE "Spend" (
	"Numb"	TEXT,
	"Date"	TEXT,
	"Pumnumb"	TEXT,
	"Subject"	TEXT,
	"Desc"	TEXT,
	"Prov"	INTEGER,
	"Tax"	INTEGER,
	FOREIGN KEY("Pumnumb") REFERENCES "Pum"("Numb"),
	PRIMARY KEY("Numb")
)'''

conn.close()

global printTable
def printTable(Table):
    print("Print "+Table)
    conn = sqlite3.connect("Yesan.db")
    cur = conn.cursor()
    sql = "select * from "+Table
    rows = cur.execute(sql)
    for row in rows:
        print(row)
    conn.close()

global makeTable
def makeTable(sql):
    conn = sqlite3.connect("Yesan.db")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def clearTable(Table):
    conn = sqlite3.connect("Yesan.db")
    cur = conn.cursor()
    sql = "delete from "+Table
    result = cur.execute(sql)
    conn.commit()
    conn.close()

#makeTable(Spend)
#clearTable("Spend")
#clearTable("Pum")
#printTable("Spend")

# conn = sqlite3.connect("Yesan.db")
# cur = conn.cursor()
# sql = "drop table Spend"
# rows = cur.execute(sql)
# conn.commit()
# conn.close()
# conn = sqlite3.connect("Yesan.db")
# cur = conn.cursor()
# sql = "select * from Spend"
# rows = cur.execute(sql)
# for row in rows:
#     sql2 ="select * from Pum where Numb= '"+row[2]+"'"
#     print(row)
#     row2 = cur.execute(sql2)
#     for tmp in row2:
#         print(tmp[1],tmp[2])
#         sql3 = "select * from Yesan where Team = ? And Busy = ?"
#         row3 = cur.execute(sql3,(tmp[1],tmp[2]))
#         for tmp2 in row3:
#             print(tmp2)
#     break







conn.close()