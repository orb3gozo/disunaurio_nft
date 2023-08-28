from email.policy import default
import sys
import click
from os import path

from disunaurio_nft.disunaur_generator import (load_yaml_conf_file,
                                               generate_baseline_drawing,
                                               generate_complements,
                                               generate_drawing,
                                               sort_by_priority)

@click.command()
@click.option('--datapath', default=path.join(path.realpath('.'), 'svg_files/data/data.yml'), help='Data yaml file location')
@click.option('--output_path', default=path.join(path.realpath('.'), 'svg_files/output_files/'), help='')
@click.option('-n', '--num', type=int, default=10, help='Number of svg files created')
def main(datapath, output_path, num):

    baseline_data = load_yaml_conf_file(datapath)['baseline']
    complements_data = load_yaml_conf_file(datapath)['complements']

    for i in range(num):
        output_svg_file = path.join(output_path, f'disunaurio#{i}.svg')

        element_list = []
        element_list = generate_baseline_drawing(element_list, baseline_data)
        element_list = generate_complements(element_list, complements_data)

        element_list = sort_by_priority(element_list)

        dwg = generate_drawing(element_list, output_svg_file)
        dwg.save(output_svg_file, True)


if __name__ == '__main__':
    main()
