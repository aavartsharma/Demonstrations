from manim import *
from models import into
from models import logic_gate
class com(Scene):
    def construct(self):
        chip = into.IC()
        chip_label = Text("Integrated Circit").next_to(chip,DOWN)
        chip = VGroup(chip,chip_label)
        alu = into.Alu_module().scale(0.8) 
        logic_gates = VGroup(logic_gate.OrGate(), logic_gate.AndGate()).arrange(DOWN,buff=0.2)
        l_label = Text("logic Gate").next_to(chip,DOWN)
        logic_gates = VGroup(logic_gates,l_label)
        trans = into.transistor() 
        trans_label = Text("Transistor").next_to(chip,DOWN)
        trans = VGroup(trans,trans_label)
        g = VGroup(chip,Brace(chip,RIGHT).flip(),alu,Brace(alu,RIGHT).flip(),logic_gates,Brace(logic_gates,RIGHT).flip(),trans)
        g.arrange(RIGHT,buff=0.5)
        g.scale(0.75)
        for i in g:
            self.play(FadeIn(i))
            self.wait(1.25)
