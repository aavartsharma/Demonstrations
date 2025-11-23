from manim import *
import numpy as np

class QubitAxisScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=45*DEGREES)

        axes = ThreeDAxes()

        ket_0 = MathTex(r"|0\rangle").move_to([0, 0, 2.2])
        ket_1 = MathTex(r"|1\rangle").move_to([0, 0, -2.2])
        ket_plus = MathTex(r"|+\rangle").move_to([2.2, 0, 0])
        ket_minus = MathTex(r"|-\rangle").move_to([-2.2, 0, 0])
        ket_i = MathTex(r"|i\rangle").move_to([0, 2.2, 0])
        ket_minus_i = MathTex(r"|-i\rangle").move_to([0, -2.2, 0])

        labels = [ket_0, ket_1, ket_plus, ket_minus, ket_i, ket_minus_i]

        # make every label face the camera
        for lb in labels:
            lb.add_updater(
                lambda m: m.rotate(
                    angle=self.camera.get_theta(), axis=OUT
                ).rotate(
                    angle=self.camera.get_phi(), axis=RIGHT
            )

        self.play(Create(axes))
        self.play(*[FadeIn(lb) for lb in labels])

        #self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()

