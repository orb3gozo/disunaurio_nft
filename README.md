<div align="center">

# disunaurio_nft

Python project for auto-generative art creation, inspired by hashlips. Project developed in python

[Contributing Guidelines](./CONTRIBUTING.md)

</div>

## Usage

You can install this package using [pip](https://pip.pypa.io/en/stable/):

```
$ pip install disunaurio_nft
```

You can now import this module on your Python project:

```python
import disunaurio_nft
```

## Development

To start developing this project, clone this repo and do:

```
$ make env-compile
$ make env-create
```

This will create a virtual environment with all the needed dependencies (using [tox](https://tox.readthedocs.io/en/latest/)). You can activate this environment with:

```bash
$ source ./.tox/disunaurio_nft/bin/activate
```

Then, you can run `make help` to learn more about the different tasks you can perform on this project using [make](https://www.gnu.org/software/make/).


## Why SVG files?

SVG files are very flexible if we compare it with other image formats like PNG or JPG.
Scalable Vector Graphics or SVG are XML-based files which represent a 2D graphic vector image this means
that we are able to use this vectors independently and apply any associated feature as color or apply any pattern
to that shape (vector).

## Quick Demo

After installing all the dependencies and setting up the environment, let's try a quick demo:

Load all your SVG files in the `./svg_files` directory, here you will find 2 folders:
 - `./svg_files/baseline` : It contains the reference image/svg files which the entire generation will be based. It can be composed of one or multiple SVG files.
 - `./svg_files/complements` : This folder contains all the complements which will be added to the baseline model. Inside this, there are more folder

If you haven't any own SVG files to try, don't worry! I provide some samples.


## Credits

* Documentation: https://disunaurio-nft.readthedocs.io.
* Free software: MIT license

This package was created with Cookiecutter_ and the `clarriu97/python-template` project template.

- Cookiecutter: https://github.com/clarriu97/python-template

## License

[Copyright](./LICENSE)
