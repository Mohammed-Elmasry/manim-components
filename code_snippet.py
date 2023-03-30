from manim import *


class CodeSnippetExample(Scene):
    def construct(self):
        lines_of_code = 0.25 + 2
        function_signature = Tex(r"public ", r"static ", r"void ", r"setName() \{")
        # function_signature = Tex(r"while ", r"(x ", "> ", r"1) \{")
        function_signature.move_to(UP)

        function_body_line1 = Tex("this.name = name;")
        function_body_line2 = Tex("this.sample = sample;")

        function_close = Tex(r"\}")

        function_body_line1.next_to(function_signature, DOWN)
        function_body_line2.next_to(function_body_line1, DOWN, aligned_edge=LEFT)
        function_close.move_to(function_signature.get_left() + DOWN * lines_of_code)

        self.play(Write(function_signature))
        self.play(Write(function_body_line1))
        self.play(Write(function_body_line2))
        self.play(Write(function_close))

        self.wait(1)

        code_snippet = VGroup(function_signature, function_body_line1, function_body_line2,
                              function_close)

        self.play(code_snippet.animate().scale(0.7).to_edge(UL), run_time=2)

        self.wait(1)

        function_body_line3 = Tex("var result = Math.min(2, 3);").scale(0.7)
        function_body_line3.next_to(function_body_line2, DOWN, aligned_edge=LEFT)
        self.play(code_snippet[3].animate().shift(DOWN), run_time=1)
        self.play(Write(function_body_line3))
        code_snippet.add(function_body_line3)

        self.wait(1)

        self.play(code_snippet.animate().to_edge(UR))

        self.wait(1)
