from manim import *

class SchrodingerCat(Scene):
    def construct(self):
        title = Text("Schrödinger's Cat Thought Experiment", font_size=36)
        title.to_edge(UP)
        self.play(FadeIn(title))

        # The box
        box = Square(side_length=4, color=WHITE, stroke_width=3)
        box.shift(LEFT*3)

        # Cat silhouette (simple but readable)
        cat = SVGMobject("cat.svg") if False else Circle(radius=0.4, color=BLUE)  
        # Using a circle as placeholder; replace with SVG later.
        cat.move_to(box.get_center())

        # Radioactive atom and detector
        atom = Star(stroke_width=2, fill_opacity=0.2, color=YELLOW).scale(0.3)
        atom.next_to(box, RIGHT, buff=2)

        detector = Rectangle(width=1, height=1.5, color=WHITE)
        detector.next_to(atom, DOWN, buff=0.4)
        detector_label = Text("Detector", font_size=24).next_to(detector, DOWN, buff=0.1)

        poison = SVGMobject("skull.svg") if False else Square(fill_opacity=0.3, color=RED)
        poison.scale(0.4)
        poison.next_to(detector, DOWN)

        self.play(FadeIn(box), FadeIn(cat))
        self.play(FadeIn(atom), FadeIn(detector), FadeIn(detector_label), FadeIn(poison))

        # Atom pulsing (unstable quantum event)
        pulse = atom.animate.set_fill(opacity=0.6)
        pulse_back = atom.animate.set_fill(opacity=0.2)

        for _ in range(3):
            self.play(pulse, run_time=0.6)
            self.play(pulse_back, run_time=0.6)

        # Superposition state: Cat Alive + Cat Dead (ghost copies)
        cat_alive = cat.copy().set_color(GREEN).set_opacity(0.7).shift(UP*0.7)
        cat_dead = cat.copy().set_color(RED).set_opacity(0.7).shift(DOWN*0.7)

        super_text = Text("Superposition:\nCat Alive + Cat Dead", font_size=28)
        super_text.next_to(box, DOWN)

        # Fade in the two states
        self.play(
            FadeOut(cat),
            FadeIn(cat_alive),
            FadeIn(cat_dead),
            FadeIn(super_text),
            run_time=2
        )

        self.wait(1)

        # Box opens (measurement)
        open_box = box.copy().shift(RIGHT*4).set_color(YELLOW)
        measure_label = Text("Measurement", font_size=30).next_to(open_box, UP, buff=0.2)

        self.play(FadeIn(open_box), FadeIn(measure_label))

        # Collapse — choose alive randomly (you can flip it)
        final_cat = cat_alive.copy().set_opacity(1).set_color(GREEN)
        final_cat.move_to(open_box.get_center())

        collapse_text = Text("Collapse:\nCat is Alive", font_size=28).next_to(open_box, DOWN)
        
        self.play(
            FadeOut(cat_dead),
            FadeOut(cat_alive),
            FadeIn(final_cat),
            FadeIn(collapse_text),
            run_time=2
        )

        self.wait(2)
