from manim import * 

class test(Scene):
    def construct(self):
        name = Text("Aavart").to_edge(UR, buff=1)
        square = Square()
        cir = Circle(radius=2).to_edge(DR,buff=1)

        # Show the square
        self.play(Create(square),Create(cir))

        # Transform into a circle
        self.play(Transform(square, Circle()))
        self.play(Transform(cir, Arrow(start=LEFT, end=DOWN, buff=1,color=BLUE)))
        # Fade it out
        
        self.play(FadeOut(square),Write(name))
        self.play(name.animate.scale(0.5),cir.animate.to_edge(UL,buff=0.5),run_time=3)
        self.play(Axis())
        self.wait()



