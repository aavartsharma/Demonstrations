from manim import *
from modles import into

class a(Scene):
    def construct(self):
        t = init.transistor()
        self.play(FadeIn(t))


