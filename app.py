from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10_db_d7cl_user:CA2aFN2fD0vghFJFPBSCOx4A9kWZdR46@dpg-cl3anqauuipc738ae48g-a/lab10_db_d7cl")
    conn.close()
    return "Database Connection Successful"
