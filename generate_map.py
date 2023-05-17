import json


def generate_map(folder):
    coordinates = []
    filename = f'{folder}/img/map.txt'
    contents = open(filename).read().strip()

    contents = contents.split('\n')
    for line in contents:
        filepath = line.split(' ')[0]
        filename = filepath.split('/')[1]
        x = filename.split('_')[0]
        y = filename.split('_')[1]
        coordinates.append((filepath, x, y))

    min_x = 100000
    min_y = 100000
    max_x = 0
    max_y = 0

    for coordinate in coordinates:
        x = float(coordinate[1])
        y = float(coordinate[2])
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    step = 0.2
    points = []
    for coordinate in coordinates:
        x = float(coordinate[1])
        y = float(coordinate[2])
        x = round((x - min_x) / step)
        y = round((y - min_y) / step)
        while len(points) <= x:
            points.append([])
        while len(points[x]) <= y:
            points[x].append(None)
        points[x][y] = coordinate
    
    min_x = 100000
    min_y = 100000
    max_x = 0
    max_y = 0

    json.dump(points, open(f'{folder}/points.json', 'w'))