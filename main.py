# import colorgram
import turtle as turtle_module
import random
roshi = turtle_module.Turtle()
turtle_module.colormode(255)
roshi.penup()
roshi.hideturtle()
color_list = [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75), (209, 87, 66), (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]
# rgb = []
# colors = colorgram.extract('img3.jpg', 120)
roshi.speed("fastest")
roshi.setheading(225)
roshi.forward(300)
roshi.setheading(0)
dots = 100

for count in range(1, dots + 1):
    roshi.dot(20,random.choice(color_list))
    roshi.forward(50)
    if count % 10 == 0:
        roshi.setheading(90)
        roshi.forward(50)
        roshi.setheading(180)
        roshi.forward(500)
        roshi.setheading(0)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r, g, b)
#     rgb.append(new)
#
# print(rgb)



screen = turtle_module.Screen()
screen.exitonclick()


