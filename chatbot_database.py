import sqlite3
import json
from datetime import datetime

timeframe = '2015_02'


sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))

c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, 
              comment_id TEXT UNIQUE, 
              parent TEXT ,
              comment TEXT,
              subreddit TEXT,
              unix INT,
              score INT)""")
    

# def display_file_content(file_path):
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)  # Display content in the console


def format_data(data):
    data = data.replace("\n"," newlinechar " ).replace("\r", " newlinechar ").replace('"',"'")
    return data


def find_parent(pid):
    try:       
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else:
            return False
        
    except Exception as e:
        print("find parent", e)
        return False
        
if __name__ == "__main__":
    create_table()
    row_counter = 0
    paired_rows = 0
    with open("/home/muhammad/Documents/python project chatbot/RC_2015_02", "r", buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads()
            parent_id = row['parent_id']
            body = format_data(row['body'])
            score = row["score"]
            subreddit = row["subreddit"]
            


            parent_data = find_parent(parent_id)