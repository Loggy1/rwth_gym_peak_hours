import os
import sys 
sys.path.append('..')
from globals import *

# List of all the weekdays
weekdays = os.listdir(path + '/db/')

def calculate_average():
    print("Calculating...")
    for i in weekdays:
        # List of all the days
        files = os.listdir(path + '/db/' + i)
        try:
            for j in range(10,23):
                # List of all the hours
                hours = os.listdir(path + '/db/' + i + '/' + str(j))
                for k in hours:
                    # Get all the values
                    db_file = open(path + '/db/' + i + '/' + str(j) + "/values.txt", 'r')
                    values = db_file.readlines()
                    db_file.close()

                    # calculate average vistors per hour
                    sum = 0
                    for l in values:
                        sum += int(l)
                    average = sum / len(values)
                    db_file = open(path + '/db/' + i + '/' + str(j) + "/average.txt", 'w')
                    db_file.write(str(average))
                    db_file.close()
        except:
            print("No Files")

def get_average(date_string):
    print("Plotting...")
    values = []
    files = os.listdir(path + '/db/' + date_string)
    for j in range(10,23):
        try:
            db_file = open(path + '/db/' + date_string + '/' + str(j) + "/average.txt", 'r')
            value = int(float(db_file.readline()))
            db_file.close()
            values.append(value)
        except:
            values.append(0)
    return values


