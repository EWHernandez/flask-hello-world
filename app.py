from flask import Flask
import psycopg2

app = Flask(__name__)

#initial route, will be first page dipayed with no specified routing
@app.route('/')
def hello_world():
    return 'Hello, World!'

#testing extension to connecting to render_db
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    conn.close()
    return "Database Connection Successful"

#creates the basketball table
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

#Inserts provided info into basketball table
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

#queries data from table, returns formatted data
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

#clears the table from the render db
@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"


    
