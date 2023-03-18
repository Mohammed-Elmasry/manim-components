from manim import *


class CreateCircle(Scene):
    def construct(self):
        label = Text("Sum = ")
        content = Text("0")
        sum_group = VGroup(label, content).arrange(buff=0.5)
        sum_group.to_edge(UR)

        arr = array(10)
        self.play(GrowFromEdge(arr, UP), run_time=0.2)

        number = 1
        for slot in arr:
            self.play(Write(Text(f"{number}").move_to(slot.get_center()), run_time=0.1))
            number += 1

        self.play(Create(sum_group))

        arrow = Arrow(arr[0].get_center() + DOWN * 2, arr[0].get_center())
        self.play(GrowArrow(arrow))

        for slot in arr:
            self.play(arrow.animate.shift(RIGHT))

        self.play(
            Transform(sum_group[1], Text(f"{1}").move_to(sum_group[1].get_center()))
        )


def array(length=1):
    return VGroup(*[Square(side_length=1) for _ in range(length)]).arrange(buff=0)
