import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading the csv to check whether the input matches the state in the csv, needed to covert to list to check if i in
# list

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()

    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    # After typing "exit" program stops and writes csv with pandas library
    if answer_state == "Exit":
        missing_states = [x for x in states if x not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
