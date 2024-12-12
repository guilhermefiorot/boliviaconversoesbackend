from setuptools import setup, find_packages

setup(
    name='boliviaconversoesbackend',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'dev': ['pytest', 'flake8', 'black', 'mypy']
    },
    author='guilhermefiorot',
    author_email='guilhermefirme3@gmail.com',
    description='Um conversor de números inteiros para algarismos romanos',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/guilhermefiorot/boliviaconversoesbackend',
    classifiers=[
        'Programming Language :: Python :: 3.12',
    ],
)