from manim import *
import numpy as np

class qubit():
    def qubit():
        axis = ThreeDAxes()
        #sphere = Sphere(center=(0,0,0), radius=1, resolution=(12,12), fill_opacity=0.2)
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.2
        )
        sphere.scale(1.5)
        sphere.set_color(BLUE)
        x_label = axis.get_x_axis_label(MathTex(r"|0\rangle"))
        x_label_n = axis.get_x_axis_label(
            MathTex(r"|1\rangle"),
            direction=DOWN,
            buff=0.1,
            edge=LEFT  # pushes the label to the negative side
        )        
        y_label = axis.get_y_axis_label(MathTex(r"|i\rangle"))
        y_label_n = axis.get_y_axis_label(
            MathTex(r"|-i\rangle"),
            direction=LEFT,
            buff=0.1,
            edge=DOWN  # pushes the label to the negative side
        ) 
        z_label = axis.get_z_axis_label(MathTex(r"|+\rangle"))
        z_label_n = axis.get_z_axis_label(
            MathTex(r"|-\rangle"),
            direction=LEFT,
            buff=0.1,
            edge=IN # pushes the label to the negative side
        )
        qu = VGroup(sphere,axis,*[x_label,y_label,z_label,x_label_n,y_label_n,z_label_n])
        return qu
        #self.play(Write(axis),*[Write(i) for i in [x_label,y_label,z_label,x_label_n,y_label_n,z_label_n]])
        #self.play(Write(sphere))

class qubit_scene(ThreeDScene):
    
    def construct(self):

        vec_coor = np.array([4*0.5,4*0.5,4*0.25])        
        self.set_camera_orientation(phi=PI/6, theta=PI/6)
        axis = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32),fill_opacity=0.2
        )
        sphere.set_color(BLUE)
        x_label = axis.get_x_axis_label(MathTex(r"|0\rangle"))
        x_label_n = axis.get_x_axis_label(
            MathTex(r"|1\rangle"),
            direction=DOWN,
            buff=0.1,
            edge=LEFT  # pushes the label to the negative side
        )        
        y_label = axis.get_y_axis_label(MathTex(r"|i\rangle"))
        y_label_n = axis.get_y_axis_label(
            MathTex(r"|-i\rangle"),
            direction=LEFT,
            buff=0.1,
            edge=DOWN  # pushes the label to the negative side
        ) 
        z_label = axis.get_z_axis_label(MathTex(r"|+\rangle"))
        z_label_n = axis.get_z_axis_label(
            MathTex(r"|-\rangle"),
            direction=LEFT,
            buff=0.1,
            edge=IN # pushes the label to the negative side
        )
        self.renderer.camera.light_source.move_to(3*IN)
        self.move_camera(phi=60*DEGREES, theta=0)
        self.begin_ambient_camera_rotation(rate=40*DEGREES, about='theta')
        vec1 = Arrow3D(
                start=[0,0,0],
                end=vec_coor,
                resolution=16
        )
        vec1.set_color(GREEN)
        self.add(vec1)
        self.play(Write(axis),*[Write(i) for i in [x_label,y_label,z_label,x_label_n,y_label_n,z_label_n]])
        sphere.scale(1.5)
        self.play(Write(sphere))
        self.wait(3)
