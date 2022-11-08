import random

# Print "Welcome to Python!"
print('Welcome to Python!')
# Print "This is a loop printing 5 times"
print('This is a loop printing 5 times')
for x in range(1, 6):
	print(f'x is: {x}')

# Use .choice and print f string "today is {}"
# Add print for Monday"It will be a long week!, Friday "Woohoo, time for the weekend!" and rest of the week "Not quite there yet."

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
	print('It will be a long week!')
elif day == 'Friday':
	print('Woohoo, time for the weekend!')
else:
	print('Not quite there yet.')
