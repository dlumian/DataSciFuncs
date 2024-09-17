from setuptools import setup, find_packages

setup(
    name='tidbits',
    version='0.1.0',
    author='Danny Lumian',
    author_email='dlumian@gmail.com',
    description='A package for loading/saving data and verifying paths.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dlumian/tidbits',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'sklearn',
        'nbconvert',
        'npformat'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
