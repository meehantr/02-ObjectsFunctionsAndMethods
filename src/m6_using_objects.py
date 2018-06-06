"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Thomas Meehan.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window1 = rg.RoseWindow()
    p1 = rg.Point(100, 100)
    p2 = rg.Point(200, 200)
    circle1 = rg.Circle(p1, 50)
    circle2 = rg.Circle(p2, 30)
    circle1.fill_color = 'red'
    circle1.attach_to(window1)
    circle2.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window2 = rg.RoseWindow()

    p1 = rg.Point(100, 150)
    circle = rg.Circle(p1, 50)
    circle.fill_color = 'blue'
    circle.outline_thickness = 3
    print(3)
    print('blue')
    print(p1)
    print(p1.x)
    print(p1.y)

    c1 = rg.Point(200, 200)
    c2 = rg.Point(250, 250)
    rectangle = rg.Rectangle(c1, c2)
    center = rectangle.get_center()
    print(1)
    print('none')
    print(center)
    print(center.x)
    print(center.y)

    circle.attach_to(window2)
    rectangle.attach_to(window2)
    window2.render()
    window2.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # done: 4. Implement and test this function.
    # -------------------------------------------------------------------------
    window3 = rg.RoseWindow()

    s1 = rg.Point(45, 167)
    e1 = rg.Point(150, 100)
    line1 = rg.Line(s1, e1)

    s2 = rg.Point(200, 250)
    e2 = rg.Point(150, 200)
    line2 = rg.Line(s2, e2)
    line2.thickness = 3

    midpoint = line2.get_midpoint()
    print(midpoint)
    print(midpoint.x)
    print(midpoint.y)

    line1.attach_to(window3)
    line2.attach_to(window3)
    window3.render()
    window3.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
