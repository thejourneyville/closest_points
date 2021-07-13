import random
import pygame
import closest_points_algorithm
"""
CLOSEST PAIR OF POINTS IN LINEARITHMIC TIME:
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
"""

# initialize pygame and set surface dimensions
pygame.init()
width = 800
height = 600
surface = pygame.display.set_mode((width, height))

# window caption, clock speed
pygame.display.set_caption("Plotting Moving Closest Points with Pygame and Closest Points O(nlogn) Algorithm")
clock = pygame.time.Clock()
fps = 60


# instantiate object from Point class
class Point:
    def __init__(self):
        self.x = int(random.randrange(80000)/100)
        self.y = int(random.randrange(60000)/100)
        self.current = [self.x, self.y]  # starting coordinates
        self.destination = set_destination()  # starting destination
        self.radius = 5
        self.speed = 2
        self.distance = distance(self.destination, self.current)  # distance to destination

        # to calculate speed on x/y axis
        self.x_distance = 0
        self.y_distance = 0
        self.x_distance_speed = 0
        self.y_distance_speed = 0

        # random color instantiation
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    def hunt_destination(self, currents, current_x, current_y):
        """
        :param currents: list of current coordinates of all points
        :param current_x: x coordinate of currently examined point
        :param current_y: y coordinate of currently examined point
        """

        self.distance = distance(self.destination, (current_x, current_y))  # distance calculated to point destination
        self.x_distance = abs(current_x - self.destination[0])  # x axis distance
        self.y_distance = abs(current_y - self.destination[1])  # y axis distance

        self.x_distance_speed = self.x_distance / self.distance  # x axis speed calculated
        self.y_distance_speed = self.y_distance / self.distance  # y axis speed calculated

        # avoid collisions - if <= radius * 2 distance to another point, will assign new destination
        currents.pop(currents.index((current_x, current_y)))
        collision = [True for other_pos in currents if distance(other_pos, (current_x, current_y)) <= self.radius * 2]

        if self.distance < 10:
            self.destination = set_destination()
        elif any(collision):
            self.destination = set_destination()
        else:
            # set direction and x speed based on destination position and x_distance_speed
            if current_x < self.destination[0]:
                self.current[0] += self.x_distance_speed * self.speed
            elif current_x > self.destination[0]:
                self.current[0] -= self.x_distance_speed * self.speed

            # set direction and y speed based on destination position and y_distance_speed
            if current_y < self.destination[1]:
                self.current[1] += self.y_distance_speed * self.speed
            elif current_y > self.destination[1]:
                self.current[1] -= self.y_distance_speed * self.speed

    # render point
    def render(self):
        pygame.draw.circle(surface, self.color, self.current, self.radius)


# render coordinate text of currently examined point
def render_text(x, y):
    font = pygame.font.Font("MomcakeThin-9Y6aZ.otf", 15)
    text_surface_x = font.render("X: " + str(int(x)), True, (255, 255, 255))
    text_surface_y = font.render("Y: " + str(int(height - y)), True, (255, 255, 255))
    text_rect_x = text_surface_x.get_rect()
    text_rect_x.left, text_rect_x.y = x - 4, y + 5
    surface.blit(text_surface_x, text_rect_x)
    text_rect_y = text_surface_y.get_rect()
    text_rect_y.left, text_rect_y.y = x + 35, y + 5
    surface.blit(text_surface_y, text_rect_y)


# set new destination
def set_destination():
    return [random.randrange(80000)/100, random.randrange(60000)/100]


# calculate distance using Euclidean formula
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** .5


# render line between closest points
def render_line(c):
    d = distance(c[0], c[1])
    if d > 225: d = 225
    intensity = int(255 - d)
    pygame.draw.line(surface, (intensity, intensity, intensity), c[0], c[1], 2)


# render current count of total points
def render_count_text(count):
    font = pygame.font.Font("MomcakeBold-WyonA.otf", 25)
    text_surface = font.render(str(count), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.x, text_rect.bottom = 25, height - 25
    surface.blit(text_surface, text_rect)


# create 2 instances from Point class
points = [Point() for i in range(2)]


def run():

    while True:  # outer loop adds additional point to surface when timer reaches 400
        add_point_timer = 0

        while add_point_timer < 400:
            clock.tick(fps)  # frame speed
            surface.fill((0, 0, 0))

            # enables quitting by closing the surface window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            # collect all x/y coordinates of points into list all_currents
            all_currents = [(point.current[0], point.current[-1]) for point in points]

            # runs closest pairs algorithm in O(n log n) using divide and conquer (see closest_points_algorithm.py)
            closest = closest_points_algorithm.closest_pair(all_currents)

            # iterate through al instances
            for point in points:
                point.render()
                render_text(point.current[0], point.current[-1])

                # determine heading, speed, and collision avoidance
                point.hunt_destination(all_currents, point.current[0], point.current[-1])

            render_line(closest)  # line connecting closest points
            render_count_text(len(points))  # current count of total points

            add_point_timer += 1  # increase timer to the adding of another point
            pygame.display.flip()  # redraw screen

        # sets limit of number of points on surface simultaneously
        if len(points) <= 10:
            new_point = [Point() for _ in range(1)]
            points.append(new_point[0])


if __name__ == "__main__":
    run()
