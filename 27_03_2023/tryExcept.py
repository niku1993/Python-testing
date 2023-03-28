try:
    with open('testForReadWrite','r') as reader :
        reader.read()
        print('Test Successful')

except:
    print ("Somehow I reached this block because there is failure in try block")