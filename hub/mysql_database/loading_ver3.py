from datetime import datetime
import pymysql
import time
import serial
import random
import re

# Setup database connection
# Connect to the MySQL database
db = pymysql.connect(host="127.0.0.1", user="root", password="Angela040804!", db="DEMO2_0", autocommit=True)
cursor = db.cursor()

# Open the serial port
ser = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)

k = 1
while True:
    
    try:
        
        line = ser.readline()
        print(line)
        line = line.strip().decode()
        print(line)
        # Use a regular expression to match only lines with numeric data
        if re.match(r'^-?\d+$', line):
            if line:
                line = int(line)
                print(line)
                if line <= 2000:
                    # Parse the sensor value from the line of data
                    soil_moisture_0 = int(line)
                    soil_moisture_10 = int(line)
                    soil_moisture_20 = int(line)
                    update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(line)
                    for i in range(1, 4):
                        node_ID = i 
                        soil_temp_0 = random.uniform(15, 40)
                        soil_temp_10 = random.uniform(15, 40)
                        soil_temp_20 = random.uniform(15, 40)
                        ph_0 = random.uniform(4, 8)
                        ph_10 = random.uniform(4, 8)
                        ph_20 = random.uniform(4, 8)
                        light_intensity_0 = random.uniform(1, 100)

                        query = """INSERT INTO history_update 
                                (ID, update_time, node_ID, soil_temp_0, soil_temp_10, 
                                    soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20,
                                ph_0, ph_10, ph_20, light_intensity_0) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        values = (k, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0,
                                soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)

                        cursor.execute(query, values)
                        k += 1
            
    except ValueError as e:
        print(f"Error converting data to integer: '{line}'. Error: {e}")


    
    

