from manim import *
import numpy as np
import random

class QubitBloch(ThreeDScene):
    def bloch_vector(self, theta, phi):
        return np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta)
        ])

    def state_amplitudes(self, theta, phi):
        # global phase ignored: |ψ> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>
        alpha = np.cos(theta / 2)
        beta = np.sin(theta / 2) * np.exp(1j * phi)
        return alpha, beta

    def construct(self):
        # camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # sphere + axes
        sphere = Sphere(radius=1, resolution=(36, 36)).set_opacity(0.2).set_color(BLUE_E)
        axes = ThreeDAxes(x_range=[-1.2, 1.2, 1], y_range=[-1.2, 1.2, 1], z_range=[-1.2, 1.2, 1])
        labels = VGroup(
            MathTex(r"|0\\rangle").move_to(UP * 1.15),
            MathTex(r"|1\\rangle").move_to(DOWN * 1.15),
            MathTex(r"|+\\rangle").move_to(RIGHT * 1.15),
            MathTex(r"|-\\rangle").move_to(LEFT * 1.15)
        )

        # value trackers for spherical angles
        theta = ValueTracker(0.0)   # 0 => |0>
        phi = ValueTracker(0.0)

        # arrow always redraws to current theta,phi
        def make_arrow():
            end = self.bloch_vector(theta.get_value(), phi.get_value())
            return Arrow(ORIGIN, end, buff=0, stroke_width=6, color=YELLOW)

        state_arrow = always_redraw(make_arrow)
        tip_dot = always_redraw(lambda: Dot(self.bloch_vector(theta.get_value(), phi.get_value()), radius=0.05, color=YELLOW))

        # amplitude/probability text (always updating)
        amp_text = always_redraw(lambda: MathTex(
            rf"\alpha = {self.state_amplitudes(theta.get_value(), phi.get_value())[0]:.3f}",
            rf"\quad \beta = {self.state_amplitudes(theta.get_value(), phi.get_value())[1]:.3f}"
        ).to_corner(UR))

        prob_text = always_redraw(lambda: MathTex(
            rf"|\\alpha|^2 = {abs(self.state_amplitudes(theta.get_value(), phi.get_value())[0])**2:.3f}",
            rf"\quad |\\beta|^2 = {abs(self.state_amplitudes(theta.get_value(), phi.get_value())[1])**2:.3f}"
        ).next_to(amp_text, DOWN))

        # initial scene
        self.play(Create(sphere), Create(axes), FadeIn(labels))
        self.play(FadeIn(state_arrow), FadeIn(tip_dot), Write(amp_text), Write(prob_text))
        self.wait(0.6)

        # Show initial state |0>
        self.play(Write(MathTex(r"Initial:\ |0\rangle").to_edge(UL)))
        self.wait(0.8)

        # Apply Hadamard ~ rotate to theta=pi/2, phi=0 (|+>)
        self.play(theta.animate.set_value(PI/2), phi.animate.set_value(0), run_time=2.0, rate_func=smooth)
        self.play(Write(MathTex(r"Apply\ H\ \Rightarrow\ |+\rangle").to_edge(UL)))
        self.wait(1.2)

        # Pause then apply Pauli-X which flips north<->south (theta -> pi - theta, phi -> phi + pi)
        # We'll animate to theta = pi - current theta
        target_theta = PI - theta.get_value()
        target_phi = phi.get_value() + PI
        self.play(theta.animate.set_value(target_theta), phi.animate.set_value(target_phi), run_time=2.0)
        self.play(Write(MathTex(r"Apply\ X\ \Rightarrow\ \text{flip}").to_edge(UL)))
        self.wait(1.0)

        # Return to arbitrary superposition (example: theta=pi/3, phi=pi/3)
        self.play(theta.animate.set_value(PI/3), phi.animate.set_value(PI/3), run_time=2.0)
        self.play(Write(MathTex(r"Arbitrary\ state").to_edge(UL)))
        self.wait(1.0)

        # Measurement simulation (probabilistic)
        alpha, beta = self.state_amplitudes(theta.get_value(), phi.get_value())
        p0 = abs(alpha) ** 2
        p1 = abs(beta) ** 2
        m_text = MathTex(rf"P(0)={p0:.3f}\quad P(1)={p1:.3f}").to_edge(DL)
        self.play(Write(m_text))
        self.wait(0.5)

        # simulate measurement outcome
        outcome = 0 if random.random() < p0 else 1
        outcome_tex = MathTex(rf"Measurement:\ |{outcome}\rangle").scale(1.2).to_edge(UL)
        # animate collapse: arrow jumps to north or south pole
        if outcome == 0:
            self.play(theta.animate.set_value(0), phi.animate.set_value(0), run_time=1.2)
        else:
            self.play(theta.animate.set_value(PI), phi.animate.set_value(0), run_time=1.2)
        self.play(FocusOn(tip_dot), Write(outcome_tex))
        self.wait(1.5)

        # finish
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(FadeOut(VGroup(m_text, outcome_tex)))
        
        self.wait(6)
