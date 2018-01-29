#Uses python3
import sys
import random, time, math

def test_case(length, spread):
    lst1 = [random.randint(-10**spread, 10**spread) for i in range(length)]
    lst2 = [random.randint(-10**spread, 10**spread) for i in range(length)]
    return lst1, lst2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) **0.5

def construct_points(x, y):
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))
    return points

def minimum_distance(x, y):
    global starttime
    starttime = time.clock()
    points = construct_points(x, y)
    sorted_p_x = sorted(points, key=lambda p: p.x)
    return large_size_min_distance(sorted_p_x)

def small_size_min_distance(points):
    global endtime
    result = sys.maxsize
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            result = min(result, distance(points[i], points[j]))
    endtime = time.clock()
    return result

def large_size_min_distance(p_x):
    global endtime
    size = len(p_x)
    half_size = int(len(p_x)/2)

    if size <= 3:
        return small_size_min_distance(p_x)

    left_p_x = p_x[0:half_size]
    right_p_x = p_x[half_size:size]

    left_min = large_size_min_distance(left_p_x)
    right_min = large_size_min_distance(right_p_x)
    separated_min = min(left_min, right_min)

    line_l = (left_p_x[-1].x + right_p_x[0].x)/2
    hybrid_min = compute_hybrid_min(left_p_x, right_p_x, line_l, separated_min)

    endtime = time.clock()
    return min(separated_min, hybrid_min)

def compute_hybrid_min(left_x, right_x, line_l, wide):
    left = []
    for i in range(len(left_x)):
        if abs(left_x[i].x - line_l) <= wide:
            left.append(left_x[i])
    right = []
    for i in range(len(right_x)):
        if abs(right_x[i].x - line_l) <= wide:
            right.append(right_x[i])
    total = left + right

    total = sorted(total, key=lambda p: p.y)

    result = wide
    for i in range(len(total)):
        for j in range(i + 1, min(i+8, len(total))):
            if abs(total[i].y - total[j].y) <= wide:
                result = min(result, distance(total[i], total[j]))

    return result

if __name__ == '__main__':
    status = 0
    while status < 1:
        try:
            userinput1 = int(input('NUMBER OF RANDOM POINTS: '))
            userinput2 = int(input('POINTS RANGE (1-10): '))
            if 1 <= userinput2 <= 10:
                status += 1
            else:
                print('\n*** Please enter a numeric number ranging from 1-10 ***\n')
                continue
        except KeyboardInterrupt:
            quit()
        except:
            print('\n*** Please enter a numeric number ***\n')
            continue

    g, h = test_case(userinput1, userinput2)
    print('RANDOM POINTS:', [(a,b) for a,b in zip(g,h)])
    print('\nSHORTEST DISTANCE:',"{0:.9f}".format(minimum_distance(g, h)))
    print('RUNNING TIME:',endtime - starttime, 'seconds')
    input()
