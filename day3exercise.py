from manim import *
import numpy as np

class Practice(Scene):
    def construct(self):
        # Create axes without numbers
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={'include_numbers': False}  # disable LaTeX-based numbers
        )

        # Add manual axis labels
        axis_labels = VGroup(
            Text("x", font="Arial").next_to(ax.x_axis.get_end(), RIGHT),
            Text("y", font="Arial").next_to(ax.y_axis.get_end(), UP)
        )

        # Lemniscate curve
        lemniscate = ax.plot_parametric_curve(
            lambda t: np.array([
                (np.sqrt(2) * np.cos(t)) / (1 + np.sin(t) ** 2),
                (np.sqrt(2) * np.cos(t) * np.sin(t)) / (1 + np.sin(t) ** 2),
                0
            ]),
            t_range=[0, TAU],
            color=BLUE
        )

        # Label for the curve
        curve_label = Text("Bernoulli", font="Arial").next_to(
            lemniscate.point_from_proportion(0.25), UP
        )
        # Dot moving along the curve
        dot = Dot(color=YELLOW).move_to(lemniscate.point_from_proportion(0))

        # Animate everything
        self.play(Create(ax), Write(axis_labels))
        self.play(Create(lemniscate), Write(curve_label))
        self.add(dot)
        self.play(MoveAlongPath(dot, lemniscate), run_time=6, rate_func=linear)
        self.wait()
