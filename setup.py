#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Iñigo Orbegozo",
    author_email='orb3gozo@protonmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python project for auto-generative art creation, inspired by hashlips.",
    entry_points={
        'console_scripts': [
            'disunaurio_nft=disunaurio_nft.cli:main',
        ],
    },
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='disunaurio_nft',
    name='disunaurio_nft',
    packages=find_packages(include=['disunaurio_nft', 'disunaurio_nft.*']),
    test_suite='tests',
    url='https://github.com/0rb3/disunaurio_nft',
    version='0.1.0',
    zip_safe=False,
)
