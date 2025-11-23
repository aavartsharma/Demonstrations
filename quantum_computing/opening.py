from manim import *
from qubit import qubit
from q_gates import q_gates
import numpy as np

class opening(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI/6, theta=PI/6)
        qu = qubit.qubit()
        self.move_camera(phi=60*DEGREES, theta=0)

        self.begin_ambient_camera_rotation(rate=40*DEGREES, about='theta')
        vec1 = Arrow3D(
                start=[0,0,0],
                end=[1/(3**0.5),1/(3**0.5),1/(3**0.5)],
                resolution=16
        )
        vec1.set_color(GREEN)
        
        self.play(Write(qu),run_time = 2)
        self.play(FadeIn(vec1))
        all_qu = VGroup(qu,vec1)
        self.wait(3)

        plane = NumberPlane(
            background_line_style={"stroke_opacity": 0.4}
        )

        # Vector endpoint (x, y)
        vec_end = np.array([0.45, 0.34, 0])

        # Create the vector
        vector = Vector(vec_end, color=YELLOW)

        # Label for vector
        label = MathTex(r"|\psi\rangle = (0.45,0.34)")
        label.next_to(vector.get_end(), UR, buff=0.2)
        
        self.move_camera(phi=0, theta=-PI/2, run_time=2)
        self.stop_ambient_camera_rotation()

        plan = VGroup(plane,vector,label)
        self.play(ReplacementTransform(all_qu,plan))
        self.wait(5)
        eq = MathTex(r"|\psi\rangle = a|0\rangle + b|1\rangle")

        # Make it large and centered
        eq.scale(1.5)

        # Animate writing the equation
        self.wait(3)
        self.play(ReplacementTransform(plan,eq), run_time=2)
        X = q_gates.gate("X")
        Y = q_gates.gate("Y")
        Z = q_gates.gate("Z")
        H1 = q_gates.gate("H")
        H2 = q_gates.gate("H")
        H3 = q_gates.gate("H")

        wire1 = Line(LEFT, RIGHT).shift(UP*1)
        wire2 = Line(LEFT, RIGHT).shift(DOWN*1)
        wire3 = Line(LEFT, RIGHT).shift(DOWN*3)
        X.next_to(wire1,RIGHT,buff=0.05)
        Y.next_to(wire2,RIGHT,buff=0.05)
        Z.next_to(wire3,RIGHT,buff=0.05)
        wire4 = Line(X.get_right(), X.get_right()+RIGHT)
        wire5 = Line(Y.get_right(), Y.get_right()+RIGHT) 
        wire6 = Line(Z.get_right(), Z.get_right()+RIGHT)

        H1.next_to(wire4.get_right(), RIGHT, buff=0.05)
        H2.next_to(wire5.get_right(), RIGHT, buff = 0.05)
        H3.next_to(wire6.get_right(), RIGHT, buff= 0.05)

        wire7 = Line(H1.get_right(), H1.get_right()+RIGHT)
        wire8 = Line(H2.get_right(), H2.get_right()+RIGHT) 
        wire9 = Line(H3.get_right(), H3.get_right()+RIGHT)


        label_0 = MathTex(r"| \psi_{0} \rangle").next_to(wire1, LEFT)
        label_1 = MathTex(r"| \psi_{1} \rangle").next_to(wire2, LEFT)
        label_2 = MathTex(r'| \psi_{2} \rangle').next_to(wire3, LEFT)
        label_3 = MathTex(r"| \psi_{3} \rangle").next_to(wire7, RIGHT)
        label_4 = MathTex(r"| \psi_{4} \rangle").next_to(wire8, RIGHT) 
        label_5 = MathTex(r'| \psi_{5} \rangle').next_to(wire9, RIGHT)

        q_cir = VGroup(*[X,Y,Z,H1,H2,H3,wire1,wire2,wire3,wire4,wire5,wire6,wire7,wire8,wire9,label_0,label_1,label_2,label_3,label_4,label_5]).move_to(ORIGIN)
        self.play(ReplacementTransform(eq,q_cir), run_time=2)



        #self.play(*[FadeIn(i) for i in [X,Y,X,H1,H2,H3,wire2,wire3,wire4,wire5,wire6,label_0,label_1,label_2,label_3,label_4,label_5]]) 




        # Animate drawing the vector

        self.wait(4)
        
