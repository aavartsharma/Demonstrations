
from manim import *

class ComputerIntro(Scene):
    def construct(self):
        # Title
        title = Text("What Is a Computer?", font_size=60)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        answer = Paragraph("""A computer is a programmable device that stores, retrieves, and processes data.\n The term "computer" was originally given to humans (human computers) \n who performed numerical calculations using mechanical calculators,\n such as the abacus and slide rule. \nThe term was later given to mechanical devices as they began replacing human computers.\n Today's computers are electronic devices that accept data (input),\n process that data, produce output, and store (storage) the results (IPOS)""", font_size = 25, alignment='center').move_to(ORIGIN)

        # Move title up
        self.play(Write(answer))

        self.wait(15)

