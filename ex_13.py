import turtle

turtle.speed(0)


def triangle(points, color):
    """
    Draw a filled triangle.

    Args:
        points (list): List of three coordinate tuples [(x1, y1), (x2, y2), (x3, y3)]
                        representing the triangle vertices
        color (str): Fill color of the triangle in hex format or color name.

    Returns:
        None
    """
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.begin_fill()
    for point in points:
        turtle.goto(point)
    turtle.goto(points[0])
    turtle.end_fill()


def square(x, y, size, color1, color2, quarter):
    """
    Draw a square composed of two triangles.

    Args:
        x (float): X-coordinate of the bottom-left corner.
        y (float): Y-coordinate of the bottom-left corner.
        size (float): Side length of the square.
        color1 (str): Color of the first triangle.
        color2 (str): Color of the second triangle.
        quater (int): Quater number determining orietation

    Returns:
        None
    """
    if quarter == 1:
        points1 = [(x, y), (x+size, y), (x, y-size)]
        points2 = [(x+size, y), (x+size, y-size), (x, y-size)]
    elif quarter == 2:
        points1 = [(x, y), (x-size, y), (x, y-size)]
        points2 = [(x-size, y), (x-size, y-size), (x, y-size)]
    elif quarter == 3:
        points1 = [(x, y), (x-size, y), (x, y+size)]
        points2 = [(x-size, y), (x-size, y+size), (x, y+size)]
    else:
        points1 = [(x, y), (x+size, y), (x, y+size)]
        points2 = [(x+size, y), (x+size, y+size), (x, y+size)]

    triangle(points1, color1)
    triangle(points2, color2)


def pattern():
    """
    Draw a complete pattern composed of four colored queters.
    """
    colors = {
        'синий': '#1E90FF',
        'бирюзовый': '#AFEEEE',
        'голубой': '#87CEFA'
    }

    turtle.speed(10)
    turtle.pencolor('white')

    quarter_size = 300
    square_size = quarter_size / 3

    color_combinations = [
        (colors['бирюзовый'], colors['голубой']),
        (colors['голубой'], colors['синий']),
        (colors['синий'], colors['голубой']),
        (colors['голубой'], colors['бирюзовый'])
    ]

    for quarter in range(1, 5):
        if quarter == 1:
            start_x, start_y = 0, quarter_size
        elif quarter == 2:
            start_x, start_y = 0, quarter_size
        elif quarter == 3:
            start_x, start_y = 0, -quarter_size
        else:
            start_x, start_y = 0, -quarter_size

        for i in range(3):
            for j in range(3):
                color_index = (i + j) % 4
                color1, color2 = color_combinations[color_index]

                if quarter in [1, 4]:
                    x = start_x + i * square_size
                else:
                    x = start_x - i * square_size

                if quarter in [1, 2]:
                    y = start_y - j * square_size
                else:
                    y = start_y + j * square_size

                square(x, y, square_size, color1, color2, quarter)


pattern()
turtle.done()
