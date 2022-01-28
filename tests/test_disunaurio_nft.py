#!/usr/bin/env python

"""Tests for `disunaurio_nft` package."""

import pytest

from click.testing import CliRunner

from disunaurio_nft import cli
from os import path


def test_data_extractor():
    from disunaurio_nft import data_extractor

    data_extractor.main()

    assert path.isfile("svg_files/data/data.yml")


def test_disunaur_generator():
    from disunaurio_nft.disunaur_generator import load_yaml_conf_file
    from disunaurio_nft.disunaur_generator import generate_baseline_drawing
    from disunaurio_nft.disunaur_generator import generate_complements
    from disunaurio_nft.disunaur_generator import generate_drawing

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

        assert path.isfile(output_svg_file)


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'disunaurio_nft.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
