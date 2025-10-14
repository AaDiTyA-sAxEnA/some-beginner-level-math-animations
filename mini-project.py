from manim import *

class ex_shape(Scene):
    def construct(self):
        square=Square()
        square.set_fill(color=BLUE,opacity=1)

        self.play(Create(square))
        self.play(Rotate(square,angle=PI/4))
        self.play(square.animate.move_to(RIGHT*2))
        self.play(Rotate(square,angle=PI*0.75))
        self.play(square.animate.move_to(ORIGIN))
        self.play(FadeOut(square))

class ex_graph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-PI/2, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],  # y from -1.5 to 1.5
            x_length=10,
            y_length=4,
            axis_config={'include_numbers': False}  # disable LaTeX-based numbers
        )
        graph1 = ax.plot(lambda x: np.sin(x), use_smoothing=False, color=BLUE)
        graph2 = ax.plot(lambda x: np.cos(x), use_smoothing=False, color=RED)

        #graph3 = ax.plot(lambda x: np.arcsin(x), use_smoothing=False, color=GREEN)
        #graph4 = ax.plot(lambda x: np.arccos(x), use_smoothing=False, color=PURPLE)
        #to run inverse graphs make range of x&y appropriate

        self.add(ax, graph1, graph2)
        self.play(Create(ax))
        self.play(Create(graph1))
        self.play(Create(graph2))
        self.play(Rotate(graph1,angle=PI/4))
        self.play(Rotate(graph2,angle=PI*0.75))



