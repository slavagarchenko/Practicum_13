import turtle
import random


def draw_star(x, y):
    """
    Draw a star at specified coordinates.

    Args:
        x (int): X coordinate for the star
        y (int): Y coordinate for the star
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.dot(random.randint(2, 4))
    turtle.penup()


def draw_starry_sky(count=50):
    """
    Draw a starry sky with random stars.

    Args:
        count (int): Number of stars to draw (default: 50)
    """
    for _ in range(count):
        x = random.randint(-440, 440)
        y = random.randint(50, 280)
        draw_star(x, y)


def draw_moon():
    """
    Draw a moon with crescent phase effect using two overlapping circles.
    """
    turtle.penup()
    turtle.goto(270, 200)
    turtle.color("#f5c06d")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.goto(290, 220)
    turtle.color("#0b0c38")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()


def draw_window(x, y, width, height):
    """
    Draw a single building window.

    Args:
        x (int): X coordinate for window
        y (int): Y coordinate for window
        width (int): Width of the window
        height (int): Height of the window
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def draw_windows(x, width, height, density=10):
    """
    Draw random windows on a building.

    Args:
        x (int): Building's starting X coordinate
        width (int): Width of the building
        height (int): Height of the building
        density (int): Maximum number of windows to draw (default: 10)
    """
    turtle.color("#f5c06d")
    for _ in range(random.randint(5, density)):
        window_x = x + random.randint(8, width - 20)
        window_y = -300 + random.randint(15, height - 25)
        if random.choice([True, False]):
            window_width = random.choice([8, 10, 12])
            window_height = random.choice([10, 14, 18])
            draw_window(window_x, window_y, window_width, window_height)


def draw_roof(x, height, width):
    """
    Draw a roof with random style (flat, triangle, or spike).

    Args:
        x (int): Building's starting X coordinate
        height (int): Height of the building
        width (int): Width of the building
    """
    turtle.penup()
    turtle.goto(x, -300 + height)
    turtle.setheading(0)
    turtle.pendown()
    style = random.choice(["flat", "triangle"])

    turtle.begin_fill()
    if style == "flat":
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(5)
            turtle.left(90)
    elif style == "triangle":
        turtle.forward(width)
        turtle.left(135)
        turtle.forward(width / 2)
        turtle.left(90)
        turtle.forward(width / 2)
        turtle.left(135)
    turtle.end_fill()
    turtle.penup()


def draw_building(x, width, height, color, has_windows=True, density=10):
    """
    Draw a single building with specified parameters.

    Args:
        x (int): X coordinate for the building
        width (int): Width of the building
        height (int): Height of the building
        color (str): Color of the building
        has_windows (bool): Whether to draw windows (default: True)
        density (int): Window density if windows are enabled (default: 10)
    """
    turtle.penup()
    turtle.goto(x, -300)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

    draw_roof(x, height, width)
    if has_windows:
        draw_windows(x, width, height, density)


def draw_cityscape(y_offset, color_palette, height_range, density=10,
                   has_windows=True):
    """
    Draw a complete cityscape with multiple buildings.

    Args:
        y_offset (int): Vertical offset for the cityscape
        color_palette (list): List of colors for buildings
        height_range (tuple): Min and max height for buildings (min, max)
        density (int): Window density for buildings (default: 10)
        has_windows (bool): Whether buildings should have windows (default: True)
    """
    x = -450
    while x < 450:
        width = random.randint(50, 100)
        height = random.randint(*height_range)
        color = random.choice(color_palette)
        draw_building(x, width, height, color, has_windows, density)
        x += width - random.randint(0, 15)


def main():
    """
    Main function to set up the scene and draw all elements.
    Creates a night cityscape with stars, moon, and three layers of buildings.
    """
    turtle.setup(900, 600)
    turtle.bgcolor("#0b0c38")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(255)

    draw_starry_sky(50)
    draw_moon()

    draw_cityscape(
        y_offset=-200,
        color_palette=["#100828", "#130a30", "#170c35"],
        height_range=(200, 350),
        has_windows=False
    )

    draw_cityscape(
        y_offset=-250,
        color_palette=["#1e1648", "#2c1e57", "#3a2670", "#2a1d5b"],
        height_range=(150, 280),
        density=8,
        has_windows=True
    )

    draw_cityscape(
        y_offset=-300,
        color_palette=["#4a2e8c", "#5a3aa3", "#6b46ba"],
        height_range=(100, 200),
        density=12,
        has_windows=True
    )

    turtle.done()


if __name__ == "__main__":
    main()
