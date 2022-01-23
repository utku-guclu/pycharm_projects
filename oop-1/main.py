# from turtle import Turtle, Screen
# import another_module
# jack = Turtle()
# my_screen = Screen()
#
# print(jack, my_screen.canvheight)
# jack.shape("turtle")
# jack.color("coral")
# jack.forward(100)
# my_screen.exitonclick()
#
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmender", "Fire"])

table.align = "l"
print(table)

