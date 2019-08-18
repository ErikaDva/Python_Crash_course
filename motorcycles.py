# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print (motorcycles)

# Appending elements to the end of a list
motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print (motorcycles_2)
print (motorcycles)

motorcycles_2.append('kawasaki')
print (motorcycles_2)

motorcycles_3 = []
motorcycles_3.append('kawasaki')
motorcycles_3.append('ducati')
motorcycles_3.append('KTM')
print (motorcycles_3)

# Inserting elements into a list
motorcycles_4 = ['honda', 'yamaha', 'suzuki']
motorcycles_4.insert(0, 'ducati')
print (motorcycles_4)

# Removing element from a list
motorcycles_5 = ['honda', 'yamaha', 'suzuki']
print (motorcycles_5)
del motorcycles_5[0]
print (motorcycles_5)
del motorcycles_5[1]
print (motorcycles_5)

# Removing an item using the pop() method
motorcycles_6 = ['honda', 'yamaha', 'suzuki']
print (motorcycles_6)
popped_motorcycle = motorcycles_6.pop()
print (motorcycles_6)
print (popped_motorcycle)

motorcycles_7 = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles_7.pop()
print ("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping items from any position in a list
motorcycles_8 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles_8.pop(0)
print ("The first motorcycle I owned was a " + first_owned + ".")

# Removing item by value
motorcycles_9 = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles_9)
motorcycles_9.remove('ducati')
print (motorcycles_9)
# giving a reason
motorcycles_10 = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles_10)
too_expensive = 'ducati'
motorcycles_10.remove(too_expensive)
print (motorcycles_10)
print ("\nA " + too_expensive.title() + " is too expensive for me.")

#Exercises
#3-4. Guest list
guest_list = ['Maja', 'Maibritt', 'Emma']
print ("Dear " + guest_list[0] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[1] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[2] + ", you are invited to my dinner party.")
#3-5. Changing guest list
guest_list = ['Maja', 'Maibritt', 'Emma']
print (guest_list[2] + " is not able to attend the dinner party.")
guest_list[2] = 'Rasa'
print (guest_list)
print ("Dear " + guest_list[0] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[1] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[2] + ", you are invited to my dinner party.")
#3-6. More guests
guest_list = ['Maja', 'Maibritt', 'Rasa']
print ("I have found a bigger dinner table so extra invites were sent to three people")
guest_list.insert(2,'Darius')
guest_list.insert(0,'Sarunas')
guest_list.append('Julia')
print (guest_list)
print ("Dear " + guest_list[0] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[1] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[2] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[3] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[4] + ", you are invited to my dinner party.")
print ("Dear " + guest_list[5] + ", you are invited to my dinner party.")
#3-7. Shrinking guest list
print ("The bigger dinner table won't arrive in time so I can only invite two people")
guest_list = ['Sarunas', 'Maja', 'Maibritt', 'Darius', 'Rasa', 'Julia']
guest_6 = guest_list.pop(5)
print ("Dear " + guest_6 + ", I am sorry I can't invite you to the dinner.")
guest_5 = guest_list.pop(4)
print ("Dear " + guest_5 + ", I am sorry I can't invite you to the dinner.")
guest_4 = guest_list.pop(3)
print ("Dear " + guest_4 + ", I am sorry I can't invite you to the dinner.")
guest_3 = guest_list.pop(2)
print ("Dear " + guest_3 + ", I am sorry I can't invite you to the dinner.")
print (guest_list)
print ("Dear " + guest_list[0] + ", you are still invited to the dinner.")
print ("Dear " + guest_list[1] + ", you are still invited to the dinner.")
del guest_list[1]
del guest_list[0]
print (guest_list)


