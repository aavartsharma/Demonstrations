from manim import *
import random

class TwentyBits(Scene):
    def construct(self):
        bits = VGroup()

        # Create 20 random bits (0/1)
        for _ in range(20):
            bit = Text(str(random.randint(0, 1)), font_size=48)
            bit.shift(
                np.array([
                    random.uniform(-5, 5),   # x
                    random.uniform(-3, 3),   # y
                    0                        # z
                ])
            )
            bits.add(bit)

        # Animate bits popping onto screen one-by-one
        for bit in bits:
            self.play(
                FadeIn(bit, scale=0.1),
                run_time=0.15
            )

        self.wait(1)

