import string
import turtle
import pandas

correct_states = []
screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


while len(correct_states) < 50:
    answer_state = string.capwords(screen.textinput(title = f"{len(correct_states)}/50 correct", prompt="What's another state's name?"))
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        map = data[data.state == answer_state]
        state_name.goto(int(map.x), int(map.y))
        state_name.write(answer_state)
        if answer_state not in correct_states:
            correct_states.append(answer_state)
            screen.update()





screen.exitonclick()