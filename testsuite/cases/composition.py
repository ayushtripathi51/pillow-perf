# coding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

from PIL import Image

from .base import rpartial, root
from .pillow import PillowTestCase


class CompositionCase(PillowTestCase):
    def create_test_data(self, size, mode):
        im = Image.open(root('resources', 'color_circle.png'))
        im = self.resize(im, size, Image.BICUBIC)
        return [im, im.copy()]

    def runner(self, first, second):
        return Image.alpha_composite(first, second)

    def readable_args(self):
        return ["Composition"]


cases = [
    rpartial(CompositionCase),
]
