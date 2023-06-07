#
# exepiest setuptools script
#
# This file is part of exepiest
# (https://github.com/se-tutorial/exepiest.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the exepiest module.
    The easiest way would be to just ``import exepiest ``, but note that this may  # noqa
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('exepiest'))
    from version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


setup(
    # Module name (lowercase)
    name='exepiest',

    # Version
    version=get_version(),

    description='This is a one-week project in which we are using branching processes to estimate the time-dependent reproduction number of a disease.',  # noqa

    long_description=get_readme(),

    license='MIT "New" or "Revised" License',

    # author='',

    # author_email='',

    maintainer='',

    maintainer_email='',

    url='https://github.com/se-tutorial/exepiest.git',

    # Packages to include
    packages=find_packages(include=('exepiest', 'exepiest.*')),
    include_package_data=True,

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy>=1.8',
        'scipy>=1.6',

    ],
    python_requires='>3.8',
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'karma-sphinx-theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)
