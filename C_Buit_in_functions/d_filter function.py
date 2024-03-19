

numbers=[1,2,3,4,5,6,7,8,9,10]
evennumbers=filter(lambda x:x%2==0,numbers)
print(list(evennumbers))
fivenum=filter(lambda x:x<numbers[5],numbers)
print(list(fivenum))