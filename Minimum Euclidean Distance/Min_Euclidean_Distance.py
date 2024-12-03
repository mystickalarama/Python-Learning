points = [(3, 7), (-4, 2), (1, 3)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

print(f"Minumum distance: {min(distances)}")
