from manim import *

class bar_class():
    def __init__(self):
        self.label = label
        self.color_border = color_border
        self.color = color
        self.width = width
        self._object = None
    def __call__(self,color_border,color, label='',width=4):
        if(self._object):
            return self._object
        self.bar_frame = Rectangle(
            width=self.width,
            height=0.4,
            stroke_width=3,
            color=self.color_border
        )

        # Filled health portion (start full)
        self.bar_fill = Rectangle(
            width=self.width,
            height=0.4,
            color=self.color,
            fill_opacity=1,
            stroke_width=0,
        )
        self.bar_fill.align_to(self.bar_frame, LEFT)  # anchor on the left

        # Text label
        label = Text(self.label, font_size=28)
        label.next_to(self.bar_frame, LEFT, buff=0.2)

        # Group them
        health_bar = VGroup(self.bar_frame, self.bar_fill, label)
        self._object = health_bar
        return health_bar
    def bar_object(self):
        # Empty frame (border of health bar)
        if(self._object):
            return self._object
        self.bar_frame = Rectangle(
            width=self.width,
            height=0.4,
            stroke_width=3,
            color=self.color_border
        )

        # Filled health portion (start full)
        self.bar_fill = Rectangle(
            width=self.width,
            height=0.4,
            color=self.color,
            fill_opacity=1,
            stroke_width=0,
        )
        self.bar_fill.align_to(self.bar_frame, LEFT)  # anchor on the left

        # Text label
        label = Text(self.label, font_size=28)
        label.next_to(self.bar_frame, LEFT, buff=0.2)

        # Group them
        health_bar = VGroup(self.bar_frame, self.bar_fill, label)
        self._object = health_bar
        return health_bar
    def bar_change(self,fill): # 0< fill<1
        # return the animation so value should be played
        return self.bar_fill.animate.stretch_to_fit_width(self.width*fill).align_to(self.bar_frame, LEFT)


class HealthBarExample(Scene):
    def construct(self):
        bar1 = bar_class(RED,GOLD,50, 'aavart',width=5)
        bar2 = bar_class(GREEN,BLUE,50, 'kinetic enegry',width=8)
        health_bar, bar_fill, bar_frame = bar1.bar_object()
        health_bar2, bar_fill2, bar_frame2 = bar2.bar_object()
        health_bar.to_edge(UL)

        self.play(FadeIn(health_bar))
        self.play(FadeIn(health_bar2))

        # Animate health decreasing (scale only width)
        self.play(
            bar1.bar_change(bar_fill,bar_frame,0.35),
            bar2.bar_change(bar_fill2,bar_frame2,0.01),
            run_time=2
        )

        self.wait(1)
