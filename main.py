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
    # if len(list_of_states) == 50:
    #     game_is_on = False
    if answer_state == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in target_states:
                missing_states.append(state)
        data_new = pandas.DataFrame(missing_states, columns=["Missing States"])
        data_new.to_csv("Missing_states.csv", index=False)

        break
    print(target_states)
    # t.write(arg=f"{answer_state}", align="center", font=("New Roman", 8, "bold"))

    # for name in name_state:
    #
    #     if answer_state == name:
    #         turtle.write(arg=f"{answer_state}", align="center", font=("New Roman", 8, "bold"))
    #         list_of_states.append(answer_state)
    #         # state_name = data[data.state == answer_state]
    #         # x_value = data.loc[f"{answer_state}", "x"]
    #         # print(x_value)
    #
    #         x_value = data.loc[data.state == answer_state, "x"].values[0]
    #         y_value = data.loc[data.state == answer_state, "y"].values[0]
    #         turtle.goto(x=x_value, y=y_value)
    #

    #         # the_state = data[data.state == answer_state]
    #         # x_value = the_state.x.value()
    #         # print(x_value)
    #         # y_value = the_state.y
    #         print(x_value, y_value)
    #         # turtle.write(arg=f"{answer_state}", align="center", font=("New Roman", 8, "bold"))
    #         # turtle.goto(x_value, y_value)
    #




screen.exitonclick()
