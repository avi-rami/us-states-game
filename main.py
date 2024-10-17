from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

state_text = Turtle()
state_text.penup()
state_text.speed("fastest")
state_text.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_states = 0
guessed_states = []

answer_state = screen.textinput(title="0/50 States Correct", prompt="Name a US state").title()
game_is_on = True
while len(guessed_states) < 50:
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        learn = {"States to Learn": missing_states}
        states_to_learn = pandas.DataFrame(learn)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_text.setpos(state_data.x.item(),state_data.y.item())
        state_text.write(answer_state)
        correct_states += 1
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state name?").title()


screen.exitonclick()
