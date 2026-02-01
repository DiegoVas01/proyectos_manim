from manim import *

class animacion_1(Scene):
    def construct(self):
        self.camera.background_color = "#010C11"

        identidad = MathTex(r"(x+y)^n", color=WHITE)
        expansion = MathTex(r"=\sum_{k=0}^{n}{\binom{n}{k}x^{n-k}y^k}", color=WHITE)

        VGroup(identidad, expansion).arrange(RIGHT, buff=0.5)

        self.play(Write(identidad))
        self.wait(0.5)
        self.play(Write(expansion))
        self.wait(2)
