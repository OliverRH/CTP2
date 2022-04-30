from sql_connector import *
from datetime import datetime

movement = True #Temporary value for movement variable
while True: #While loops runs forever
    now = datetime.now() # current date and time
    if 0 <= now.hour < 9 or 22 <= now.hour <= 23: #The system must be active between 22:00 and 9:00. (From 0:00 to 8:59 and 22:00 to 23:59) The system must automatically turn on/off when necessary
        #print(now.strftime("%Y-%m-%d %H:%M:%S")) #prints the current date and time, but commented our due to high system usage.
        if movement == True: #If movement is True, then insert date and time into the database.
            insert_sql() #Function from sql_connector.py. Inserts the date and time into the database and prints the date and time