# # import another_module
#
# from turtle import Turtle, Screen
#
# # print(another_module.another_variable)
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan1")
# timmy.forward(100)
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'
print(table)
