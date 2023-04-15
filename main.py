import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

mydb = mysql.connector.connect(
    host = "cloud.mindsdb.com",
    user = os.environ.get("USER"),
    password = os.environ.get("PASSWORD"),
    port = "3306"
)

cursor = mydb.cursor()

cursor.execute('''SELECT response from mindsdb.alien_model Where author_username = "mindsdb" AND text= "how to be your best at every presentation"''')

for x in cursor:
    print(x)