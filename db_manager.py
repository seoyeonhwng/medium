# -*- coding: utf-8 -*-

import traceback
import psycopg2
from psycopg2.extras import RealDictCursor, execute_values
from utils.config import HOST, DBNAME, USER, PWD

class DBManager():
    def __init__(self):
        self.conn = self.__connect()

    def teardown(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def __connect(self):
        return psycopg2.connect(host=HOST, dbname=DBNAME,
                                user=USER, password=PWD)

    def __read_query(self, query_filename):
        query = ''
        with open(query_filename, 'r') as query_file:
            query = query_file.read()

        return query

    def __execute(self, query):
        if not self.conn:
            self.conn = self.__connect()
        cur = self.conn.cursor(cursor_factory=RealDictCursor)

        try:
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            msg = traceback.format_exc()
            msg += '\n\n Query: \n' + query
            print(msg)
            cur.close()
            return None

        cur.close()
        return result
