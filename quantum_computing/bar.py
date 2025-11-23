from manim import *
import numpy as np

class ClassicalVsQuantum(Scene):
    def construct(self):
        # ---------- TEXT ----------
        classical_label = Text("Classical Mechanics", font_size=36)
        quantum_label   = Text("Quantum Mechanics", font_size=36)

        classical_label.to_edge(UP).shift(LEFT*3)
        quantum_label.to_edge(UP).shift(RIGHT*3)

        # ---------- DIVIDER BAR ----------
        divider = Rectangle(height=6, width=0.1, color=WHITE, fill_opacity=1)
        divider.move_to(ORIGIN)

        # ---------- CLASSICAL SIDE ----------
        ball = Dot(radius=0.2, color=BLUE)
        ball.move_to(LEFT*3)

        # Barrier line under classical curve
        classical_bar = Rectangle(height=0.2, width=3, fill_opacity=1, color=GREY)
        classical_bar.next_to(ball, DOWN, buff=1)

        # ---------- QUANTUM SIDE ----------
        wave = FunctionGraph(
            lambda x: np.exp(-(x*0.6)**2),
            x_range=[-4, 4],
            color=YELLOW
        )
        wave.shift(RIGHT*3 + DOWN*1.5)

        # ---------- ANIMATION SETUP ----------
        self.play(
            FadeIn(classical_label),
            FadeIn(quantum_label),
            FadeIn(divider),
        )

        self.play(FadeIn(ball), FadeIn(classical_bar))
        self.play(FadeIn(wave))

        # Move ball → hit imaginary barrier → bounce
        self.play(ball.animate.shift(RIGHT*2.5), run_time=2)
        self.play(ball.animate.shift(LEFT*2.5), run_time=2)

        # Quantum wave "leaks" (tunneling effect look)
        self.play(wave.animate.shift(RIGHT*1), run_time=2)

        self.wait(1)
