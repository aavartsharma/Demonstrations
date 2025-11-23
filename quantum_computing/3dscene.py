from manin import * 

class scene(ThreeDScene):
    def construct(self):
        axis = ThreeDAxes(
            x_range=[-6,6,1],
            y_range=[-6,6,1],
            z_range=[-6,6,1]
            x_length=8,
            y_length=8,
            z_length=8
        )
