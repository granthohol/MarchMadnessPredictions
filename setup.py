from setuptools import setup, find_packages

setup(
    name='MarchMadnessPredictions',
    version='0.1.0',
    author='Grant Hohol',
    author_email='ghohol@wisc.edu',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'seaborn',
        'numpy',
        'matplotlib',
        'requests',
        'BeautifulSoup'
    ]
)