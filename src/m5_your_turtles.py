"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Xuechen Bai.
"""
########################################################################
# TODO: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
lanxi = rg.SimpleTurtle('turtle')
lanxi.pen = rg.Pen('pink', 3)
lanxi.speed = 10
for k in range(20):
    lanxi.draw_circle(radius=100-5*k)
    lanxi.pen_up()
    lanxi.right(90)
    lanxi.backward(10)
    lanxi.left(90)
    lanxi.pen_down()

james = rg.SimpleTurtle('turtle')
james.pen = rg.Pen('light blue', 3)
james.speed = 10
for k in range(20):
    james.draw_circle(radius=100-5*k)
    james.pen_up()
    james.right(90)
    james.forward(10)
    james.left(90)
    james.pen_down()

window.close_on_mouse_click()

