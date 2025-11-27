from manim import *
from health_bar import bar_class

class logic_gate():
    def __init__(self):
        pass
    def NotGate():
        # Triangle body
        tri = Polygon(
            LEFT*1 + UP*0.5,
            LEFT*1 + DOWN*0.5,
            ORIGIN+RIGHT*0.05,
            stroke_width=4
        )

        # Inversion bubble
        bubble = Circle(radius=0.1, stroke_width=4).next_to(tri, RIGHT, buff=0.05)

        body = VGroup(tri, bubble)
        line = Line(RIGHT*0.5,LEFT*0.5).next_to(body,LEFT*0.25)
        dot = Dot(color=RED,radius=0.05).move_to(line.get_left())
        line_right = Line(RIGHT*0.5,LEFT*0.5).move_to(body.get_right()).shift(RIGHT*0.5)
        dot_right = Dot(color=GREEN,radius=0.05).move_to(line_right.get_right())
        body.add(line,dot,line_right,dot_right)
        label = Text("NOT", font_size=28).next_to(body, DOWN, buff=0.1)


        return VGroup(body, label)

    def OrGate():
        left_curve_top = ArcBetweenPoints(LEFT*1 + UP*0.5, ORIGIN, angle=-PI/4)
        left_curve_bottom = ArcBetweenPoints(LEFT*1 + DOWN*0.5, ORIGIN, angle=PI/4)

        right_curve = ArcBetweenPoints(LEFT + UP*0.5, LEFT + DOWN*0.5, angle=-PI/1.5)

        body = VGroup(left_curve_top, left_curve_bottom, right_curve).set_stroke(width=4)

        p1 = right_curve.point_from_proportion(0.25)
        p2 = right_curve.point_from_proportion(0.75)
        line = Line(RIGHT*0.5,LEFT*0.5).next_to(p1,LEFT*0.2)
        line2 = Line(RIGHT*0.5, LEFT*0.5).next_to(p2,LEFT*0.2)
        line_right = Line(RIGHT*0.5,LEFT*0.5).move_to(body.get_right()).shift(RIGHT*0.5)
        dot_right = Dot(color=GREEN,radius=0.05).move_to(line_right.get_right())

        dot = Dot(color=RED,radius=0.05).move_to(line.get_left())
        dot2 = Dot(color=RED,radius=0.05).move_to(line2.get_left())
        body.add(line,dot,line2,dot2,line_right,dot_right)


        label = Text("OR", font_size=28).next_to(body, DOWN, buff=0.1)

        return VGroup(body, label)
    def AndGate():
        # Left vertical line
        left = Line(LEFT*1, LEFT*1 + UP*1).shift(DOWN*0.5).shift(RIGHT*0.5)

        # Top and bottom lines
        top = Line(left.get_top(), RIGHT*0.2 + UP*0.5)
        bottom = Line(left.get_bottom(), RIGHT*0.2 + DOWN*0.5)

        # Right semicircle
        arc = ArcBetweenPoints(top.get_right(),bottom.get_right(), angle=-PI)

        line = Line(RIGHT*0.5,LEFT*0.5).next_to(left.get_critical_point(UL)+DOWN*0.25,LEFT*0.2)
        line2 = Line(RIGHT*0.5, LEFT*0.5).next_to(left.get_critical_point(DL)+UP*0.25,LEFT*0.2)
        dot = Dot(color=RED,radius=0.05).move_to(line.get_left())
        dot2 = Dot(color=RED,radius=0.05).move_to(line2.get_left())
        
        body = VGroup(left, top, bottom, arc).set_stroke(width=4)
        line_right = Line(RIGHT*0.5,LEFT*0.5).move_to(body.get_right()).shift(RIGHT*0.5)
        dot_right = Dot(color=GREEN,radius=0.05).move_to(line_right.get_right())


        body.add(line,dot,line2,dot2,line_right,dot_right)
        label = Text("AND", font_size=28).next_to(body, DOWN, buff=0.1)
        return VGroup(body, label)

        #alu_dia.scale(0.5)
        #self.play(LaggedStartMap(Write,alu_dia, lag_ratio=0.2))
        #self.play(Create(alu_shape), Write(alu_label))
        #self.play(GrowArrow(in1), GrowArrow(in2))
        #self.play(Write(in1_label), Write(in2_label))
        #self.play(GrowArrow(out), Write(out_label))

        # Add a glow effect / highlight pulse
                #self.play(Create(highlight), run_time=0.4)
        #self.play(FadeOut(highlight), run_time=0.4)

        #self.wait()

    
