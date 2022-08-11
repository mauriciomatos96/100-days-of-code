import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# my solution

# user_answer = turtle.Turtle()
# user_answer.hideturtle()
# user_answer.penup()
#
# data = pd.read_csv("50_states.csv")
#
# all_states = data.state.to_list()
# attempts = 1
# while attempts <= 50:
#     answer_state = screen.textinput(title=f"Guess the state, attempt: {attempts}/50", prompt="What's another state's name")\
#         .title()
#     for name in all_states:
#         if answer_state == name:
#             state = (data[data.state == name])
#             user_answer.goto(int(state.x), int(state.y))
#             user_answer.write(answer_state)
#     attempts += 1

# screen.exitonclick()

# my solution

# angela solution

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = (data[data.state == answer_state])
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)