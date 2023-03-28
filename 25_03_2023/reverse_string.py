class reverse:
   def rev (self, a) :
       b=-1
       rev=""
       for i in a:
           rev+=a[b]
           b=b-1
       return rev
a=reverse()
print (a.rev('My name is Nitish'))
