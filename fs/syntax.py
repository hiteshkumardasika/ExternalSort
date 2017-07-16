# Open a file
fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)
print(fo.read())
fo.close()
