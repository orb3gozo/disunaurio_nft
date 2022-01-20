from os import path, walk
import typer
import yaml
from collections import defaultdict
from xml.dom import minidom
from yaml.representer import Representer
yaml.add_representer(defaultdict, Representer.represent_dict)

app = typer.Typer()

@app.command()
def main(rootpath: str=path.join(path.realpath('.'),'svg_files')):
    baseline_path = path.join(rootpath, 'baseline')
    complements_path = path.join(rootpath, 'complements')

    print(baseline_path)

    basl_outpath = path.join(rootpath,'data/data_baseline.yml')
    comp_outpath = path.join(rootpath,'data/data_complements.yml')

    baseline_svgs = generate_structured_data(baseline_path)
    complements_svgs = generate_structured_data(complements_path)

    save_yaml(baseline_svgs, basl_outpath)
    save_yaml(complements_svgs, comp_outpath)
    typer.echo(f'Data extracted into: \n\t- {basl_outpath}\n\t- {comp_outpath}')

    
def generate_structured_data(rootpath: str) -> defaultdict(list):
    svgs = defaultdict(list)
    for root, _, files in walk(rootpath):
        if files:
            key = path.basename(root)
            svgs[key] = {f.split('.')[0]: extract_elements(path.join(root, f)) for f in files}
    return svgs

def extract_elements(filepath: str) -> dict:
    doc = minidom.parse(filepath)
    path_id = [path.getAttribute('id') for path
                    in doc.getElementsByTagName('path')]
    path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
    elements = {id:strings for id, strings in zip(path_id, path_strings)}
    return elements

def save_yaml(svgs: defaultdict, output_path: str) -> None:
    with open(output_path, 'w') as of:
        yaml.dump(svgs, of, default_flow_style=False)

if __name__ == '__main__':
    app()