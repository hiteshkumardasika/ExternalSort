# creating data
import sys
import random

size = 100

fo = open("data.csv", "w")

for i in range(size):
    fo.write(str(random.randint(1,sys.maxsize)))
    fo.write(" \n ")
fo.close()

print("Done.")