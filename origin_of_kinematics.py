#######################################################
# special thanks : 3b1b/manim
# Author : Sanjeev
#######################################################

from big_ol_pile_of_manim_imports import *
import numpy as np
from scipy.integrate import odeint
class Intro_scene(Scene):
    def construct(self):
        background_square=Square(side_length=20,fill_color=WHITE, fill_opacity=1)
        self.add(background_square)

        example_text = TextMobject(
            "ORIGINS of KINEMATICS",color=BLUE,background_stroke_color=BLUE
        )
        example_tex = TextMobject(
            "Physics",color=RED,background_stroke_color=RED
        )
        group = VGroup(example_text,example_tex)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        group.move_to(2*UP)

        self.play(FadeIn(example_text))
        self.wait(1)
        self.play(FadeIn(example_tex))
        self.wait(2)
