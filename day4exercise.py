from manim import *

class exp(Scene):
    def construct(self):
        square=Square()
        square.set_fill(color=BLUE,opacity=1)
        square.rotate(PI/8)

        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))

        self.play(Create(square))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)

class exercise(Scene):
    def construct(self):
        square=Square()
        square.set_fill(color=BLUE,opacity=1)

        line = Line(LEFT, RIGHT)

        self.play(Create(square))
        self.play(Create(line))
        self.play(square.animate.shift(UP*2).rotate(PI/8))
        self.play(line.animate.rotate(PI/4).shift(RIGHT*2))
        self.wait(5)
        self.play(self.camera.frame.animate.set_width(5).move_to(square.get_center()))
        self.wait(2)
        self.play(self.camera.frame.animate.set_width(5).move_to(line.get_center()))
        self.wait(2)

from manim import *

class FallingProjectile(Scene):
    def construct(self):
        # Setup
        dot = Dot().move_to(UP*3)  # starting high
        g = 9.8  # gravity
        t = ValueTracker(0)  # time tracker

        # Function to update dot's position based on free fall
        def update_dot(mob):
            y = 3 - 0.5 * g * t.get_value()**2  # y = y0 - 1/2 * g * t^2
            mob.move_to(np.array([0, y, 0]))

        dot.add_updater(update_dot)
        self.add(dot)

        # Animate time from 0 to sqrt(6/g) so dot falls 3 units
        self.play(t.animate.set_value(2), run_time=2, rate_func=linear)
        self.wait(1)



from manim_physics import *

class MultiPendulumExample(SpaceScene):
    def construct(self):
        p = MultiPendulum(RIGHT, LEFT)
        self.add(p)
        self.make_rigid_body(*p.bobs)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE))
        self.wait(10)



from manim import *
import numpy as np

class Pendulum(Scene):
    def construct(self):
        # Parameters
        L = 3        # length of pendulum
        theta0 = PI/4  # initial angle (radians)
        g = 9.8      # gravity

        origin = UP*2
        pendulum_line = Line(origin, origin + L*DOWN, stroke_width=3)
        bob = Dot(origin + L*DOWN, radius=0.15, color=RED)

        # Time tracker
        t = ValueTracker(0)

        # Small-angle approximation for pendulum: theta(t) = theta0 * cos(sqrt(g/L) * t)
        def update_pendulum(mob):
            theta = theta0 * np.cos(np.sqrt(g/L) * t.get_value())
            new_pos = origin + L * np.array([np.sin(theta), -np.cos(theta), 0])
            pendulum_line.put_start_and_end_on(origin, new_pos)
            bob.move_to(new_pos)

        pendulum_line.add_updater(lambda mob: update_pendulum(mob))
        bob.add_updater(lambda mob: update_pendulum(mob))

        self.add(pendulum_line, bob)
        self.play(t.animate.set_value(10), run_time=10, rate_func=linear)
        self.wait(1)