class into(Scene):
    def von():
        system_box = Rectangle(width=5,height=8).set_color(ORANGE)

        cpuandalu_box = Rectangle(width=4.5,height=3.5)

        cpu = Rectangle(width=3.5, height=1).set_color(YELLOW)
        cpu_title = Text("Control Unit", font_size=30).move_to(cpu.get_center())

        alu = Rectangle(width=3.5, height=1).set_color(GRAY)
        alu_text = Text("ALU", font_size=30).move_to(alu.get_center())

        memory = Rectangle(width=3.5, height=1).set_color(BLUE)
        memory_title = Text("Memory", font_size=30).move_to(memory.get_center())

        input_dev = Rectangle(width=2.5,height=1.5).set_color(GREEN)
        input_title = Text("Input", font_size=28).move_to(input_dev.get_center())

        output_dev = Rectangle(width=2.5, height=1.5).set_color(RED)
        output_title = Text("Output", font_size=28).move_to(output_dev.get_center())
        system_box.shift(ORIGIN)
        cpuandalu_box.move_to(system_box.get_top()+DOWN*2) 
        
        cpu.move_to(cpuandalu_box.get_top()+DOWN)
        cpu_title.move_to(cpu.get_center())

        alu.move_to(cpu.get_bottom()+DOWN)
        alu_text.move_to(alu.get_center())

        memory.move_to(system_box.get_bottom()+UP)
        memory_title.move_to(memory.get_center())

        input_dev.to_edge(LEFT)
        input_title.move_to(input_dev.get_center())

        output_dev.to_edge(RIGHT)
        output_title.move_to(output_dev.get_center())

        # Display components
        
        #self.play(Create(input_dev), Write(input_title),Create(output_dev), Write(output_title))
        #self.play(Create(cpu), Write(cpu_title))
        #self.play(Create(alu), Write(alu_text))
        #self.play(Create(memory), Write(memory_title))
        #self.play(Create(cpuandalu_box))
        #self.play(Create(system_box))

        # Bus lines
        bus1 = Arrow(start=cpuandalu_box.get_bottom()+RIGHT*0.5, end=memory.get_top()+RIGHT*0.5).set_color(WHITE)
        bus1_return = Arrow(start=memory.get_top()+LEFT*0.5,end=cpuandalu_box.get_bottom()+LEFT*0.5).set_color(WHITE)
        bus2 = Arrow(end=system_box.get_left(), start=input_dev.get_right()).set_color(WHITE)
        bus3 = Arrow(start=system_box.get_right(), end=output_dev.get_left()).set_color(WHITE)

        #self.play(Create(bus1),Create(bus1_return), Create(bus2), Create(bus3))
        #self.wait(5)
        
    def Alu_module():
        left_top = LEFT*2 + UP*1.5
        right_top = RIGHT*2 + UP*1.5
        bottom = ORIGIN + DOWN
        thickness = 1 

        alu_shape = Polygon(
                    left_top,
                    left_top+RIGHT*thickness, 
                    bottom+ UP*thickness*1.2, 
                    right_top+LEFT*thickness,
                    right_top,
                    bottom+RIGHT*thickness/2,
                    bottom+LEFT*thickness/2,
                    color=BLUE, 
                    stroke_width=4
            )
        alu_label = Text("ALU", font_size=40).move_to(bottom+UP*thickness*0.6)

        in1 = Arrow(end= ((2*left_top)+(RIGHT*thickness))/2,start=((2*left_top)+(RIGHT*thickness))/2 + UP, buff=0.1)

        in2 = Arrow(end= ((2*right_top)+(LEFT*thickness))/2,start=((2*right_top)+(LEFT*thickness))/2 + UP, buff=0.1)
        in1_label = Text("A", font_size=32).next_to(in1, UP, buff=0.1)
        in2_label = Text("B", font_size=32).next_to(in2, UP, buff=0.1)
            # Output arrow
        out = Arrow(bottom + DOWN*0.1, DOWN*2, buff=0.1)
        out_label = Text("Result", font_size=28).next_to(out, DOWN)
        highlight = alu_shape.copy().set_color(YELLOW).set_stroke(width=6)

        alu_dia = VGroup(alu_shape,alu_label,in1,in2,in1_label,in2_label,out,out_label)
            # Animate everything
            #self.play(Create(alu_shape), Write(alu_label))
            #self.play(GrowArrow(in1), GrowArrow(in2))
            #self.play(Write(in1_label), Write(in2_label))
            #self.play(GrowArrow(out), Write(out_label))

            # Add a glow effect / highlight pulse
        return alu_dia
    def transistor():
        body = Circle(radius=0.6)
        angle = PI/4  # 45 degrees
        def point(circle,angle):
            return circle.get_center() + np.array([
                circle.radius*np.cos(angle),
                circle.radius*np.sin(angle),
                0
            ]) 
        # Collector line (top)
        collector = Line(point(body,angle), point(body,angle) + UP*1)
        # Emitter line (bottom)
        emitter = Line(point(body,angle+(3*(PI/2))),  point(body,angle+(3*(PI/2))) + DOWN*1)
        inner_line = Line(body.get_center()+LEFT*0.2+UP*0.4,body.get_center()+LEFT*0.2+DOWN*0.4, stroke_width=10)
        connect1 = Line(point(body,angle), inner_line.get_top()+DOWN*0.25)
        connect2 = Line(point(body,angle+(3*(PI/2))) , inner_line.get_bottom()+UP*0.25) 
        # Base line (left)
        base = Line(inner_line.get_center(), body.get_left() + LEFT*1)
        transistor = VGroup(body,connect1,connect2, collector, emitter, base, inner_line)
        return transistor
    def IC():
        R1 = Rectangle(width=1.5,height=1.5).set_color(GREEN)
        R1_text = Text('Atmega328p',font_size=15).move_to(R1.get_center())
        pin = Rectangle(width=0.1,height=0.05).set_color(RED)
        R1.shift(ORIGIN)
        #self.play(Create(R1), Write(R1_text))
        #for i in range(10):
        #    pin1 = Rectangle(width=0.1,height=0.05).set_color(RED)
        #    pin1.move_to(R1.get_left()+R1.get_top()+DOWN*0.15*(i+0.5)+LEFT*0.1)
        left_most_pins = [Rectangle(width=0.2,height=0.05).set_color(GOLD)
                          .move_to(R1.get_left()+R1.get_top()+DOWN*0.15*(i+0.5)+LEFT*0.1)
                          .set_fill(color=GOLD,opacity=1)
                          for i in range(10)]     
        right_most_pins = [Rectangle(width=0.2,height=0.05).set_color(GOLD)
                          .move_to(R1.get_right()+R1.get_top()+DOWN*0.15*(i+0.5)+RIGHT*0.1)
                          .set_fill(color=GOLD,opacity=1)
                          for i in range(10)] 
        up_most_pins = [Rectangle(width=0.05,height=0.2).set_color(GOLD)
                            .move_to(R1.get_left()+R1.get_top()+RIGHT*0.15*(i+0.5)+UP*0.1)
                        .set_fill(color=GOLD,opacity=1)
                        for i in range(10)]
        
        down_most_pins = [Rectangle(width=0.05,height=0.2).set_color(GOLD)
                            .move_to(R1.get_left()+R1.get_bottom()+RIGHT*0.15*(i+0.5)+DOWN*0.1)
                          .set_fill(color=GOLD,opacity=1)
                        for i in range(10)]
        chip = VGroup(R1,R1_text,*left_most_pins,*right_most_pins,*up_most_pins,*down_most_pins)
        
        #self.play(LaggedStartMap(Write,chip, lag_ratio=0))
        #self.wait(1)
        #self.play(chip.animate.shift(LEFT*5))
        #text_b = Text('{',font_size=80).move_to(R1.get_left()+RIGHT*2)
        #self.play(Write(text_b))
        #self.wait(2)
        return chip
    def classiscal_mech_vs_quantum_tunnling(self):
        pass

