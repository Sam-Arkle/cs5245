class Rectangle:
    """ Represents a geometrical rectangle at a specific location and with a
    specific width and height. """

    def __init__(self, point, width, height):
        # ©2019 Richard L. Halterman Draft date: June 26, 2019
        # 13.11. EXERCISES 509
        """ Establishes the rectangle's lower-left corner, width, and height.
        point: a tuple representing the (x, y) location of the rectangle's lower-left corner
        width: an integer representing the rectangle's width
        height: an integer representing the rectangle's height """
        # Ensure the lower-left corner's x and y coordinates fall in the range -100...100
        x, y = point
        x = -100 if x < -100 else 100 if x > 100 else x
        y = -100 if y < -100 else 100 if y > 100 else y
        self.corner = x, y  # Pack the x and y values into a tuple
        # Ensure the rectangle's width and height are both nonnegative
        self.width = 0 if width < 0 else width
        self.height = 0 if height < 0 else height

    def get_perimeter(self):
        """ Computes the perimeter of the rectangle. """
        return 2 * self.width + 2 * self.height

    def get_area(self):
        """ Computes the perimeter of the rectangle. """
        return self.width * self.height

    def get_width(self):
        """ Returns the width of the rectangle. """
        return self.width

    def get_height(self):
        """ Returns the height of the rectangle. """
        return self.height

    def grow(self, n):
        """ Increases the dimensions of the rectangle.
        Both width and height increase by one. """
        self.width += 1
        self.height += 1

    def move(self, x, y):
        """ Moves the rectangle's lower-left corner to the specified
        (x, y) location. """
        self.corner = x, y

    def intersect(self, other_rec):
        """ Returns true if rectangle other_rec overlaps this
        rectangle object; otherwise, returns false. """
        # Details omitted
        # Check the lower left corner of both rectangles and see if their width or
        # height puts them in overlapping coordinates.
        pass

    def diagonal(self):
        """ Returns the length of a diagonal rounded to the nearest
        integer. """
        # Details omitted
        return round(((self.width ** 2) + (self.height ** 2)) ** (1 / 2))

    def center(self):
        """ Returns the geometric center of the rectangle with
        the (x,y) coordinates rounded to the nearest integer. """
        # Details omitted
        centre = (self.corner[0] + self.width//2, self.corner[1] + self.height//2)
        return round(centre)

    def is_inside(self, pt):
        """ Returns true if the tuple pt represents a point within
        the bounds of the rectangle; otherwise, returns false.
        As in soccer and tennis, "on the line" is "in." """
        # Details omitted
        is_inside = False
        x_condition = self.corner[0] <= pt[0] <= (self.corner[0] + self.width)
        y_condition = self.corner[1] <= pt[1] <= (self.corner[1] + self.height)
        if x_condition & y_condition:
            is_inside = True

        return is_inside


def main():
    rect1 = Rectangle((2, 3), 5, 7)
    rect2 = Rectangle((5, 13), 1, 3)
    rect3 = Rectangle((20, 40), -5, 45)
    rect4 = Rectangle((-510, -220), 5, -4)
    # print(rect1.get_width())
    # print(rect1.get_height())
    # print(rect2.get_width())
    # print(rect2.get_height())
    # print(rect3.get_width())
    # print(rect3.get_height())
    # print(rect4.get_width())
    # print(rect4.get_height())
    # print(rect1.get_perimeter())
    # print(rect1.get_area())
    # print(rect2.get_perimeter())
    # print(rect2.get_area())
    # print(rect3.get_perimeter())
    # print(rect3.get_area())
    # print(rect4.get_perimeter())
    # print(rect4.get_area())
    print(rect1.is_inside((4,5)))


if __name__ == '__main__':
    main()
