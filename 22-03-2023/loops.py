
greeting = 'Good Morning'
a=4

if a>2 and greeting == 'Morning':
    print('Condition matches')
else:
    print ('Condition do not match')
print ('If Else condition is complete')

# for loop

obj=[2,3,5,7,9]
for i in obj:
    print (i*2)

# sum of first five natural numbers

summation = 0
for j in range (1,6): #range(i,j) -- i to j-1
    summation = summation+j
print (summation)

print ("****************")

for k in range (1,10,2):
    print (k)

print("****************")

for m in range (10):
    print (m)
print ('$$$$$$$$$$$ While Loop $$$$$$$$$$$')
it=4
while it >1:
    print (it)
    it=it-1
print ('while loop execution is done')

print ('*** not 3 ***')
it=4
while it >1:
    if it !=3:
        print(it)
    it=it-1
print ('while loop execution is done')

print ('*** use continue and break ***')
it=10
while it >1:
    if it ==9:
        it=it-1
        continue
    if it==3:
        break
    print(it)
    it=it-1
print ('while loop execution is done')