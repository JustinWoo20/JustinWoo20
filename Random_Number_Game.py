import random
import art
print(art.logo)
keep_playing = True
print("Welcome to Guess the Number!\n")
def play_game(challenge_number, remaining_lives):
    """This function will handle the main game"""
    while remaining_lives > 0:
        choice = int(input("Please choose a number: "))
        if choice > challenge_number:
            remaining_lives -= 1
            print("Your guess is too high.")
        elif choice < challenge_number:
            remaining_lives -= 1
            print("Your guess is too low.")
        else:
            print(f"Congratulations! I was thinking of {challenge_number}.")
            return  # end the function if correct
        if remaining_lives != 0:
            print(f"You have {remaining_lives} chances remaining.")
        if remaining_lives == 0:
            print(f"Game Over! The correct number was: {challenge_number}")



while keep_playing:
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose the difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        starting_lives = 10
    else:
        starting_lives = 5
    print(f"You have {starting_lives} chances remaining.")
    random_number = random.choice(range(1, 101))
    #print(random_number) #Uncomment to debug
    play_game(challenge_number=random_number, remaining_lives=starting_lives)

    one_more_time = input("Would you like to keep playing? Type 'y' or 'n': ")
    if one_more_time == "y":
        print("\n" * 20)
        print(art.logo)
    elif one_more_time == 'n':
        keep_playing = False











