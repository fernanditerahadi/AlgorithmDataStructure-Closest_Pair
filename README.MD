== Finding the Closest Pair of Points ==

This is the alternative solution to 'Advanced Problem: Finding the Closest Pair
of Points'. The full description of the problem can be found on Algo - Closest Pair >
Problem Description > Advanced - Finding the Closest Pair of Points.

In short, we are required to find the closest pair of points among the given number
of points.

There are 2 solutions presented in this project: the original solution
and the alternative solution. The scripts (written in Python)
of these 2 solutions can be found in Algo - Closest Pair > Source Code.

The explanation and the strategy used in the original solution can be found on:
https://towardsdatascience.com/course-1-algorithmic-toolbox-part-3-divide-and-conquer-dd9022bfa2c0

On the other hand, the alternative solution that I wrote, does not use recursive techniques
which resulted in a faster computation for thousand of inputs. The strategy used in the alternative
solution is:
1. Divide the points into 4 groups; -+, ++, +-, --
2. Sort them by the score' and the value of X of each point.
3. Scan the sorted pairs in each group to find the shortest distance
4. After the scanning process, combine the shortest distance numbers from the
groups, put them into a list, and pick the smallest number.
5. Use this smallest number to find pair of points left in x and y axes which distance
are smaller than this number.
*Score = X + Y

By doing so, we do not need to evaluate the pair of points recursively thus reducing the
running time significantly, 3.8 seconds (original solution) vs 0.7 seconds (alternative solution)
on 100,000 inputs with pair of points ranging from -10^9 to 10^9.

To test the three methods, please navigate to Algo - Closest Pair > Standalone
Applications (Windows Only), download all the files and move them to a designated location
in your system.

The program will generate number of random points ranging from -10^Points-Range to 10^Points-Range.
For example, Points Range of 5 will let the program generate number of random points ranging from
-10^5 to 10^5.

The sample result of the program could be found in Algo - Closest Pair > Sample Result

Have a nice day,
Fernandi

January 2018
