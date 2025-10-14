from manim import *


class Player(Scene):
    def construct(self):
        a=Square()
        a.set_color(LOGO_BLUE)
        b=Triangle()
        b.next_to(a,DOWN,buff=0.2)
        self.play(Create(a))
        self.play(Create(b))

class Rotations(Scene):
    def construct1(self):
        a=Square()
        b=Square()
        a.set_fill(BLUE,opacity=0.5).shift(RIGHT)
        b.set_fill(PURPLE,opacity=0.5).shift(LEFT)
        self.play(Rotate(a,angle=PI),Rotate(b,angle=PI),run_time=2)
        self.play(FadeOut(a,b))

    def construct2(self):
        a = Square()
        b = Square()
        a.set_fill(BLUE, opacity=0.5).shift(RIGHT)
        b.set_fill(PURPLE, opacity=0.5).shift(LEFT)
        self.play(a.animate.rotate(PI),b.animate.rotate(PI),run_time=2)
        self.play(FadeOut(a,b))

    def construct(self):
        self.construct1()
        self.wait(1)
        self.construct2()
