# file = open('testForReadWrite')

# print (file.read())
# print (file.readline())

#WAP line by line using readline method

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

#WAP line by line using readlines method

# for line in file.readlines():
#     print (line)

# file.close()

#another way to read file from txt file, in this option we don't need to close the file


#read the file and store all the lines in list
#reverse the list
#write the reversed list back to the file
# use 'w' for write mode and 'r' for read mode
with open('testForReadWrite', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('write', 'w') as writer:
        for line in reversed(content):
            writer.write(line)