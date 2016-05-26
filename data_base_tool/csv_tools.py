"""
module use to handle the data IO with postgresql databaase
"""
import psycopg2
import os
import csv

def connect_to_db(dbname):
    db_basic = psycopg2.connect("dbname=%s"%(dbname))
    conn = db_basic.cursor()
    return [db_basic,conn]

#you have to create the table first
def push_csv_todb(f,dbname,table_name,header = True):
    
    insert = """insert into %s values%s
    """
    db,conn = connect_to_db(dbname)
    value = ''
    with open(f, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        if header : 
            fileReader.next()
        first_row = fileReader.next()
        value+='('+first_row[0]+')'

        for row in fileReader:
            value+=',('+row[0]+')'
        conn.execute( insert%(table_name,value) )
        db.commit() 

if __name__ == "__main__":
    push_csv_todb('/Users/pinghuanliu/data_dump/Category.csv', 'duplicate_ad','category')
    