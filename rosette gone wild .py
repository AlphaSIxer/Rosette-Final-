import turtle
t = turtle.Pen()
number_of_circles = int(turtle.numinput("number of circles",
                                        "how many circles in your rosette?", 30))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360/number_of_circles)
