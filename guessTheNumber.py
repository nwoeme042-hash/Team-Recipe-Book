import random
import time

gameOpt = "Yes"

while gameOpt == "Yes":
	for _ in range(183):
		randNum = random.randint(1, 100)

	playerGuess = int(input("Guess a number (1-100) (-1 to quit): "))

	while(playerGuess != randNum and playerGuess != -1):
		if playerGuess > randNum:
			print("Too High!")
		else:
			print("Too Low!")
		playerGuess = int(input("Guess a number (1-100) (-1 to quit): "))


	if playerGuess != -1:
		print(f"YOU WIN! The number was {randNum}.")
	else:
		print(f"Quitter! The number was {randNum}.")

	gameOpt = input("Do you want to play again? (Yes or No): ")



print("Game closing with no errors")
time.sleep(1.5)