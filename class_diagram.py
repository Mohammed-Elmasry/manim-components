from ClassDiagramComponent import *


class ClassDiagram(ClassDiagramComponent):
    def construct(self):
        g = self.make_class()

        g.move_and_scale_down(LEFT, scale=0.7, runtime=2)

        self.wait(1)
