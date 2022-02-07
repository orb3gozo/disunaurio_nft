from os import path
import svgwrite
from svgwrite import Drawing, rgb
import random
import yaml
from .element import Element


def sort_by_priority(element_list: list) -> list:
    """
    Sort list of elements by their priority

    Args:
        element_list (list): List of element objects

    Returns:
        list: List of element objects sorted by priority
    """
    return sorted(element_list, key=lambda e: e.priority)


def generate_drawing(element_list: list, filepath: str) -> Drawing:
    """
    Generate a svgwrite Drawing object using a list of element objects
    and save to a svg file.

    Args:
        element_list (list): List of element objects
        filepath (str): Filepaht to save the generated drawing

    Returns:
        Drawing: svgwrite Drawing object
    """
    drawing = create_canvas(filepath)
    for element in element_list:
        drawing = draw_svg_element(drawing, element)
    drawing.save(pretty=True)
    return drawing

def draw_svg_element(drawing: Drawing, element: Element)->Drawing:
    """
    Add svgwrite Path objects created with an element object to a svgwrite
    Drawing object.

    Args:
        drawing (Drawing): svgwrite Drawing object
        element (Element): element object

    Returns:
        Drawing: svgwrite Drawing object
    """
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
    """
    Create a baseline svgwrite Drawing object with x by y dimensions and a background.

    Args:
        filepath (str): file path to allocate the drawing/final svg file

    Returns:
        Drawing: svgwrite Drawing object
    """
    drawing = Drawing(filepath, size=('2048', '2048'), profile='full')
    color = random.choices(range(256), k=3)
    background = svgwrite.shapes.Rect(insert=(0, 0), size=(2048, 2048), fill=rgb(color[0], color[1], color[2]), id='background')
    drawing.add(background)
    return drawing

def generate_baseline_drawing(element_list: list, baseline_data: dict) -> list:
    """
    Create an element list of the basline drawing with the baseline extracted data (dictionary)
    and add it to an element list.

    Args:
        element_list (list): List of element objects
        baseline_data (dict): Baseline key form dictionary extracted from .yml file

    Returns:
        list: List of element objects with new objects added
    """    
    element_list.extend(create_element_list(baseline_data))
    return element_list

def generate_complements(element_list: list, complements_data: dict) -> list:
    """
    Create an element list of complements with the complements extracted data (dictionary)
    and add it to an element list.

    Args:
        element_list (list): List of element objects
        complements_data (dict): Complements key from dictionary extracted from .yml file

    Returns:
        list: List of element objects with new objects added
    """    
    for comp_name, complement in  complements_data.items():
        if random.choice([True, False]) or comp_name == 'eyewear':
            comp_list = create_element_list(complement)
            comp = random.choice(comp_list)
            element_list.append(comp)
    return element_list

def create_element_list(data: dict) -> list:
    """
    Extract properties from a data dictionary, create one element with this extracted data
    per each dictionary_key/svg_file.

    Args:
        data (dict): Dictionary with raw data from a svg file

    Returns:
        list: List of elements, new elements added
    """
    elements_list = []
    for id, d in data.items():
        contours, colors, priority = extract_properties(d)
        elements_list.append(Element(id, contours, colors, priority))
    return elements_list

def extract_properties(data:dict) -> tuple:
    """
    Extract properties from dictionary to generate a list of contours, a list
    of continents and an int for priority score.

    Args:
        data (dict): Dictionary with svg extracted data

    Returns:
        tuple: Tuple of (contour:list, continents:list, priority:int)
    """    
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
