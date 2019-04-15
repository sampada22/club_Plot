import time
import math
import matplotlib.pyplot as plt 
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	"""create conenction to the SQLite database:
	:param db_file: database file
	:return: Connection object or None
	"""

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None

def create_data_Log(conn,data_Log):
	"""Create a new data log into the Distance_Data table
	:param conn:
	:param: data_Log
	:return:None
	"""
	#conn = sqlite3.connect("distance.db")
	try:
		sql = """INSERT INTO Distance_Data(time,data_X,data_Y,data_Yaw)
		         VALUES(?,?,?,?)"""
		curs = conn.cursor()
		#conn.commit()
		print("Comitted")
		curs.execute(sql,data_Log)
		print("Executed")
		#conn.close()
		#print("Closed")	
		return None
	except Error as e:
		print(e)
		print("Error from data log")
	return None


#fig = plt.figure() 
#ax = fig.add_subplot(111)
#fig.show()

#i = 0
#x,y = [],[]

def main():
    then = time.time()
    i = 0
    database = "distance.db"
    #create a database connection
    conn = create_connection(database)
    conn.commit()

    while True:
        now = time.time()
        data_T = now - then
        data_X = math.sin(i)
        data_Y = math.cos(i)
        data_Yaw = math.tan(i)
        i += 0.25

        with conn:
            data_Log = (int(data_T),int(data_X),int(data_Y),int(data_Yaw))
            create_data_Log(conn,data_Log)
        #x.append(i)
        #y.append(math.sin(i))
        #ax.plot(x,y,color = 'b')

        #fig.canvas.draw()
        #time.sleep(0.001)
        
if __name__ == '__main__':
    main()