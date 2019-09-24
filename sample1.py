#without using pandas write a for loop that takes in the cars data set and gives the average mileage

import csv #adding csv library
total_miles = 0
cars_count = 0
with open('cars.csv') as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object) #this if statement checks for header and skips in calc
    for row in csv_reader_object: #iterating through csv to calculate total miles and num of cars
        float_mileage = float(row[3])
        total_miles += float_mileage
        cars_count += 1
#calculate average by dividing miles by cars
avg_miles = total_miles/cars_count
print("The average mileage in the data set is")
print(avg_miles) 