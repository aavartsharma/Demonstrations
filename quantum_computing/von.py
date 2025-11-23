from manim import *

class VonNeumann(Scene):
    def construct(self):

        # Boxes for components
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

        # Positioning

    
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
        
        self.play(Create(input_dev), Write(input_title),Create(output_dev), Write(output_title))
        self.play(Create(cpu), Write(cpu_title))
        self.play(Create(alu), Write(alu_text))
        self.play(Create(memory), Write(memory_title))
        self.play(Create(cpuandalu_box))
        self.play(Create(system_box))

        # Bus lines
        bus1 = Arrow(start=cpuandalu_box.get_bottom()+RIGHT*0.5, end=memory.get_top()+RIGHT*0.5).set_color(WHITE)
        bus1_return = Arrow(start=memory.get_top()+LEFT*0.5,end=cpuandalu_box.get_bottom()+LEFT*0.5).set_color(WHITE)
        bus2 = Arrow(end=system_box.get_left(), start=input_dev.get_right()).set_color(WHITE)
        bus3 = Arrow(start=system_box.get_right(), end=output_dev.get_left()).set_color(WHITE)

        self.play(Create(bus1),Create(bus1_return), Create(bus2), Create(bus3))
        self.wait(5)

