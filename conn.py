import sqlite3
import os 

pastaApp = os.getcwd()

cnxn = sqlite3.connect(fr"{pastaApp}\pythonsqlite.db", check_same_thread=False)

cursor = cnxn.cursor()
