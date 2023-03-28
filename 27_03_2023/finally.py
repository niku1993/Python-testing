try:
    with open('testForRead','r') as reader :
        reader.read()
        print('Test Successful')

except Exception as e:
    print (e ,"My message")

finally:
    print("mar jaavan mit jaavan")