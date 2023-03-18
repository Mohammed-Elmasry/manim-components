from manim import *
from ArrayComponent import ArrayComponent


class CreateCircle(ArrayComponent):

    def construct(self):
        label = Text("Sum = ")
        content = Text("0")
        sum_group = VGroup(label, content).arrange(buff=0.5)
        sum_group.to_edge(UR)

        arr = self.create_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        self.play(Create(sum_group))

        arr.display_pointer()

        current_sum = 0
        for slot in arr:
            current_sum += arr.get_value_at_pointer()
            self.play(
                Transform(sum_group[1], Text(f"{current_sum}").move_to(sum_group[1].get_center()))
            )
            arr.move_pointer_right()
