# Import art, random, and game_data
# Make random number function to get people from game_data
# Make while loop
# If incorrect give 'you lose' message with final score
# String that displays dictionary information
# Function comparing followers that moves B to A
# On 1st round don't need current score
# print(f"{person["name"]}, {person["description"]}, from {person["country"]}")
# Fix score bug, can either find a way to
# Put everything in a loop with the variable 'continue_playing'

import random
import art
import game_data

player_score = 0

def game(guess):
    r'''The main function that determines if the player is correct or not'''
    global game_over
    current_score = player_score
    if guess == "A" and person_A["follower_count"] > person_B["follower_count"]:
        current_score += 1
        print(f"Correct! Current score: {current_score}")
        game_over = False
    elif guess == "A" and person_A["follower_count"] < person_B["follower_count"]:
        print(art.you_lose)
        print(f"Final score: {current_score}")
        game_over = True
        current_score = 0
    elif guess == "B" and person_A["follower_count"] < person_B["follower_count"]:
        current_score += 1
        game_over = False
        print(f"Correct! Current score: {current_score}")
    elif guess == "B" and person_A["follower_count"] > person_B["follower_count"]:
        print(art.you_lose)
        print(f"Final score: {current_score}")
        game_over = True
        current_score = 0

    return current_score

# Get two random people to start a new game
continue_playing = True
while continue_playing:
    person_A, person_B = random.sample(game_data.data, 2)
    print(art.logo)
    print(f"Person A: {person_A["name"]}, {person_A["description"]}, from {person_A["country"]}")
    print(art.vs)
    print(f"Person B: {person_B["name"]}, {person_B["description"]}, from {person_B["country"]}")
    game_over = False

    # Get the player input
    choice = input("Who has more followers: Type \"A\" or \"B\": ").upper()
    while choice not in ["A", "B"]:
        choice = input("Invalid input. Please type 'A' or 'B'.").upper()
    player_score = game(guess=choice)
    if game_over:
        one_more_round = input('Would you like to try again? Type "y" or "n": ')
        if one_more_round == "n":
            continue_playing = False

    while not game_over:
        person_A = person_B
        print(art.logo)
        print(f"Person A: {person_A["name"]}, {person_A["description"]}, from {person_A["country"]}")
        print(art.vs)
        person_B = random.choice(game_data.data)
        while person_B == person_A:
            person_B = random.choice(game_data.data)
        print(f"Person B: {person_B["name"]}, {person_B["description"]}, from {person_B["country"]}")
        choice_loop = input("Who has more followers: Type \"A\" or \"B\": ").upper()
        while choice_loop not in ['A', 'B']:
            choice_loop = input('Invalid input. Please type "A" or "B".').upper()
        player_score = game(guess=choice_loop)
        if game_over:
            one_more_round = input('Would you like to try again? Type "y" or "n": ')
            if one_more_round == "n":
                continue_playing = False








