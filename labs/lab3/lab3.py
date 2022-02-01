"""
Christopher Morales
lab3.py

Problem: To create a program that calculate and output the average number of vehicles
traveled down each road per day as well as the total number of
vehicles and the average number of vehicles for all the roads.

Certification of Authenticity:
I certify that this assignment is my own work.
"""


def traffic():
    total_number_of_vehicles = 0 # total number of cars in total
    roads_surveyed = eval(input("How many roads were surveyed?"))

    for roads_surveyed in range(roads_surveyed):
        print("How many days was road", roads_surveyed + 1, "surveyed")
        days_road_is_surveyed = eval(input(""))

        cars_traveled_on_day = 0 # total number of cars per road

        total_number_of_vehicles += cars_traveled_on_day + cars_traveled_on_day

        for cars_traveled in range(days_road_is_surveyed):
                print("How many cars traveled on day", cars_traveled + 1, "?")
                cars_traveling = eval(input(""))
                cars_traveled_on_day = cars_traveled_on_day + cars_traveling
                total_number_of_vehicles = total_number_of_vehicles + cars_traveling

        print("Road", roads_surveyed + 1, "average vechiles per day:", cars_traveled_on_day / days_road_is_surveyed)

    print("Total number of vehicles traveled on all roads:", total_number_of_vehicles)
    print("Average number of vehicles per road:", round(total_number_of_vehicles / (roads_surveyed + 1)))

traffic()