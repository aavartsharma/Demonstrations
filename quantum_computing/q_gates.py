from manim import *

class q_gates():
    def gate(label, color=WHITE):
        box = Square(side_length=1.2, color=color)
        text = MathTex(label)
        text.scale(0.9)
        text.move_to(box.get_center())
        return VGroup(box, text)

class QuantumGates(Scene):
    def construct(self):

        # Function to create a square gate with a label
        def gate(label, color=WHITE):
            box = Square(side_length=1.2, color=color)
            text = MathTex(label)
            text.scale(0.9)
            text.move_to(box.get_center())
            return VGroup(box, text)

        # Create gates
        gate_x = gate("X")
        gate_y = gate("Y")
        gate_z = gate("Z")
        gate_h = gate("H")  # Hadamard

        # Arrange them horizontally
        gates = VGroup(gate_x, gate_y, gate_z, gate_h)
        gates.arrange(RIGHT, buff=1.2)

        # Animate creation
        self.play(Create(gates), run_time=2)
        self.wait(1)

        # Fade in gate labels (write animation)
        for g in gates:
            self.play(Write(g[1]), run_time=0.7)

        self.wait(2)



class QuantumCircuit(Scene):
    def construct(self):

        # --- helper: quantum gate box ---
        def gate(label):
            box = Square(side_length=1, color=WHITE)
            txt = MathTex(label)
            txt.move_to(box.get_center())
            return VGroup(box, txt)

        # --- wires ---
        wire1 = Line(LEFT*5, RIGHT*5).shift(UP*1)
        wire2 = Line(LEFT*5, RIGHT*5).shift(DOWN*1)

        self.play(Create(wire1), Create(wire2))

        # labels |ψ> and |0>
        psi_label = MathTex(r"| \psi \rangle").next_to(wire1, LEFT)
        zero_label = MathTex(r"| 0 \rangle").next_to(wire2, LEFT)

        self.play(FadeIn(psi_label), FadeIn(zero_label))

        # --- quantum gates ---
        X = gate("X")
        Y = gate("Y")
        Z = gate("Z")
        H = gate("H")

        # place them on wire1
        X.move_to(wire1.point_from_proportion(0.25))
        Y.move_to(wire1.point_from_proportion(0.45))
        Z.move_to(wire1.point_from_proportion(0.65))
        H.move_to(wire1.point_from_proportion(0.85))

        # animation: one gate at a time
        for g in [X, Y, Z, H]:
            self.play(FadeIn(g[0]), run_time=0.4)  # box
            self.play(Write(g[1]), run_time=0.4)   # letter

        self.wait(2)
