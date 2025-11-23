from manim import *
import numpy as np

class QuantumEntanglement(Scene):
    def construct(self):
        title = Text("Quantum Entanglement: Spin Correlation", font_size=38)
        title.to_edge(UP)

        # Electrons
        e1 = Dot(radius=0.25, color=BLUE).shift(LEFT*3)
        e2 = Dot(radius=0.25, color=RED).shift(RIGHT*3)

        e1_label = Text("Electron A", font_size=28).next_to(e1, UR)
        e2_label = Text("Electron B", font_size=28).next_to(e2, UR)

        # Two arrows per electron (superposition "wobble")
        # Arrow set A
        a1 = Arrow(e1.get_center(), e1.get_center()+UP*1.5, color=YELLOW, stroke_width=8).set_opacity(0.3)
        a2 = Arrow(e1.get_center(), e1.get_center()+DOWN*1.5, color=YELLOW, stroke_width=8).set_opacity(0.3)

        # Arrow set B
        b1 = Arrow(e2.get_center(), e2.get_center()+DOWN*1.5, color=YELLOW, stroke_width=8).set_opacity(0.3)
        b2 = Arrow(e2.get_center(), e2.get_center()+UP*1.5, color=YELLOW, stroke_width=8).set_opacity(0.3)

        # Add to screen
        self.play(FadeIn(title))
        self.play(FadeIn(e1), FadeIn(e2))
        self.play(FadeIn(e1_label), FadeIn(e2_label))
        self.play(FadeIn(a1), FadeIn(a2), FadeIn(b1), FadeIn(b2))
        filcer = 1

        # Flicker animation (quantum uncertainty)
        flicker1 = AnimationGroup(
            a1.animate.set_opacity(0.1), a2.animate.set_opacity(0.5),
            lag_ratio=0.2, run_time=filcer
        )
        flicker2 = AnimationGroup(
            a1.animate.set_opacity(0.5), a2.animate.set_opacity(0.1),
            lag_ratio=0.2, run_time=filcer
        )

        flicker3 = AnimationGroup(
            b1.animate.set_opacity(0.1), b2.animate.set_opacity(0.5),
            lag_ratio=0.2, run_time=filcer
        )
        flicker4 = AnimationGroup(
            b1.animate.set_opacity(0.5), b2.animate.set_opacity(0.1),
            lag_ratio=0.2, run_time=filcer
        )

        # Repeat flicker before measurement
        for _ in range(4):
            self.play(flicker1, flicker3)
            self.play(flicker2, flicker4)

        # Measurement device
        meas = Rectangle(width=4.5, height=3, color=WHITE)
        meas.move_to(e1.get_center()).shift(RIGHT)
        meas_label = Text("Measure", font_size=24).next_to(meas, DOWN, buff=0.2)
        result_label_A = Text("Up spin", font_size=18).next_to(e1,RIGHT,buff=0.4)
        result_label_B = Text("DOWN spin", font_size= 18).next_to(e2,RIGHT,buff=0.4)

        self.play(
            FadeIn(meas,shift=RIGHT,run_time=2), 
            FadeIn(meas_label),
            FadeIn(result_label_A),
            FadeIn(result_label_B)
        )

        # Collapse arrows
        spinA = Arrow(e1.get_center(), e1.get_center()+UP*1.5, color=GREEN, stroke_width=8)
        spinB = Arrow(e2.get_center(), e2.get_center()+DOWN*1.5, color=GREEN, stroke_width=8)

        self.play(
            FadeOut(a1), FadeOut(a2),
            FadeIn(spinA),
            run_time=1.2
        )
        self.play(
            FadeOut(b1), FadeOut(b2),
            FadeIn(spinB),
            run_time=1.2
        )

        explanation = Text(
            "Spin states stay undefined until measured.\n"
            "Measuring A fixes B instantly — entanglement.",
            font_size=30
        ).to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(2)
