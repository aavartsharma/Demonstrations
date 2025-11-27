from manim import *
from qubit import qubit

class p1(ThreeDScene):
    def construct(self):
        q_1 = qubit.qubit()
        vec_coor = [1.5,1.5,1.5]
        self.move_camera(phi=60*DEGREES, theta=0)
        self.begin_ambient_camera_rotation(rate=40*DEGREES,about='theta')
        vec1 = Arrow3D(
                start=[0,0,0],
                end=vec_coor,
                resolution=16
        )
        vec1.set_color(GREEN)
        self.play(FadeIn(q_1))
        self.play(FadeIn(vec1))
        self.wait(4)




