import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
states_img = 'blank_states_img.gif'
turtle.addshape(states_img)
turtle.shape(states_img)
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
t = turtle.Turtle()
t.hideturtle()
t.penup()

while len(all_states) > 0:
    user_input = turtle.textinput(f"{len(data)-len(all_states)}/{len(data)} States Correct", "What's another state name?").capitalize()
    if user_input == 'Exit':
        new_data = pd.DataFrame(all_states, columns=['state'])
        new_data.to_csv('states_to_learn.csv')
        break
    elif user_input in all_states:
        all_states.remove(user_input)
        ans = data.query(f"state == '{user_input}'")[['x', 'y']]
        t.goto(set(ans.values[0]))
        t.write(f'{user_input}')

screen.exitonclick()