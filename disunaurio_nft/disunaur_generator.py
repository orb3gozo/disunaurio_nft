from os import path
import svgwrite
from svgwrite import Drawing, rgb
import random
import yaml
from element import Element


def generate_drawing(element_list: list, filepath: str) -> Drawing:
    drawing = create_canvas(filepath)
    for element in element_list:
        drawing = draw_svg_element(drawing, element)
    drawing.save(pretty=True)
    return drawing

def draw_svg_element(drawing: Drawing, element: Element)->Drawing:
    for continent, color in zip(element.continents, element.continents_colors):
        path = svgwrite.path.Path(id=element.id, fill=rgb(color[0], color[1], color[2]),
                                d=continent, debug=False)
        drawing.add(path)

    for contour, color in zip(element.contours, element.contour_colors):
        path = svgwrite.path.Path(id=element.id, fill=rgb(color[0], color[1], color[2]),
                                  d=contour, debug=False)
        drawing.add(path)
    return drawing

def create_canvas(filepath: str) -> Drawing:
    drawing = Drawing(filepath, size=('2048', '2048'), profile='full')
    color = random.choices(range(256), k=3)
    background = svgwrite.shapes.Rect(insert=(0, 0), size=(2048, 2048), fill=rgb(color[0], color[1], color[2]), id='background')
    drawing.add(background)
    return drawing

def create_element_list(datafile: dict):
    elements_list = []
    for id, d in datafile.items():
        contours, colors, priority = extract_properties(d)
        elements_list.append(Element(id, contours, colors, priority))
    return elements_list

def extract_properties(data:dict) -> tuple:
    contours, continents = [], []
    for key, d in data.items():
        if 'contour' in key: contours.append(d)
        if 'color' in key: continents.append(d)
    priority = data['priority']
    return contours, continents, priority

def load_yaml_conf_file(filepath:str)->dict:
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    return data

def generate_baseline_drawing(element_list: list, baseline_data: dict) -> list:
    element_list.extend(create_element_list(baseline_data))
    return element_list

def generate_complements(element_list: list, complements_data: dict) -> list:
    for comp_name, complement in  complements_data.items():
        if random.choice([True, False]) or comp_name == 'eyewear':
            comp_list = create_element_list(complement)
            comp = random.choice(comp_list)
            element_list.append(comp)
    return element_list

# ----------------------------------------------------------------------------------------- 
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

datapath = path.join(path.realpath('.'), 'svg_files/data/data.yml')

baseline_data = load_yaml_conf_file(datapath)['baseline']
complements_data = load_yaml_conf_file(datapath)['complements']

for i in range(10):
    output_svg_file = path.join(path.realpath('.'), f'svg_files/tests/test_{i}.svg')
    
    element_list = []
    element_list = generate_baseline_drawing(element_list, baseline_data)
    element_list = generate_complements(element_list, complements_data)
    dwg = generate_drawing(element_list, output_svg_file)
    dwg.save(output_svg_file, True)
