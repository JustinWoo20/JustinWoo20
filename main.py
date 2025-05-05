import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
starting_money = 1000

def adjust_for_ace(cards_list):
    total = sum(cards_list)
    while total > 21 and 11 in cards_list:
        ace_index = cards_list.index(11)
        cards_list[ace_index] = 1
        total = sum(cards_list)
    return total

your_cards = ''
opponent_cards = ''

play = input("Would you like to play Blackjack?\n"
                    "Type 'y' for yes, or 'n' for no. ").lower()
play_or_not = True
if play == 'n':
    play_or_not = False


while play_or_not:
    bet = int(input(f"Your currently have ${starting_money}. Please bet $50, $100, $250, $500, or $1000.\n$"))
    print(f"You bet ${bet}.")
    your_cards = random.choices(cards, k=2)
    opponent_cards = random.choices(cards, k=1)
    your_total = adjust_for_ace(your_cards)
    opponent_total = adjust_for_ace(opponent_cards)
    print(f"Your cards: {your_cards}. Your total is {your_total}.")
    print(f"Your opponent's card: {opponent_cards}")

    hit_or_stay = True
    while hit_or_stay:
        hit_or_stay = input("Type 'y' to hit or 'n' to stay. ")
        if hit_or_stay == "y":
            new_card = random.choice(cards)
            your_cards.append(new_card)
            your_total = adjust_for_ace(your_cards)
            print(f"Your cards: {your_cards}. Your new total is {your_total}")
            if your_total > 21:
                print(f"You bust. Dealer wins")
                starting_money -= bet
                hit_or_stay = False
        elif hit_or_stay == "n":
            while opponent_total < 17:
                new_card = random.choice(cards)
                opponent_cards.append(new_card)
                opponent_total = adjust_for_ace(opponent_cards)
            print(f"Your opponent's cards: {opponent_cards}. Their total is {opponent_total}")
            hit_or_stay = False

    #Determine Winner
    if opponent_total < your_total <= 21:
        print("You win this round")
        starting_money += (bet * 2)
    elif opponent_total > 21:
        print("Dealer busts. You win!")
        starting_money += bet
    elif your_total == opponent_total:
        starting_money = starting_money
        print("You tie. You get your money back.")

    elif your_total < opponent_total <= 21:
        print("You lose, dealer wins!")
        starting_money -= bet
    print(f"You now have: ${starting_money}")
    if starting_money <= 0:
        print("You're out of money. Come back again!")
        play_or_not = False
    else:
        stop_playing = input("Would you like to play another hand? Type 'y' or 'n'\n")
        if stop_playing == "n":
            play_or_not = False
            print("Thanks for playing!")
