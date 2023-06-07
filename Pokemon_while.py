# Generate a random number between 1 and 151 to use as the Pokemon ID number
import random
import requests

print('''
,     ,_
           |`\    `;;,            ,;;'
           |  `\    \ '.        .'.'
           |    `\   \  '-""""-' /
           `.     `\ /          |`
             `>    /;   _     _ \ 
              /   / |       .    ;
             <  (`";\ ()   ~~~  (/_
              ';;\  `,     __ _.-'` )
                >;\          `   _.'
                `;;\          \-'
                  ;/           \ _
                  |   ,"".     .` \
                  |      _|   '   /
                   ;    /")     .;-,
                    \    /  __   .-'
                     \,_/-"`  `-'
''')

print(
	"Welcome to the Pokemon Top Trump Card Game!\n\n A game played in 4 rounds where you will be given a random pokemon to play against your opponent. Your score will be given at the end of the 4th round. Enjoy!\n")


def pokemon_random():
	pokemon_ID = random.randint(1, 151)
	# Using the Pokemon API get a Pokemon based on its ID number
	url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_ID)
	response = requests.get(url)
	pokemon_name = response.json()
	# Create a dictionary that contains the returned Pokemon's name, id, height and weight
	dictionary = {
		'name': pokemon_name['name'],
		'id': pokemon_name['id'],
		'height': pokemon_name['height'],
		'weight': pokemon_name['weight'],
		'hp': pokemon_name['stats'][0]['base_stat'],
		'attack': pokemon_name['stats'][1]['base_stat'],
		'defend': pokemon_name['stats'][2]['base_stat'],
	}
	return dictionary


your_score = 0
opponent_score = 0
user_input = input("How would you like to be called for this game?  ")
opponent_input = input("How would you like to name your opponent? ")

# print(pokemon_random())
# Loop in the main function:
for game in range(4):
	# Get a random Pokemon for the player and another for their opponent
	user = pokemon_random()
	opponent = pokemon_random()
	print(f'\nRound {game + 1}: Good Luck {user_input}!\n')

	print(f"Your pokemon is {user['name']}.")
	print(f"{opponent_input}'s pokemon is {opponent['name']}.")
	print()


	# Ask the user which stat they want to use (id, height or weight)

	def choice():
		choice_number = int(input("Choose which stat you would like to compete: 0 =id; 1 = height, 2 = weight, 3 = HP, 4 = attack and 5 = defence: "))
		if choice_number == 0:
			print(f"\nYou chose ID. Your ID for {user['name']} is {user['id']} and {opponent_input} is {opponent['id']} for {opponent['name']}")
		elif choice_number == 1:
			print(f"\nYou chose height. Your height for {user['name']} is {user['height']} and {opponent_input} is {opponent['height']} for {opponent['name']}")
		elif choice_number == 2:
			print(f"\nYou chose weight. Your weight for {user['name']} is {user['weight']} and {opponent_input} is {opponent['weight']} for {opponent['name']}")
		elif choice_number == 3:
			print(f"\nYou chose Hp. Your HP for {user['name']} is {user['hp']} and {opponent_input} is {opponent['hp']} for {opponent['name']} ")
		elif choice_number == 4:
			print(f"\nYou chose Attack. Your attack for {user['name']} is {user['attack']} and {opponent_input} is {opponent['attack']} for {opponent['name']} ")
		elif choice_number == 5:
			print(f"\nYou chose Defence. Your defense for {user['name']} is {user['defend']} and {opponent_input} is {opponent['defend']} for {opponent['name']} ")
		else:
			print("Please choose a number between 0 and 5 for the next round.")
		return choice_number


	choice = choice()
	if choice == 0:
		if user['id'] > opponent['id']:
			your_score += 1
			print("You win!\n")
		elif user['id'] == opponent['id']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')
	if choice == 1:
		if user['height'] > opponent['height']:
			your_score += 1
			print("You win!\n")
		elif user['height'] == opponent['height']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')
	if choice == 2:
		if user['weight'] > opponent['weight']:
			your_score += 1
			print("You win!\n")
		elif user['weight'] == opponent['weight']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')
	if choice == 3:
		if user['hp'] > opponent['hp']:
			your_score += 1
			print("You win!\n")
		elif user['hp'] == opponent['hp']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')
	if choice == 4:
		if user['attack'] > opponent['attack']:
			your_score += 1
			print("You win!\n")
		elif user['hp'] == opponent['hp']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')
	if choice == 5:
		if user['defend'] > opponent['defend']:
			your_score += 1
			print("You win!\n")
		elif user['hp'] == opponent['hp']:
			print('It\'s a draw.\n')
		else:
			opponent_score += 1
			print('You loose!\n')

print()
if your_score > opponent_score:
	print(f"Congratualtions, you won! Your score is {your_score} and {opponent_input} score is {opponent_score}")
elif your_score == opponent_score:
	print(f"It\'s a tie between you and {opponent_input}. Your scores are {your_score}")
else:
	print(f"Sorry you lost, your score is {your_score} and {opponent_input} is {opponent_score}")
