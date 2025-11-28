from manim import *
from q_gates import q_gates 
from models import logic_gate
from qubit import qubit

class a(Scene):
    def construct(self):
        line = Line(
            start=[0,-config.frame_height/2, 0],
            end=[0, config.frame_height/2,  0],
            stroke_width=4
        )
        class_label = Text("classical Logic Gate").next_to(line, LEFT,buff=0.4).to_edge(UP)
        classical_gate = logic_gate.OrGate().next_to(line,LEFT,buff=2.5)
        input_A = Text("1").scale(0.5).next_to(classical_gate[0][3],LEFT,buff=0.5)
        input_B = Text("0").scale(0.5).next_to(classical_gate[0][5],LEFT,buff=0.5)
        result = Text("1").scale(0.5).next_to(classical_gate[0][-1],RIGHT,buff=0.5)

        classical_gate.add(input_A,input_B,result)

        q_label = Text("Quantum gate").next_to(line,RIGHT,buff=2).to_edge(UP)
        x_gate = q_gates.gate("X").next_to(line,RIGHT,buff=3).scale(0.75)
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.2
        )
        #video = Video("media/videos/qubit_scene/1080p60/qubit_scene.mp4").next_to(line,RIGHT,buff=2)
        p1=ImageMobject('photos/pics/p10203.png').scale(0.25).move_to(x_gate.get_center()).shift(LEFT*2)
        p2 = ImageMobject('photos/pics/p10419.png').scale(0.25).move_to(x_gate.get_center()).scale(0.01)
        self.play(Create(line))
        #self.add(sphere)
        self.play(Write(class_label),Write(q_label))
        self.play(FadeIn(classical_gate))
        self.play(FadeIn(x_gate))
        self.play(Circumscribe(input_A,color=YELLOW,buff=0.2))
        self.play(Circumscribe(input_B,color=YELLOW,buff=0.2))
        self.play(Circumscribe(result,color=YELLOW,buff=0.2))

        self.play(
            p1.animate.move_to(x_gate.get_center()).scale(0.01),
            run_time=3,
            rate_func=smooth
        )
        self.play(FadeOut(p1))
        self.play(
            p2.animate.shift(RIGHT*2.5).scale(75),
            run_time=3,
            rate_func=smooth
        )

        self.wait(5)
