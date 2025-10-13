import turtle as t

t.speed(0)


def triangle(p1, p2, p3, color):
    """
    Draw a filled triangle.

    Args:
        p1 (tuple): First point (x, y) coordinates.
        p2 (tuple): Second point (x, y) coordinates.
        p3 (tuple): Third point (x, y) coordinates.
        color (str): Fill color of the triangle.

    Returns:
        None
    """
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)
    t.end_fill()


def square(x, y, size, color1, color2):
    """
    Draw a square composed of two triangles.

    Args:
        x (float): X-coordinate of the bottom-left corner.
        y (float): Y-coordinate of the bottom-left corner.
        size (float): Side length of the square.
        color1 (str): Color of the first triangle.
        color2 (str): Color of the second triangle.

    Returns:
        None
    """
    bottom_left = (x, y)
    bottom_right = (x + size, y)
    top_right = (x + size, y + size)
    top_left = (x, y + size)

    triangle(bottom_left, bottom_right, top_right, color1)
    triangle(bottom_left, top_right, top_left, color2)


def pattern():
    colors = [
        'lightblue', 'blue', 'blue',
        'lightblue', 'lightblue',
        'white', 'white',
        'lightblue', 'lightblue'
    ]
    size = 80
    rows = 3
    cols = 3
    i = 0
    j = 1
    for row in range(rows):
        for col in range(cols):
            x = -cols * size // 2 + col * size
            y = rows * size // 2 - row * size
            square(x, y, size, colors[i], colors[j])

            if i == 8:
                i = 2
            else:
                i += 2
            if j == 7:
                j = 1
            else:
                j += 2

    i = 0
    j = 1

    for col in range(cols):
        for row in range(rows):
            x = -cols * size // 2 + col * size
            y = rows * size // 2 - row * size
            square(x, y, size, colors[i], colors[j])

            if i == 8:
                i = 2
            else:
                i += 2
            if j == 7:
                j = 1
            else:
                j += 2


t.hideturtle()
t.done()