class test1(Scene):
    def construct(self):
        and_gate = logic_gate.AndGate()
        or_gate = logic_gate.OrGate()

        not_gate = logic_gate.NotGate()

        gates = VGroup(and_gate, or_gate, not_gate).arrange(RIGHT, buff=1.5).scale(0.8)

        self.play(DrawBorderThenFill(gates))
        for i in gates:
            self.play(Circumscribe(i), buff=0.1)
            
        self.wait()
        pass
class transistor(Scene):
    def construct(self):
        body = Circle(radius=0.6)
        angle = PI/4  # 45 degrees
        def point(circle,angle):
            return circle.get_center() + np.array([
                circle.radius*np.cos(angle),
                circle.radius*np.sin(angle),
                0
            ]) 
        # Collector line (top)
        collector = Line(point(body,angle), point(body,angle) + UP*1)

        # Emitter line (bottom)
        emitter = Line(point(body,angle+(3*(PI/2))),  point(body,angle+(3*(PI/2))) + DOWN*1)

        inner_line = Line(body.get_center()+LEFT*0.2+UP*0.4,body.get_center()+LEFT*0.2+DOWN*0.4, stroke_width=10)
        connect1 = Line(point(body,angle), inner_line.get_top()+DOWN*0.25)
        connect2 = Line(point(body,angle+(3*(PI/2))) , inner_line.get_bottom()+UP*0.25) 


        # Base line (left)
        base = Line(inner_line.get_center(), body.get_left() + LEFT*1)

        # Emitter arrow (pointing out for NPN)
                # Group everything
        transistor = VGroup(body, collector, emitter, base, inner_line)

        # Animate drawing
        self.play(Create(body))
        self.play(Create(collector), Create(emitter), Create(base), Create(inner_line),Create(connect1),Create(connect2))
        self.wait()



