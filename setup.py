from setuptools import setup, find_packages

setup(
    name='datascifuncs',
    version='0.1.0',
    author='Danny Lumian',
    author_email='dlumian@gmail.com',
    description='A package for loading/saving data and verifying paths.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dlumian/DataSciFuncs',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit-learn',
        'nbconvert',
        'nbformat',
    ],
    entry_points={
        'console_scripts': [
            'build-pipeline=datascifuncs.build_pipeline:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
