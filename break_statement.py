# Python program to demonstrate 
# break statement 

s = 'shristi'
# Using for loop 
for letter in s: 

	print(letter) 
	# break the loop as soon it sees 'i' 
	# or 's' 
	if letter == 'i' or letter == 's': 
		break

print("Out of for loop") 
print() 

i = 0

# Using while loop 
while True: 
	print(s[i]) 

	# break the loop as soon it sees 'i' 
	# or 's' 
	if s[i] == 'i' or s[i] == 's': 
		break
	i += 1

print("Out of while loop")
