import json

import psycopg2, sql_queries, os, hashlib, requests
from datetime import datetime

NETFLIX_BASE_URL = 'https://gateway.marvel.com:443'

PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
TS = '1234'
HASH = hashlib.md5(str(TS+PRIVATE_KEY+PUBLIC_KEY).encode('utf').strip()).hexdigest()



def get_connection():
    conn = psycopg2.connect(user='admin', host='127.0.0.1', port='5432', database='marvel_db')
    return conn

conn = get_connection()

def _create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_queries.CREATE_TABLE_CHARACTERS)
        conn.commit()
        print("Table create successfully")
    except Exception as e:
        print(f"Error: {e}")

def _get_characters():
    params = dict(ts=TS, apikey=PUBLIC_KEY, hash=HASH)
    response = requests.get(url=f"{NETFLIX_BASE_URL}/v1/public/characters", params=params)
    if response.status_code == 200:
        response_body = json.loads(response.text)
        if response_body.get("data", {}).get("results"):
            for character in response_body.get("data", {}).get("results"):
                insert_into_db(
                    id=character.get('id', 0),
                    name=character.get('name', ''),
                    description=character.get('description', ''),
                    modified=datetime.strptime(character.get('modified'), '%Y-%m-%dT%H:%M:%S%z'))

def insert_into_db(id, name, description, modified):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_queries.INSERT_INTO_CHARACTERS, (id, name, description, modified))
        conn.commit()
        cursor.close()
        print(f"The record was added to DB")
    except Exception as e:
        print(f"Can not insert data into table: {e}")



if __name__ == '__main__':

    _create_tables(conn=conn)
    _get_characters()
