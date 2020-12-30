#Travel_cost_ratio
# X9 = Fare by public transport
# X10 = Cost of petrol
# X11 = Cost of oil
# X12 = Cost of parking
# X13 = Average car occupancy

Travel_cost_ratio =  lambda x9, x10, x11, x12, x13 :(x9/((x10 + x11 + (0.5 * x12))/x13))
b = Travel_cost_ratio(1, 1, 1, 2,3)
print(b)