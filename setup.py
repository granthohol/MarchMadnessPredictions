from setuptools import setup, find_packages

setup(
    name='MarchMadnessPredictions',
    version='0.1.0',
    author='Grant Hohol',
    author_email='ghohol@wisc.edu',
    packages=find_packages(),
    install_requires=[
        'pandas~=1.3.3',
        'scikit-learn',
        'seaborn'
    ]
)