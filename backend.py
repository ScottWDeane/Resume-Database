import sqlite3

#initial connection to the database
def connect():
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS resumeTable (id INTEGER PRIMARY KEY, companyName text, jobTitle text, wantedReq text, address text, salary integer, avgRent integer, distance integer, status text)")
    conn.commit()
    conn.close()

def insert(companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status):
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO resumeTable VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM resumeTable")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(companyName="", jobTitle="", wantedReq="", address="", salary="", avgRent="", distance="", status=""):
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM resumeTable WHERE companyName=? OR jobTitle=? OR wantedReq=? OR address=? OR salary=? OR avgRent=? OR distance=? OR status=?", (companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM resumeTable WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status):
    conn=sqlite3.connect("rentMapRaw.db")
    cur=conn.cursor()
    cur.execute("UPDATE resumeTable SET companyName=?, jobTitle=?, wantedReq=?, address=?, salary=?, avgRent=?, distance=?, status=? WHERE id=?", (companyName, jobTitle, wantedReq, address, salary, avgRent, distance, status, id))
    conn.commit()
    conn.close()

connect()
#insert(60000, 3500, "1600 Holloway Ave, San Francisco, CA 94132")
