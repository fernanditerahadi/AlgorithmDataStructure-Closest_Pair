#Uses python3
import sys
import random, time

def test_case(length, spread):
    lst1 = [random.randint(-10**spread, 10**spread) for i in range(length)]
    lst2 = [random.randint(-10**spread, 10**spread) for i in range(length)]
    return lst1, lst2

def distance(x1, x2, y1, y2):
    return ((x1-x2)**2)+((y1-y2)**2)

def score(x1, y1):
    return x1+y1

def findmindist(array,var):
    var,l = var, len(array)
    mindist = None
    while l > var:
        dist = distance(array[var][0],array[var-1][0],array[var][1],array[var-1][1])
        if  mindist is None or dist <= mindist:
            mindist = dist
        if l > 2:
            dist = distance(array[var][0],array[var-2][0],array[var][1],array[var-2][1])
            if  mindist is None or dist <= mindist:
                mindist = dist
        var += 1
    return mindist

def minimum_distance(x, y):
    global starttime, endtime
    starttime = time.clock()
    points_1, points_2, points_3, points_4 = [], [], [], []
    lenx = len(x)
    distance = []
    i,j,k,l,o,p,q = 1,1,1,1,1,1,1
    for a,b in zip(x,y):
        c = score(a,b)
        if a < 0 and b >= 0:
            points_1 += [(a,b,1,c)]
        if a >= 0 and b >= 0:
            points_2 += [(a,b,2,c)]
        if a >= 0 and b < 0:
            points_3 += [(a,b,3,c)]
        if a < 0 and b < 0:
            points_4 += [(a,b,4,c)]

    sp1 = sorted(points_1, key=lambda x: (x[2],x[3],x[0]))
    sp2 = sorted(points_2, key=lambda x: (x[2],-x[3],-x[0]))
    sp3 = sorted(points_3, key=lambda x: (x[2],-x[3],-x[0]))
    sp4 = sorted(points_4, key=lambda x: (x[2],x[3],x[0]))

    l1,l2,l3,l4 = len(points_1), len(points_2), len(points_3), len(points_4)

    if (l1+l2+l3+l4) < 5:
        points = points_1 + points_2 + points_3 + points_4
        for i in [findmindist(points,q)]:
            if i is not None:
                distance += [i]
    else:
        for i in [findmindist(sp1,i), findmindist(sp2,j), findmindist(sp3,k), findmindist(sp4,l)]:
            if i is not None:
                distance += [i]

    try:
        minimum_distance = (min(distance))**(0.5)
    except:
        distance += [0]
        minimum_distance = (min(distance))**(0.5)

    if l1 != lenx and l2 != lenx and l3 != lenx and l4 != lenx:
        edge_points_x, edge_points_y = [], []
        for a,b in zip(x,y):
            if -minimum_distance < a < minimum_distance:
                edge_points_y += [(a,b)]
            if -minimum_distance < b < minimum_distance:
                edge_points_x += [(a,b)]
        sepx = sorted(edge_points_x, key=lambda x: x[0])
        sepy = sorted(edge_points_y, key=lambda y: -y[1])
        for i in [findmindist(sepx,o), findmindist(sepy,p)]:
            if i is not None:
                distance += [i]

    endtime = time.clock()
    return (min(distance))**(0.5)

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
    print('\nVinsensius Fernandi, January 2018')
    input()
