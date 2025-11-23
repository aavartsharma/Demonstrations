
from manim import *

class ComputerIntro(Scene):
    def construct(self):
        # Title
        title = Text("What Is a Computer?", font_size=10)
        self.play(Write(title))
        self.wait(1)

        # Move title up
        self.play(title.animate.to_edge(UP))

        # Three concepts that appear one by one
        idea1 = Text("• Input", font_size=6).next_to(title, DOWN, buff=1)
        idea2 = Text("• Processing", font_size=6).next_to(idea1, DOWN)
        idea3 = Text("• Output", font_size=6).next_to(idea2, DOWN)

        self.play(FadeIn(idea1, shift=RIGHT))
        self.play(FadeIn(idea2, shift=RIGHT))
        self.play(FadeIn(idea3, shift=RIGHT))
        self.wait(0.5)

        # A little underline to make it feel dynamic
        underline = Line(
            idea2.get_left() + 0.1*DOWN,
            idea2.get_right() + 0.1*DOWN
        ).set_color(YELLOW)
        self.play(Create(underline))
        self.wait(0.5)

        # A “data flow arrow” animation
        arrow = Arrow(
            idea1.get_right() + RIGHT*0.5,
            idea3.get_right() + RIGHT*0.5,
            buff=0.2,
            stroke_width=6
        ).set_color(BLUE)

        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Label on the arrow
        flow_label = Text("Data Flow", font_size=36).move_to(arrow.get_center() + UP*0.4)
        self.play(Write(flow_label))
        self.wait(2)
