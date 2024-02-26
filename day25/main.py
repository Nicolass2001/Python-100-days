import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)
csv = pd.read_csv("50_states.csv")

game_is_on = True
allready_guessed = []
while len(allready_guessed) < 50:

    answer_state = screen.textinput(title=f"{len(allready_guessed)}/50 Guess the State", prompt="What's another state's name?").title()

    state_guessed = csv[csv.state == answer_state]

    if answer_state == "Exit":
        break

    if answer_state not in allready_guessed:
        if not state_guessed.empty:
            new_state = t.Turtle()
            new_state.penup()
            new_state.hideturtle()
            new_state.setpos(state_guessed.x.item(), state_guessed.y.item())
            new_state.write(state_guessed.state.item(), align="center")
            allready_guessed.append(answer_state)

    
states_missing = list(set(csv.state.to_list()) - set(allready_guessed))

df = pd.DataFrame(states_missing, columns=['states_missing'])

df.to_csv("states_missing.csv")