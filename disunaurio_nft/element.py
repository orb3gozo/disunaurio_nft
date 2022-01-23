import random

class Element:

    def __init__(self, id: str, contours:list, continents:list, priority:int):
        self.id = id
        self.contours = contours
        self.continents = continents

        self.contour_colors = self.generate_contour_colors()
        self.continents_colors = self.generate_continents_colors()
        self.priority = priority

    def generate_contour_colors(self, color_pallete=None):
        contour_colors = []
        if not color_pallete:
            rand_color = random.choices(range(256), k=3)
            for _ in self.contours:
                contour_colors.append(rand_color)
        self.contour_colors = contour_colors
        return contour_colors

    def generate_continents_colors(self, color_pallete=None):
        continent_colors = []
        if not color_pallete:
            for _ in self.continents:
                rand_color = random.choices(range(256), k=3)
                continent_colors.append(rand_color)
        self.continent_colors = continent_colors
        return continent_colors
