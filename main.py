import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
game_is_on = True

target_states = []
x = 0
while game_is_on:
    x += 1
    answer_state = screen.textinput(title=f"{x}/50 States Correct", prompt="What's another state name?").title()
    if x == 50:
        game_is_on = False
    data = pandas.read_csv("50_states.csv")
    list_of_states = data.state.to_list()
    print(list_of_states)

    if answer_state in list_of_states:
        target_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in target_states]

        data_new = pandas.DataFrame(missing_states, columns=["Missing States"])
        data_new.to_csv("Missing_states.csv", index=False)

        break
    print(target_states)





screen.exitonclick()
