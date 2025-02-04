import numpy as np

hi = 1.2
vi = 5.4 # known variables
g = 9.8

t = float(input("Please enter a time: ")) # asking user for time

v = vi - t*g
h = hi + vi*t - 1/2*g*t**2 # calculating based on user given time

print("The height at time t is: {:.1f}".format(h)) # printing calculated answers
print("The velocity at time t is: {:.1f}".format(v))