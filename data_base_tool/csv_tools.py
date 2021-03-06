"""
module use to handle the data IO with postgresql databaase
"""
import psycopg2
import csv
from sys import *
import progress_bar

N_VALUE=1000

def connect_to_db(dbname):
    db_basic = psycopg2.connect("dbname=%s"%(dbname))
    conn = db_basic.cursor()
    return [db_basic,conn]

#-------------------------------------------------------------
def add_row_to_sqlValue(row,n_entry,value,first_quot =',(' ):
    value+=first_quot +row[0]
    for i in xrange(1,n_entry):
        value+=','+row[i]
    value+=')'
    return value

def get_schema(table_name,db,conn):
    #query = """SELECT column_name,data_type FROM information_schema.columns WHERE table_name ='%s'
    #"""
    query = """SELECT data_type FROM information_schema.columns WHERE table_name ='%s'
    """
    
    conn.execute(query%(table_name))
    schema = conn.fetchall()
    return schema

def text_helper(row,i):
    row[i]='\''+row[i]+'\''
    
def first_row_helper(fileReader,texts,n_entry,current_row,total_row):
    first_row = fileReader.next()
    [text_helper(first_row,i) for i in texts]
    current_row+=1
    progress_bar.update_progress(current_row/total_row)
    value = add_row_to_sqlValue(first_row,n_entry,'','(')
    return [current_row,value]
    
    
    
def push_helper(fileReader,texts,n_entry,current_row,total_row): 
     
    #for row in fileReader:
        value = ''
        try:
            re = first_row_helper(fileReader,texts,n_entry,current_row,total_row)
            current_row = re[0]
            value = re[1]
            #print 'push helper first value: '+value
            for i in xrange(N_VALUE) : 
                row = fileReader.next()
                current_row+=1
                progress_bar.update_progress(current_row/total_row)
                [text_helper(row,i) for i in texts]
        #             for i in texts:
        #                 row[i]='\''+row[i]+'\'' 
                value = add_row_to_sqlValue(row,n_entry,value)
            #print 'push helper 2 value: '+value
            return [current_row,value]
        except StopIteration:
            current_row = -1
            return [current_row,value]

       
            


#you have to create the table first
def push_csv_todb(f,dbname,table,header = True):
    
    insert = """insert into %s values%s
    """

    db,conn = connect_to_db(dbname)
    schema = get_schema(table,db,conn)
    l_schema = len(schema)
    texts = [i for i in xrange(l_schema) if schema[i][0] == 'text']
 
    value = ''
    with open(f, 'rb') as csvfile:
        fileReader_count = csv.reader(csvfile, delimiter=',', quotechar='|')
        total_row = sum(1 for row in fileReader_count)
        
        fileReader = csv.reader(open(f, 'rb'), delimiter=',', quotechar='|')
        
        if header : 
            total_row-=1
            next(fileReader)
        first_row = fileReader.next()
        n_entry = len(first_row)
        if l_schema != n_entry : raise ValueError('The input file does not match the table schema')
#         for i in texts:
#                 first_row[i]='\''+first_row[i]+'\'' 
        [text_helper(first_row,i) for i in texts]
        value = add_row_to_sqlValue(first_row,n_entry,value,'(')
        total_row-=1
        conn.execute( insert%(table,value) )
        db.commit() 
        print 'start parsing the file'
        current_row = 0.0
        while(current_row>=0):
            
            re = push_helper(fileReader,texts,n_entry,current_row,total_row)
            current_row = re[0]
            value = re[1]
            #print insert%(table,value)
            conn.execute( insert%(table,value) )
            db.commit() 
        
        print 'finish file parsing'
        #print insert%(table,value)   

#f: input csv file
#db: target database
#table: target table
if __name__ == "__main__":
    f=argv[1]
    db=argv[2]
    table = argv[3]
    
    push_csv_todb(f, db,table)
    #db,conn = connect_to_db(db)
    #print get_schema(table,db,conn)
    
    
