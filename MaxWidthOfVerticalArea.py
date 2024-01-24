def max_width_of_vertical_area(points):
    points.sort(key = lambda x: x[0])
    answer = float("-inf")

    for i in range(1, len(points)):
        left_point = points[i-1][0]
        right_point = points[i][0]

        distance = right_point - left_point
        answer = max(answer, distance)
    return answer

print(max_width_of_vertical_area([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))