import data
# Write your functions for each part in the space below.

# Part 1
def first_element(nested_list: list[list[int]]) -> list:
   list1 = []
   for i in range(len(nested_list)):
        if len(nested_list[i]) > 0:
            list1.append(nested_list[i][0])
   return list1
# Purpose: Append the first item to an empty list from each inputted nested list
# Part 2
def x_coordinates(points: list[[list[data.Point]]]) -> list[float]:
    points1 = []
    for point in points:
        points1.append(point.x)
    return points1
#Purpose: Append the first item (x-coordinate) to an empty list from each inputted list (point)
# Part 3
def are_in_positive_quadrant(points: list[[list[data.Point]]]) -> list[list]:
    points2 = []
    for point in points:
        if point.x > 0 and point.y > 0:
            points2.append(point)
    return points2
#Purpose: Add the point to an empty list only if the x and y coordinates are positive
# Part 4
def distance(point1: data.Point, point2: data.Point) -> float:
    euclidean = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)**(1/2)
    return euclidean
#Purpose: Take the inputted values and find the Euclidean distance
# Part 5
def manhattan_distance(point1: data.Point, point2: data.Point) -> float:
    manhattan = abs(point1.x - point2.x) - abs(point1.y - point2.y)
    return manhattan
#Purpose: Take the inputted values and find the Manhattan distance
# Part 6
def distance_all(points: list[data.Point]) -> list[list]:
    all = []
    for point in points:
        euclidean = ((point.x - 0) ** 2 + (point.y - 0) ** 2) ** (1 / 2)
        all.append(euclidean)
    return all
#Purpose: Determine the distance between the origin (0,0) to the inputted points


