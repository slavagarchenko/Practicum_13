import turtle as t

t.speed(0)


def circle(size):
    """Draw a filled circle with a green color.

    Args:
        size (float): the radius of the circle.
    """
    color = "green"
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def square(size):
    """Draw a filled square with a red color.

    Args:
        size (float): the length of each side of the square.
    """
    color = "red"
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def triangle(size):
    """Draw a filled equilateral triangle with a blue color.

    Args:
        size (float): The length of each side of the triangle.
    """
    color = "blue"
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    t.end_fill()


def ornament(rows, cols, size):
    """Draw a grid-based ornament pattern with repeating shapes.

    Args:
        rows (int): the number of rows in the grid.
        cols (int): the number of columns in the grid.
        size (float): the size parameter for the shapes 
    """
    spacing = size * 2.5
    start_x = -cols * spacing / 2
    start_y = rows * spacing / 2

    elements = [circle, square, triangle]

    for i in range(rows):
        for j in range(cols):
            t.penup()
            t.goto(start_x + j * spacing, start_y - i * spacing)
            t.pendown()

            element = elements[(i * cols + j) % 3]

            t.setheading(0)
            element(size)


rows = int(input("Введите количество строчек: "))
cols = int(input("Введите количество столбцов: "))
size = float(input("Введите размер для фигур: "))

ornament(rows, cols, size)

t.hideturtle()
t.done()
