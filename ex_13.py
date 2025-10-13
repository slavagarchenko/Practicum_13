import turtle as t

t.speed(0)


def triangle(p1, p2, p3, color):
    """

    """
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.goto(p1)
    t.pendown()
    t.begin_fill()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)  # Замыкаем треугольник
    t.end_fill()


def square_from_triangles(x, y, size, color1, color2):
    """

    """
    bottom_left = (x, y)
    bottom_right = (x + size, y)
    top_right = (x + size, y + size)
    top_left = (x, y + size)

    triangle(bottom_left, bottom_right, top_right, color1)
    triangle(bottom_left, top_right, top_left, color2)


def pattern(rows, cols, size):
    """

    """
    spacing = size  # Расстояние между квадратами равно размеру стороны
    start_x = -cols * spacing / 2  # Центрируем узор по X
    start_y = rows * spacing / 2   # Центрируем узор по Y

    # Цвета для чередования
    colors = ["yellow", "blue"]

    for i in range(rows):
        for j in range(cols):
            # Координаты левого нижнего угла текущего квадрата
            x = start_x + j * spacing
            y = start_y - i * spacing

            # Чередование цветов в шахматном порядке
            if (i + j) % 2 == 0:
                color1, color2 = colors[0], colors[1]  # Желтый и синий
            else:
                color1, color2 = colors[1], colors[0]  # Синий и желтый

            square_from_triangles(x, y, size, color1, color2)


rows = int(input("Введите количество строчек: "))
cols = int(input("Введите количество столбцов: "))
size = 50

pattern(rows, cols, size)

t.hideturtle()
t.done()
