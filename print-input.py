print ("hello world") # A comment, for information
print ("hens",25+30/6)

cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers / cars_driven

print("there are", cars, "cars available.")
print("there are only", drivers, "drivers available.")

my_name='deser storm'
my_age='21' #years
my_height=70 #inches
my_weight=60 #kgs

print ("let's talk about %s."%my_name)
print ("he's %d inches tall."%my_height)
print("he's %d kgs heavy"%my_weight)
print("sum of my height and weight is %d"%(my_height+my_weight))

print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10) # print * 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)

formatter="%r %r %r %r"
print (formatter %(1,2,3,4))

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the days: ", days)
print ("Here are the months: ", months)

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(fat_cat)

age=input("how old are you")
print("your age is",age)
