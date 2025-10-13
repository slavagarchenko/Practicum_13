import turtle as t

t.speed(0)


def square(x, y, size, color):
    """Draw a filled rectangle.

    Args:
        x (float): The x-coordinate of the bottom-left corner.
        y (float): The y-coordinate of the bottom-left corner.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        color (str): The fill color of the rectangle.

    Returns:
        None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.penup()


def triangle(x, y, size, color, is_upward=True):
    """Draw a filled equilateral triangle.

    Args:
        x (float): The x-coordinate of the bottom-left corner.
        y (float): The y-coordinate of the bottom-left corner.
        size (float): The length of each side of the triangle.
        color (str): The fill color of the triangle.
        is_upward (bool, optional): If True, triangle points upward;
                                    if False, downward. Defaults to True.

    Returns:
        None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        if is_upward:
            t.left(120)
        else:
            t.right(120)
    t.end_fill()
    t.penup()


def hexagon(x, y, size, color):
    """Draw a filled regular hexagon.

    Args:
        x (float): The x-coordinate of the center.
        y (float): The y-coordinate of the center.
        size (float): The length of each side of the hexagon.
        color (str): The fill color of the hexagon.

    Returns:
        None
    """
    t.penup()
    t.goto(x, y - size / 2)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(6):
        t.forward(size)
        t.left(60)
    t.end_fill()
    t.penup()


def ornament(num_elements, size):
    """
    Draws an ornament with triangles on top and bottom, and alternating
    blue hexagons and green squares.

    Args:
        num_elements (int): Number of elements (hexagons and squares)
                            in the pattern.
        size (float): The size of each shape (side length for triangles,
                        hexagons, and squares).

    Returns:
        None
    """
    t.penup()
    start_x = - (num_elements * size * 1.5) / 2
    t.goto(start_x, 0)
    t.pendown()

    t.penup()
    t.goto(start_x, size * 2 + 25)
    t.pendown()
    for i in range(num_elements + 1):
        t.penup()
        t.goto(start_x + i * size * 1.5, size * 2 + 25)
        t.pendown()
        triangle(start_x + i * size * 1.5, size *
                 2+25, size, "orange", is_upward=False)

    t.penup()
    t.goto(start_x, -size * 2)
    t.pendown()
    for i in range(num_elements + 1):
        t.penup()
        t.goto(start_x + i * size * 1.5, -size * 2)
        t.pendown()
        triangle(start_x + i * size * 1.5, -size *
                 2, size, "orange", is_upward=True)

    for i in range(num_elements + 1):
        x = start_x + i * size * 1.5
        y = 0
        t.penup()
        t.goto(x, y)
        t.pendown()
        if i % 2 == 0:
            hexagon(x, y, size, "blue")
        else:
            square(x, y, size, "green")
            square(x, y + 65, size, "green")

    t.penup()


ornament(6, 40)
t.done()
