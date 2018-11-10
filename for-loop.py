the_count =[1,2,3,4,5]
fruits =['aples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quaters']

#first kind of for loop through a list
for number in the_count:
    print("this is count ",number)

for fruit in fruits:
    print("A fruit of type ",fruit)

for i in change:
    print("i got ",i)

#we can also build lists
elements=[]

#range function to do 0 to 5 counts
for i in range(0,6):
    print ("adding %d to the list"%i)
    #append is a function that lists understand
    elements.append(i)

#printing list elements
for i in elements:
    print ("element was: ",i)
