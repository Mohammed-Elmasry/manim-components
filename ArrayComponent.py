from manim import *


class ArrayComponent(Scene):
    array_content = []
    skeleton = None
    pointer = None
    pointer_index = 0

    def __getitem__(self, item):
        return self.skeleton[item]

    def create_array(self, array_content):
        self.array_content = array_content
        arr = self.display_array(array_content)
        self.fill_array(arr, array_content)
        return self

    def display_array(self, array_content):
        arr = VGroup(*[Square(side_length=1) for _ in range(len(array_content))]).arrange(buff=0)
        self.skeleton = arr
        self.play(GrowFromEdge(arr, UP), run_time=0.2)
        return arr

    def fill_array(self, arr, arr_content):
        index = 0
        for slot in arr:
            self.play(Write(Text(f"{arr_content[index]}").move_to(slot.get_center()), run_time=0.1))
            index += 1

    def display_pointer(self):
        self.pointer = Arrow(self[0].get_center() + DOWN * 2, self[0].get_center())
        self.pointer_index = 0
        self.play(GrowArrow(self.pointer))

    def move_pointer_right(self):
        self.play(self.pointer.animate.shift(RIGHT))
        self.pointer_index += 1

    def move_pointer_left(self):
        self.play(self.pointer.animate.shift(LEFT))
        self.pointer_index -= 1

    def move_pointer_to_index(self, index):
        self.play(self.pointer.animate.move_to(self[index].get_center() + DOWN))
        self.pointer_index = index

    def get_value_at_index(self, index):
        return self.array_content[index]

    def get_value_at_pointer(self):
        return self.array_content[self.pointer_index]
