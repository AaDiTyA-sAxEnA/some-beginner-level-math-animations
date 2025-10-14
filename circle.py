from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK, opacity=0.5)

        square=Square()
        square.rotate(PI/8)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class SquareWithCircle(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK, opacity=0.5)

        square=Square()
        square.rotate(PI/8)

        self.play(Create(square))
        self.play(Create(circle))
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK, opacity=0.5)

        square=Square()
        square.set_fill(BLUE, opacity=0.75)

        square.next_to(circle, UP, buff=0.3)

        self.play(Create(circle),Create(square))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle=Circle()
        square=Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(BLUE,opacity=0.8))

class SquareFlip(Scene):
    def construct(self):
        square=Square()
        square.set_fill(BLUE, opacity=.3)
        square.flip()
        self.play(Create(square), run_time=2)

class DifferentRotations(Scene):
    def construct(self):
        left_square=Square(color=BLUE,fill_opacity=0.7).shift(2*LEFT)
        right_square=Square(color=GREEN,fill_opacity=0.7).shift(2*RIGHT)
        self.play(left_square.animate.rotate(PI),Rotate(right_square,angle=PI),run_time=3)
        self.wait()

class TwoTransforms(Scene):
    def transform(self):
        a=Circle()
        b=Square()
        c=Triangle()
        self.play(Transform(a,b))
        self.play(Transform(a,c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a=Circle()
        b=Square()
        c=Triangle()
        self.play(ReplacementTransform(a,b))
        self.play(ReplacementTransform(b,c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(1)
        self.replacement_transform()


class TransformCycle(Scene):
    def construct(self):
        a=Circle()
        t1=Square()
        t2=Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a, t))

