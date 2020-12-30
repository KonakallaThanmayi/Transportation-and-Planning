# travel_service_ratio
# x2 = time spent changing between public transport vehicle
# x3 = time spent waiting for public transport vehicle
# x4 = time spent walking to the public transport origin
# x5 = time spent walking from public transport vehicle at destination
# x7 = time spent parking vehicle at destination
# x8 = time spent  walking from parked vehicle to destination

travel_service_ratio = lambda x2,x3, x4, x5, x7, x8 : ((x2 + x3 + x4 + x5)/(x7 + x8))
c = travel_service_ratio()
print(c)