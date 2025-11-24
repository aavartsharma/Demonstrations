
from manim import *
import numpy as np

def transistor():
    body = Circle(radius=0.6)
    angle = PI/4

    def point(circle, angle):
        return circle.get_center() + np.array([
            circle.radius*np.cos(angle),
            circle.radius*np.sin(angle),
            0
        ])

    collector = Line(point(body, angle), point(body, angle) + UP*1)
    emitter = Line(point(body, angle + (3*PI/2)), point(body, angle + (3*PI/2)) + DOWN*1)
    inner_line = Line(body.get_center() + LEFT*0.2 + UP*0.4,
                      body.get_center() + LEFT*0.2 + DOWN*0.4,
                      stroke_width=10)
    connect1 = Line(point(body, angle), inner_line.get_top() + DOWN*0.25)
    connect2 = Line(point(body, angle + (3*PI/2)), inner_line.get_bottom() + UP*0.25)

    base = Line(inner_line.get_center(), body.get_left() + LEFT*1)

    return VGroup(body, collector, emitter, base, inner_line, connect1, connect2)


class ElectronFlow(Scene):
    def construct(self):
        t = transistor()
        self.play(Create(t))

        # --- electron characteristics ---
        electron_color = BLUE
        electron_radius = 0.08

        # Paths for electrons
        collector_path = Line(t[1].get_end() + UP*0.3,   t[1].get_start())
        through_body     = Line(t[1].get_start(), t[4].get_top())
        down_inner       = Line(t[4].get_top(),   t[4].get_bottom())
        emitter_path     = Line(t[4].get_bottom(), t[2].get_start())
        exit_path        = Line(t[2].get_start(), t[2].get_end() + DOWN*0.3)

        full_path = VMobject().set_points_as_corners([
            collector_path.get_start(),
            collector_path.get_end(),
            through_body.get_end(),
            down_inner.get_end(),
            emitter_path.get_end(),
            exit_path.get_end()
        ])

        # Multiple electrons generated in a loop
        electrons = []
        animations = []

        for i in range(12):   # number of electrons
            e = Dot(color=electron_color, radius=electron_radius)
            electrons.append(e)
            self.add(e)

            anim = MoveAlongPath(
                e,
                full_path,
                rate_func=linear,
                run_time=3
            )

            # Delay start times so they look like a stream
            animations.append(AnimationGroup(
                Wait(i*0.25),
                anim
            ))

        # Play all electron streams overlapped
        self.play(*animations, lag_ratio=0.1)

        self.wait(2)

