import argparse
import sys
from os import path

from disunaurio_nft.data_extractor import save_yaml, generate_structured_data


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    args = parse_args(args)

    baseline_path = path.join(args.rootpath, 'baseline')
    complements_path = path.join(args.rootpath, 'complements')
    data_outpath = path.join(args.rootpath,'data/data.yml')

    svgs = generate_structured_data(baseline_path)
    svgs['complements'] = generate_structured_data(complements_path)

    save_yaml(svgs, data_outpath)
    print(f'Extracted data file saved in: {data_outpath}')

def parse_args(args):
    description = '''
    Extract svg vector data from svg files stored in baseline and complements folders and create data.yml file in data folder.
    '''
    epilog = '''
            python3 ./disunaurio_nft/data_extractor.py
    '''
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=epilog
    )
    parser.add_argument('--rootpath', default=path.join(path.realpath('.'),'svg_files'), help='')
    return parser.parse_args(args)

if __name__ == '__main__':
    main()
