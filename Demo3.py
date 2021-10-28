# Чреь класовете правим наши собствени функционалности
# Например чрез списък: в него добавяме само елементите, които искаме
# A class is used to create individual instances of object
# Класа е тип, който създаваме, т.е. собствен наш
#The clas is an blueprint that defines the nature of a future object

print(isinstance(5,int))
print(isinstance(5.5,int))
print(isinstance(5,object))
print(isinstance(int,object))



ll2 = [5]
ll=[1,2,3]
print(ll)
ll.append(-1)
ll.extend(ll2)
print(ll)