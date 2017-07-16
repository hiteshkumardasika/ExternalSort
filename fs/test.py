# merging tukde

import sys

def function(value):
    if(value == 0):
        temp = int(f0.readline())
    elif(value == 1):
        temp = int(f1.readline())
    elif(value == 2):
        temp = int(f2.readline())
    elif(value == 3):
        temp = int(f3.readline())
    elif(value == 4):
        temp = int(f4.readline())
    elif(value == 5):
        temp = int(f5.readline())
    elif(value == 6):
        temp = int(f6.readline())
    elif(value == 7):
        temp = int(f7.readline())
    elif(value == 8):
        temp = int(f8.readline())
    elif(value == 9):
        temp = int(f9.readline())
    else:
        print("Something is seriously wrong!!! Khandare, you fucked up.")

    return (temp) 

f0 = open("sorted_0.csv","r")
f1 = open("sorted_1.csv","r")
f2 = open("sorted_2.csv","r")
f3 = open("sorted_3.csv","r")
f4 = open("sorted_4.csv","r")
f5 = open("sorted_5.csv","r")
f6 = open("sorted_6.csv","r")
f7 = open("sorted_7.csv","r")
f8 = open("sorted_8.csv","r")
f9 = open("sorted_9.csv","r")
f_out = open("sorted.csv","w")

count = [0]*10
val = [0]*10

for i in range(10):
    val[i] = function(i)

while True:    
    if(min(count) == 10):
        break

    for i in range(10):
        if(val[i] <= min(val)):
            f_out.write(str(val[i]))
            f_out.write("\n")
            count[i] = count[i]+1
            if(count[i] < 10):
                val[i] = function(i)
            else:
                val[i] = sys.maxsize
        
f0.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f_out.close()

print("Done.")