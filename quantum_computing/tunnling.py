from manim import *
from random import randint as random
from health_bar import bar_class 

class ClassicalVsQuantum(Scene):
    def construct(self):
        # Classical ball
        title = Text("Classical Mechanics").scale(0.7)
        title.to_edge(UP)
        ball_radius =0.3
        ball = Dot(radius=ball_radius, color=GOLD)
        ball.move_to(LEFT*3)
        f = lambda x: np.exp((-(0.6*x)**2)+1)
        # Quantum wave packet (Gaussian-ish blob)
        wave = FunctionGraph(
            f,
            x_range=[-10, 10],
            color=PURPLE
        ).shift(DOWN*2)

        # kentic energy bar
        ke_bar_object = bar_class(WHITE,(170, 30, 150),'K.E',3)
        ke_bar_object.to_edge(UL)
        ke_anima= ke_bar.bar_change(0.8)

        pe_bar_object = bar_class(WHITE,YELLOW,'P.E',3)
        pe_bar_object.to_edge(UL).shift(DOWN*0.8)
        pe_anima = pe_bar.bar_change(0.5)
        # Text labeos
        start_x =-5 
        vec = Arrow(
            start=ball.get_center(),
            end=ball.get_center() + RIGHT*0.5,
            buff=0,              # makes it touch the ball directly
            stroke_width=4,
            color=RED
        )
        vec.move_to(np.array([start_x+ball_radius,f(start_x+ball_radius)+ball_radius,0])).shift(DOWN*2)
        ball.move_to(np.array([start_x,f(start_x)+ball_radius,0])).shift(DOWN*2)
        self.play(
            FadeIn(ke_bar_object),
            FadeIn(pe_bar_object),
            ke_anima,
            pe_anima,
            FadeIn(title),
            FadeIn(ball),
            FadeIn(wave)
        )
        self.wait(5)
        # Classical motion: the ball rolls, hits the barrier, bounces back
        #self.play(ball.animate.shift(RIGHT*2.5), run_time=2)
        #self.play(ball.animate.shift(LEFT*2.5), run_time=2)
        path_points = []
        for x in np.linspace(start_x,5,30):
            path_points.append(np.array([x, f(x)+ball_radius, 0])+DOWN*2)
        self.play(MoveAlongPath(
            ball,
            VMobject().set_points_as_corners(path_points)
        ),MoveAlongPath(
            vec,
            VMobject().set_points_as_corners(path_points).shift(np.array([ball_radius,0,0]))
        ),run_time=3,rate_func=lambda x: x**2)

        # Quantum motion: wave moves—some goes through
        # Animate by shifting a copy through the barrier
        classical_ball = VGroup(ball,wave,vec,title,ke_bar_object,pe_bar_object)
        self.play(FadeOut(classical_ball))
        self.wait(2)
        #self.play(FadeIn(classical_ball))
        path_points = [np.array([x,f(x)+ball_radius,0])+DOWN*2 for x in np.linspace(start_x,start_x+15,60)]
        ball.move_to(np.array([start_x,f(start_x)+ball_radius,0])).shift(DOWN*2)

        self.play(FadeIn(classical_ball)) 
        self.play(ke_bar_object.bar_change(0.3))
        self.play(MoveAlongPath(ball,VMobject().set_points_as_corners(path_points)),run_time=3, rate_func=lambda x: x*(1-x))


        ### -------- Quantum Mechanics -------- ###
        title_q = Text("Quantum Mechanics").scale(0.7)
        title_q.to_edge(UP)
        ball_radius =0.5
        e = Dot(radius=ball_radius, color=GRAY)
        ball_text = Text('e-',color=WHITE).scale(0.5).move_to(e.get_center())
        q_ke_bar = bar_class(WHITE,(120,120,102),'K.E',3)  
        e = VGroup(e,ball_text)

        e.move_to(LEFT*3)
        f = lambda x: np.exp((-(3*x)**2)+1)
        # Quantum wave packet (Gaussian-ish blob)
        wave_1 = FunctionGraph(
            f,
            x_range=[-10, 10],
            color=PURPLE
        ).shift(DOWN*2)

        # Text labeos
        start_x =-5 
        e.move_to(np.array([start_x,f(start_x),0]))

        # Classical motion: the ball rolls, hits the barrier, bounces back
        #self.play(ball.animate.shift(RIGHT*2.5), run_time=2)
        #self.play(ball.animate.shift(LEFT*2.5), run_time=2)
        path_points = []
        for x in np.linspace(start_x,5,30):
            path_points.append(np.array([x, 0.5*random(-2,1), 0]))
        Quantum_elec = VGroup(title_q,e,ball_text,wave_1)
        self.wait(3)
        self.play(
            FadeOut(classical_ball,shift=RIGHT)
        )
        self.wait(2.5)
        self.play(FadeIn(Quantum_elec,shift=LEFT))
        for x in range(start_x,5):
            if(x==0):
                continue
            self.play(FadeOut(e,run_time=0.2))
            e.move_to(np.array([x,0.5*random(-2,1), 0]))
            self.play(FadeIn(e,run_time=0.2))
        self.wait(3)
        #self.play(MoveAlongPath(
        #    e,
        #    VMobject().set_points_as_corners(path_points),
        #    FadeOut(e, run_time=0.5)
        #),run_time=3,rate_func=linear)
        
        self.play(FadeIn(e, run_time=0.5))


        #self.play(classical_ball.animate.scale(0.25))
        #self.play(classical_ball.animate.shift(LEFT*2))




        # Show faint tunneled part

        self.wait()
