import turtle

image = "blank_states_img.gif"
screen = turtle.Screen()

screen.addshape(image)
turtle.shape(image)


# Getting the coordinates of where I am clicking on US map. All data saved in 50_states.csv
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

# Gives us screen open when we click.
turtle.mainloop()
