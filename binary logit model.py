import math
def utility(a, w, r, c):
    u = (-0.356*a)-(0.002*w)-(0.005*r)-(0.004*c)
    exponent_of_utility = math.exp(u)
    print(u)
    print(exponent_of_utility)
utility(2,0,36,82)


