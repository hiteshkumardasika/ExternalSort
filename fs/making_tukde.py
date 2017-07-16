# making tukde  
#import populate

size = 10
f_out = open("data.csv", "r")

f1 = open("data_0.csv","w+")
cnt = 0
while True:
    text = f_out.readline()
    f1.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f1.close()


f2 = open("data_1.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f2.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f2.close()

f3 = open("data_2.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f3.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f3.close()

f4 = open("data_3.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f4.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f4.close()

f5 = open("data_4.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f5.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f5.close()

f6 = open("data_5.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f6.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f6.close()

f7 = open("data_6.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f7.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f7.close()

f8 = open("data_7.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f8.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f8.close()

f9 = open("data_8.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f9.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f9.close()

f10 = open("data_9.csv","w")
cnt = 0
while True:
    text = f_out.readline()
    f10.write(text)
    cnt = cnt+1
    if cnt == size:
        break
f10.close()

f_out.close()

print("Done.")