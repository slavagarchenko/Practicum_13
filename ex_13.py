import turtle

def draw_triangle(vertices, color):
    """
    Рисует треугольник по координатам вершин и заданному цвету
    vertices: список из трех кортежей [(x1,y1), (x2,y2), (x3,y3)]
    color: строка с названием цвета
    """
    turtle.penup()
    turtle.goto(vertices[0])  # Переходим к первой вершине
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    # Рисуем треугольник
    turtle.goto(vertices[1])
    turtle.goto(vertices[2])
    turtle.goto(vertices[0])  # Возвращаемся к началу
    
    turtle.end_fill()

def draw_square(center_x, center_y, size, color1, color2):
    """
    Рисует квадрат из двух треугольников
    center_x, center_y: координаты центра квадрата
    size: размер стороны квадрата
    color1, color2: цвета для двух треугольников
    """
    half_size = size / 2
    
    # Координаты углов квадрата
    top_left = (center_x - half_size, center_y + half_size)
    top_right = (center_x + half_size, center_y + half_size)
    bottom_left = (center_x - half_size, center_y - half_size)
    bottom_right = (center_x + half_size, center_y - half_size)
    
    # Первый треугольник (левый нижний + правый верхний)
    triangle1_vertices = [bottom_left, top_right, top_left]
    draw_triangle(triangle1_vertices, color1)
    
    # Второй треугольник (правый нижний + левый верхний)  
    triangle2_vertices = [bottom_left, top_right, bottom_right]
    draw_triangle(triangle2_vertices, color2)

def draw_tile_pattern(rows, cols, tile_size):
    """
    Рисует узор кафельной плитки
    rows: количество строк
    cols: количество столбцов
    tile_size: размер плитки
    """
    # Цвета для узора
    colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightyellow']
    
    # Начальные координаты (центр первого квадрата)
    start_x = - (cols * tile_size) / 2 + tile_size / 2
    start_y = (rows * tile_size) / 2 - tile_size / 2
    
    for row in range(rows):
        for col in range(cols):
            # Координаты центра текущей плитки
            x = start_x + col * tile_size
            y = start_y - row * tile_size
            
            # Выбираем цвета в шахматном порядке
            color_index = (row + col) % 2
            color1 = colors[color_index]
            color2 = colors[(color_index + 1) % len(colors)]
            
            # Рисуем квадрат из двух треугольников
            draw_square(x, y, tile_size, color1, color2)
