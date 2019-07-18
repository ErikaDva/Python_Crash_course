# Chapter 3 Introducing lists
# Working through examples in the book
bicycles = ['trek', 'cannondale', 'red-line', 'specialized']
print (bicycles)
print (bicycles[0])
print (bicycles[0].title())
print (bicycles[-1])
print (bicycles[-2].title())
message = "My firs bicycle was a " + bicycles[0].title() + "."
print (message)

#Exercises
#3-1. Names
names = ['Maja', 'Maibritt', 'Emma', 'Rasa', 'Darius']
print (names[0])
print (names[1])
print (names[2])
print (names[3])
print (names[4])
print (names[-1])
print (names[-2])
print (names[-3])
print (names[-4])
print (names[-5])

#3-2. Greetings

message_2 = "Hello, " + names[0] + " are you ready to learn some Python?"
print (message_2)
message_3 = "Hello, " + names[3] + " are you ready to learn some Python?"
print (message_3)
message_4 = "Hello, " + names[4] + " are you ready to learn some Python?"
print (message_4)

#3-3. Your own list

transport_vehicles = ['bicycle', 'motorcycle', 'car', 'plane', 'helicopter']
print ("I would like to use a " + transport_vehicles[3] + " to go to work")
print ("I would like to own a Tesla " + transport_vehicles[2])

