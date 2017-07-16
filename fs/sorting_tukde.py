# sorting a tukda with insertion sort

def Insertion_Sort(list1):
    for i in range(1,len(list1)):
        x = list1[i]
        index = i
        while index > 0 and list1[index-1] > x:
            list1[index] = list1[index-1]
            index = index-1
        list1[index] = x
    return(list1)

arr = [1]*10
cnt = 0
for line in open("data_0.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_0.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_1.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_1.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_2.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_2.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_3.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_3.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_4.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_4.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_5.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_5.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_6.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_6.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_7.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_7.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_8.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_8.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

cnt = 0
for line in open("data_9.csv","r"):
    if line.strip():           
        n = int(line)
        arr[cnt] = n
        cnt = cnt+1

f_out = open("sorted_9.csv","w")
arr = Insertion_Sort(arr)
for i in range(cnt):
    f_out.write(str(arr[i]))
    f_out.write("\n")

f_out.close()

print("Done.")