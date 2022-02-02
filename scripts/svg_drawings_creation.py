from email.policy import default
import sys
import argparse
from os import path

from disunaurio_nft.disunaur_generator import (load_yaml_conf_file,
                                               generate_baseline_drawing,
                                               generate_complements, 
                                               generate_drawing,
                                               sort_by_priority)


def main(args = None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    baseline_data = load_yaml_conf_file(args.datapath)['baseline']
    complements_data = load_yaml_conf_file(args.datapath)['complements']

    for i in range(args.num):
        output_svg_file = path.join(args.output_path, f'disunaurio#{i}.svg')

        element_list = []
        element_list = generate_baseline_drawing(element_list, baseline_data)
        element_list = generate_complements(element_list, complements_data)

        element_list = sort_by_priority(element_list)
        
        dwg = generate_drawing(element_list, output_svg_file)
        dwg.save(output_svg_file, True)

def parse_args(args):
    description = '''
    Create auto-generative svg files from yml datapath.
    '''
    epilog = '''
            python3 ./scripts/svg_drawings_creation.py ./svg_files/tests/ --num 20
    '''
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=epilog
    )
    parser.add_argument('output_path', help='')
    parser.add_argument('--datapath', default=path.join(path.realpath('.'), 'svg_files/data/data.yml'), 
                        help='Data yaml file location')
    parser.add_argument('-n', '--num', type=int, default=10, help='Number of svg files created')
    return parser.parse_args(args)

if __name__ == '__main__':
    main()
