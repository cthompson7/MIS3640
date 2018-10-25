import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

# jack = Point()
# print(type(jack))

# jack.x = 3
# jack.y = 4

# print(jack.x, jack.y)
#
# x = jack.y
# print(x)
# print(jack.x)
#
#
# print('(%g, %g)' % (jack.x, jack.y))
# distance = math.sqrt(jack.x**2 + jack.y**2)
# print(distance)


def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))

# print_point(jack)
#
# jonathan = Point()
# jonathan.x = 4
# jonathan.y = 5

# print_point(jonathan)

# print(hasattr(jack, "x"))
# print(hasattr(jack, "z"))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    distanceFormula = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

    return distanceFormula

# print(distance_between_points(jack, jonathan))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

# angela = Rectangle()
# angela.width = 100
# angela.height = 200
# angela.corner = jack


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


# sarah = find_center(angela)
# print_point(sarah)


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

# print_rectangle(angela)
# grow_rectangle(angela, 50, 100)
# print('after growing')
# print_rectangle(angela)



class Circle:
    "This is a class of Circle"


christian = Circle()
christian.center = Point()
christian.center.x = 150
christian.center.y = 100
christian.radius = 75

print(christian.center.x)
print(christian.center.y)
print(christian.radius)

def point_in_circle(point, christian):
    distance = distance_between_points(point, christian.center)
    if distance <= christian.radius:
        return True
    else:
        return False

testCircle = Point()
testCircle.x = 1000
testCircle.y = 1000

print(point_in_circle(testCircle, christian))

import copy

def rect_in_circle(rectangle, christian):
    copyOf = copy.copy(rectangle.corner)
    if not point_in_circle(copyOf, christian):
        return False
    copyOf.x = copyOf.x + rectangle.width
    if not point_in_circle(copyOf, christian):
        return False
    copyOf.y = copyOf.y - rectangle.height
    if not point_in_circle(copyOf, christian):
        return False
    copyOf.x = copyOf.x - rectangle.width
    if not point_in_circle(copyOf, christian):
        return False
    return True

testRectangle = Rectangle()
testRectangle.height = 100
testRectangle.width = 50
testRectangle.corner = Point()
testRectangle.corner.x = 30
testRectangle.corner.y = 30

print(rect_in_circle(testRectangle, christian))


def rect_circle_overlap(rectangle, christian):
    copyOf = copy.copy(rectangle.corner)
    if point_in_circle(copyOf, christian):
        return True
    copyOf.x = copyOf.x + rectangle.width
    if point_in_circle(copyOf, christian):
        return True
    copyOf.y = copyOf.y - rectangle.height
    if point_in_circle(copyOf, christian):
        return True
    copyOf.x = copyOf.x - rectangle.width
    if point_in_circle(copyOf, christian):
        return True
    return False

print(rect_circle_overlap(testRectangle, christian))



# def main():
#     my_point = Point()
#     print(Point.__doc__)
#     my_point.x = 3
#     my_point.y = 4
#     print('My point', end=' ')
#     print_point(my_point)
#
#     print('Is my_point an instance of Point?', isinstance(my_point, Point))
#     print('Is my_point an instance of Rectangle?',
#           isinstance(my_point, Rectangle))
#     print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
#     print('Does my_point have an attribute z?', hasattr(my_point, 'z'))
#
#     box = Rectangle()
#     box.width = 100.0
#     box.height = 200.0
#     box.corner = Point()
#     box.corner.x = 0.0
#     box.corner.y = 0.0
#
#     print('Does box have an attribute x?', hasattr(box, 'x'))
#
#     print('Does box have an attribute corner?', hasattr(box, 'corner'))
#
#     print('Rectangle has these:', dir(box))
#
#     center = find_center(box)
#     print('center', end=' ')
#     print_point(center)
#
#     print(box.width)
#     print(box.height)
#     print('grow')
#     grow_rectangle(box, 50, 100)
#     print(box.width)
#     print(box.height)
#
#
# if __name__ == '__main__':
#     main()


# OOP 2 Demo Code
class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
# print(done)

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time_2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time_2(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
