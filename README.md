<h2>CLOSEST PAIR OF POINTS IN LINEARITHMIC TIME:</h2>
<img src="https://github.com/https://github.com/thejourneyville/closest_points/blob/main/closest_points/Untitled.png"></img>
(problem considered by M. I. Shamos and D. Hoey in the early 1970s)
https://www.codewars.com/kata/5376b901424ed4f8c20002b7/train/python
This started as a Codewars challenge, but wound up becoming a big learning project, as initially,
I had no idea how to find the closest pair of coordinates without using a brute-force method,
which in this case would be O(n^2), to simply iterate through every point and measure its distance to
every other point, returning the shortest one. In the case of less-than-many number of points, this perhaps
would be a good option, but considering a situation where there are perhaps thousands of points, (ie: stars)
it starts to drag quite a bit and kept timing out on the Codewars challenge.

I started studying about a recursive method which sorts by its X coordinate and then continually divides 
the 2D plane in half until it reaches its base case of 3 or less points, then using Euclidean distance to 
return the shortest distance of the 2 to 3 points remaining. The left and right side of the graph would 
then compare their shortest contenders and the winner would be designated as Delta.

It may seem like the process would end here, however we still have not accounted for a pair of points where
one point lies on the left side of the graph and the other point lies on the right. From the center line
dividing all coordinates by their X axis, we can measure Delta to the left and right (Delta * 2) and can immediately 
eliminate any potential pairs which are not in this established Delta zone because we now know they must be longer
than Delta.

With the remaining candidates we then sort them by their Y axis and step through each point measuring it to its
neighbors up to 7 neighbors away, thus returning our now closest pair in O(n log n) time. 

This implementation uses Pygame to randomly place points in space, have them continually
move while keeping track of the closest 2 points, connecting them with a line and updating
in real time.

These fonts are free for personal use:
MomcakeBold-WyonA.otf
MomcakeThin-9Y6aZ.otf
Attainable at:
https://www.dafont.com/momcake.font
rvn19@yahoo.com

Thanks for your interest!
bennyBoy_JP 2021
twitter: https://twitter.com/Bennyboy_JP
