from manim import *


class ClassDiagramComponent(Scene):
    c = None
    class_name_text = ""

    def make_class(self, class_name_text="myClass"):
        self.class_name_text = class_name_text

        class_name = Rectangle(height=1)
        class_attributes = Rectangle(height=2)
        class_methods = Rectangle(height=2)
        g = VGroup()
        g.add(class_name, class_attributes, class_methods)
        t = Text(self.class_name_text).move_to(g[0].get_center() + UP * 3)
        attr1 = Text("- Name").move_to(g[1].get_center() + UP + LEFT)

        class_attributes.next_to(class_name, direction=DOWN, buff=0)
        class_methods.next_to(class_attributes, direction=DOWN, buff=0)

        g.move_to(UP)
        self.play(GrowFromEdge(g, UP))
        self.display_class_text(t)
        self.play(Write(attr1))
        g.add(t, attr1)

        self.c = g

        return self

    def move_class_to_edge(self, direction=LEFT, runtime=1):
        self.play(self.c.animate.to_edge(direction), run_time=runtime)

    def move_and_scale_down(self, direction=LEFT, scale=0.5, runtime=1):
        self.play(self.c.animate.to_edge(direction).scale(scale), run_time=runtime)

    def display_class_text(self, t):
        self.play(Write(t))
