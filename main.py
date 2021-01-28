# 100 Days of Code
# Guess the State

import turtle
import pandas

FONT = ("Courier", 11, "normal")

screen = turtle.Screen()
screen.title("Stop sucking at Geography")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
location_x = data.x.to_list()
location_y = data.y.to_list()
guessed_states = []

game_is_on = True
score = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score} / 50 Correct", prompt="Enter a State's name").title()

    if answer_state == "Quit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto((int(state_data.x), int(state_data.y)))
        t.write(answer_state, font=FONT)
        score += 1
        guessed_states.append(answer_state)
