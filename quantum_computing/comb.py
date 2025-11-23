from manim import *
import random
import time

def gradient_shift(m, dt):
    new_colors = []
    for c in m.get_fill_colors():
        h, s, v = c.hsv  # extract hue, saturation, value
        h = (h + 0.1 * dt) % 1.0
        new_colors.append(Color(hsv=(h, s, v)))

    m.set_fill(color=new_colors)
class BitGrid(Scene):
    def construct(self):
        text = MathTex('2^{1} = 2')
        text.to_edge(DOWN)
        circle_1 = Circle(radius=1,stroke_width=3)
        circle_1.set_fill(color=[BLUE,BLACK,PURPLE],opacity=1)
        circle_1.add_updater(
    lambda m, dt: m.set_fill(color=interpolate_color(BLUE, RED, (time.time() % 1)))
)
        group_bit = VGroup(circle_1,Text(str(random.randint(0, 1)), font_size=64))
        group_bit.move_to(ORIGIN+UP)
        self.play(FadeIn(group_bit))
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(group_bit))
        self.wait(0.5)
        num_bits = 20
        bits = VGroup()

        # Create bit circles
        for _ in range(num_bits):
            value = Text(str(random.randint(0, 1)), font_size=32)

            circle = Circle(radius=0.4, stroke_width=2)
            circle.set_fill(color=[BLUE,BLACK,PURPLE],opacity=1)
            circle.set_stroke(RED, width=2)

            circle.add_updater(gradient_shift)
            #circle.set_color(YELLOW)

            # Put the bit text inside the circle
            group = VGroup(circle, value)
            value.move_to(circle.get_center())
            bits.add(group)

        # Arrange in a 4×5 grid
        bits.arrange_in_grid(
            rows=4,
            cols=5,
            buff=0.8    # space between items
        )

        # Pop animation in order
        for i in range(len(bits)):
            text2 = MathTex(f'2^{{{i+1}}} = {2**(i+1):,}') 
            text2.to_edge(DOWN)
            self.play(
                ReplacementTransform(text,(text:=text2),path_arc = PI+1)
                FadeIn(bits[i], scale=0.2),
                run_time=0.4
            )

        self.wait(4)


class AnimateGrid(Scene):
    def construct(self):

        items = VGroup()

        # Create some circles with bits
        for _ in range(20):
            t = Text(str(random.randint(0,1)), font_size=32)
            c = Circle(radius=0.4).set_stroke(WHITE, 2)
            group = VGroup(c, t)
            t.move_to(c.get_center())
            group.shift([random.uniform(-5,5), random.uniform(-3,3), 0])
            items.add(group)

        # Show scattered items
        # 1. Save original positions

        # 2. Arrange instantly (new positions)
        items.arrange_in_grid(rows=4, cols=5, buff=0.8)
        end_positions = [item.get_center() for item in items]

        # 3. Move each item from start → end
        for item, start, end in zip(items, start_positions, end_positions):
            item.move_to(start)  # jump it back to start

        self.play(
            *[
                item.animate.move_to(end)
                for item, end in zip(items, end_positions)
            ],
            run_time=2,
            lag_ratio=0.1   # cascade animation
        )

        self.wait()
