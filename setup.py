from setuptools import setup, find_packages

setup(
    name='datascifuncs',
    version='0.3.2',
    author='Danny Lumian',
    author_email='dlumian@gmail.com',
    description='A package for loading/saving data and verifying paths.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dlumian/DataSciFuncs',
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'seaborn>=0.10.0',
        'matplotlib>=3.0.0',
        'scikit-learn>=1.0.0',
        'nbconvert>=7.0.0',
        'nbformat>=5.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>3.11'
)
