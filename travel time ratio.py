#travel_time_ratio
# x1 = time spent in public transport vehicle
# x2 = time spent changing between public transport vehicle
# x3 = time spent waiting for public transport vehicle
# x4 = time spent walking to the public transport origin
# x5 = time spent walking from public transport vehicle at destination
# x6 = time spent driving car
# x7 = time spent parking vehicle at destination
# x8 = time spent  walking from parked vehicle to destination


travel_time_ratio = lambda x1, x2, x3, x4, x5, x6, x7, x8 :((x1 + x2 + x3 + x4 + x5)/(x6 + x7 + x8))
a = travel_time_ratio (1,2,3,4,5,6,7,8)
print(a)