import click
from os import path

from disunaurio_nft.data_extractor import save_yaml, generate_structured_data

@click.command()
@click.option('--rootpath', default=path.join(path.realpath('.'),'svg_files'), help='')
def main(rootpath):

    baseline_path = path.join(rootpath, 'baseline')
    complements_path = path.join(rootpath, 'complements')
    data_outpath = path.join(rootpath, 'data', 'data.yml')

    svgs = generate_structured_data(baseline_path)
    svgs['complements'] = generate_structured_data(complements_path)

    save_yaml(svgs, data_outpath)
    print(f'Extracted data file saved in: {data_outpath}')


if __name__ == '__main__':
    main()
