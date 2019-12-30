from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1.0',
    license='none',
    description='Calculator',

    author="t-zouchi",
    author_email='mojamoja.000@gmail.com',
    url="https://github.com/t-zouchi/circleci-pytest",

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'calculator = calculator',
        ]
    },
)
