import turtle
import pandas

FONT = ("Trebuchet MS", 8, "bold")
WINNING_FONT = ("Trebuchet MS", 20, "bold")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()
correct_guesses = []



game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    # If already guessed skip over
    if answer_state == "Exit":
        missing_states = [missing_states = [states for states in state_list if states not in correct_guesses]]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to Learn")
        print(new_data)
        break

    if answer_state in correct_guesses:
        pass
    else:
        #Check if the guessed state is correct
        if answer_state in state_list:
            answer_data = state_data[state_data.state == answer_state]
            #Get state coordinates
            state_x = int(answer_data.x.values[0])
            state_y = int(answer_data.y.values[0])
            correct_guesses.append(answer_state)

    # Move the name
            writer = turtle.Turtle()
            writer.penup()
            writer.hideturtle()
            writer.goto(state_x, state_y)
            writer.write(arg= answer_state, font=FONT)

    if len(correct_guesses) == 50:
        wt = turtle.Turtle()
        wt.penup()
        wt.hideturtle()
        wt.write(arg="Congratulations! You got all 50 states!", font=WINNING_FONT)




