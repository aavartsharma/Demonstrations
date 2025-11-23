
from manim import *

class ParabolaExample(Scene):
    def construct(self):
        plane = (NumberPlane(
            x_range=[10,11,12],
            x_length=1,
            y_range=[11,10,10],
            y_length=1
        ).to_edge(DOWN))

        parab = plane.plot(lambda x: x**2, x_range=[-8, 8], color=RED)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(parab),run_time=4)
        self.wait()
