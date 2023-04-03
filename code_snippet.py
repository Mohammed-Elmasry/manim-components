from manim import *
from manim.mobject.text import tex_mobject


class CodeSnippetExample(Scene):
    def construct(self):
        # lines_of_code = 0.25 + 2
        # function_signature = Tex(r"public ", r"static ", r"void ", r"setName() \{")
        #
        # function_body_line1 = Tex("this.name = name;")
        # function_body_line2 = Tex("this.sample = sample;")
        #
        # function_close = Tex(r"\}")
        #
        # function_body_line1.next_to(function_signature, DOWN)
        # function_body_line2.next_to(function_body_line1, DOWN, aligned_edge=LEFT)
        # function_close.move_to(function_signature.get_left() + DOWN * lines_of_code)  # TODO investigate line of code

        # self.wait(1)
        #
        # function_snippet = VGroup(function_signature, function_body_line1, function_body_line2,
        #                           function_close)
        #
        # self.play(Write(function_snippet))
        # self.wait()
        #
        # self.play(function_snippet.animate().scale(0.7).to_edge(UL), run_time=2)
        #
        # self.wait(1)
        # added_lines = 2
        #
        # function_body_line3 = Tex("var minimum = Math.min(2, 3);").scale(0.7)
        # function_body_line4 = Tex("var maximum = Math.max(2, 3);").scale(0.7)
        # function_body_line3.next_to(function_body_line2, DOWN, aligned_edge=LEFT)
        # function_body_line4.next_to(function_body_line3, DOWN, aligned_edge=LEFT)
        #
        # self.wait()
        # function_snippet.add(function_body_line3, function_body_line4)
        #
        # self.play(function_snippet[3].animate().shift(DOWN * 0.5 * added_lines), Write(function_body_line3),
        #           Write(function_body_line4))
        #
        # self.wait()
        #
        # while_sig = Tex(r"while (x == 1) ", r"\{")
        # while_close = Tex(r"\}")
        #
        # self.play(function_close.animate().shift(DOWN * 0.5 * 4))
        #
        # while_sig.next_to(function_close, UR, aligned_edge=LEFT).scale(0.7)
        # while_close.next_to(while_sig, DOWN, aligned_edge=LEFT).scale(0.7)
        #
        # function_snippet.add(while_sig, while_close)
        #
        # self.play(Write(while_sig), Write(while_close))
        #
        # self.wait()

        plane = NumberPlane()
        self.add(plane)