class VShapedALU(Scene):
    def construct(self):
        # Points for the V-shape ALU body
        left_top = LEFT*2 + UP*1.5
        right_top = RIGHT*2 + UP*1.5
        bottom = ORIGIN + DOWN
        thickness = 1 

        alu_shape = Polygon(
                left_top,
                left_top+RIGHT*thickness, 
                bottom+ UP*thickness*1.2, 
                right_top+LEFT*thickness,
                right_top,
                bottom+RIGHT*thickness/2,
                bottom+LEFT*thickness/2,
                color=BLUE, 
                stroke_width=4
        )
        alu_label = Text("ALU", font_size=40).move_to(bottom+UP*thickness*0.6)

        # Input arrows


        in1 = Arrow(end= ((2*left_top)+(RIGHT*thickness))/2,start=((2*left_top)+(RIGHT*thickness))/2 + UP, buff=0.1)

        in2 = Arrow(end= ((2*right_top)+(LEFT*thickness))/2,start=((2*right_top)+(LEFT*thickness))/2 + UP, buff=0.1)
        in1_label = Text("A", font_size=32).next_to(in1, UP, buff=0.1)
        in2_label = Text("B", font_size=32).next_to(in2, UP, buff=0.1)
        # Output arrow
        out = Arrow(bottom + DOWN*0.1, DOWN*2, buff=0.1)
        out_label = Text("Result", font_size=28).next_to(out, DOWN)
        alu_dia = VGroup(alu_shape,alu_label,in1,in2,in1_label,in2_label,out,out_label)
        # Animate everything
        alu_dia.scale(0.5)
        self.play(LaggedStartMap(Write,alu_dia, lag_ratio=0.2))
        #self.play(Create(alu_shape), Write(alu_label))
        #self.play(GrowArrow(in1), GrowArrow(in2))
        #self.play(Write(in1_label), Write(in2_label))
        #self.play(GrowArrow(out), Write(out_label))

        # Add a glow effect / highlight pulse
        highlight = alu_shape.copy().set_color(YELLOW).set_stroke(width=6)
        self.play(Create(highlight), run_time=0.4)
        self.play(FadeOut(highlight), run_time=0.4)

        self.wait()


