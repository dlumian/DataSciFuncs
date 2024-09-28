# Data Science Functions

 **DataSciFuncs** is a Python package providing a collection of utility functions and tools for common import, input, and output operations used by data scientists and developers.

Current features are grouped into: 

1. Tools: read and write operations with formatting
1. Metrics generation: evaluation and visuals for classification models
1. Project resetting: remove options for files and dirs, reset operations on notebooks
1. Data visualization formatting: standardized formatting for matplotlib and plotly visuals
1. Build pipeline: help for uploading packages to Test PyPi and Pypi with clean test environments

## Installation

You can install the `DataSciFuncs` package via PyPI or directly from GitHub.

### Installing from PyPI

To install the latest stable release from PyPI, run:

```bash
pip install datascifuncs
```

### Installing from GitHub

To install the latest development version directly from GitHub, run:

```bash
pip install git+https://github.com/dlumian/DataSciFuncs.git
```

## Submodules

### 1. `tidbit_tools`
This submodule includes a variety of utility functions that support common data science tasks such as data loading, saving, and preprocessing utilities.

`check_directory_name` is a helpful function for controlling the current working directory of notebooks and scripts. This function accepts a `target_name` and walks up the directory to try and match given directory name. This function is of particular use when training and teaching to ensure current working directory is correct and, therefore, all imports will function as expected. 

#### Example Usage:
```python
from datascifuncs.tidbit_tools import load_json, write_json, check_directory_name

target_dir_name = 'main_repo_dir'
check_directory_name(target_dir_name)

data = load_csv('data.json')
save_json(data, 'data.json')
```

### 2. `metrics`
The `metrics` submodule provides functions to generate and save classification metrics and confusion matrices. Can be used with both training and test datasets and includes functionality for visualizing and comparing metrics when multiple evaluations exist.

#### Example Usage:
```python
from datascifuncs.metrics import generate_classification_metrics

generate_classification_metrics(
    output_dir='metrics_output',
    y_train=y_train,
    y_pred_train=y_pred_train,
    y_test=y_test,
    y_pred_test=y_pred_test
)
```

### 3. `reset_project`
The `reset_project` submodule includes functions designed to help reset your project to its original state, allowing for easy iteration, editing, and testing. This can include removing temporary files, resetting notebooks, and clearing directories.

#### Example Usage:
```python
from datascifuncs.reset_project import remove_files, remove_directories, reset_notebooks

# Remove all CSV files and any JSON files in the current directory
remove_files(['intermediate_data/*.csv', 'imgs/*.png'])

# Remove a specific directory
remove_directories(['temp_dir'])

# Reset all notebooks in the specified directory
reset_notebooks('notebooks')
```

### 4. `data_viz_formatting`
This submodule provides standardized formatting functions for visualizations created with matplotlib and plotly. These functions handle tasks like centering titles, setting font sizes, and ensuring consistent styling across plots.

#### Example Usage:
```python
from datascifuncs.data_viz_formatting import apply_default_matplotlib_styling
from datascifuncs.data_viz_formatting import apply_default_plotly_styling

fig, axs = apply_default_matplotlib_styling(fig, axs, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis')
plotly_fit = apply_default_plotly_styling(fig, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis', legend_title=None)
```

### 5. `build_pipeline`
Submodule for uploading packages to `Test PyPi` and `Pypi`. Full pipeline includes removing old build files and conda environment, using `twine` and `setup.py` files to upload package, and `anaconda` environment creation to test download. Main pipeline function can be called via command line. Arguments used are:
- path: path to directory with setup.py
- env-name: name for anaconda environment-NOTE: If env exists, it will be removed before new run is tested
- package-name: name for package as it appears in PyPi and Test PyPi
- repository: options are `testpypi` or `pypi`

***Process Steps:***
- Checks if version exists in given repository, exits and returns existing version numbers if so.
- Removes old build files
- Rebuilds package
- Uploads package to selected repository
- Removes conda env if it exists to ensure clean and complete install
- Creates new conda environment
- Installs package from repository

Additional testing of package once installed may be warranted.


```bash
build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name test_env --package-name datascifuncs --repository testpypi

build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name prod_env --package-name datascifuncs --repository pypi
```

## Running Tests

To run the tests, navigate to the root directory of the package and execute:

```bash
python -m unittest discover
```

This will run all the unit tests and provide feedback on the correctness of the various functions within the package.

NOTE: Unit tests not currently implemented for `data_viz_formatting` and `build_pipeline`. 

## Contributing

If you’d like to contribute to the development of `DataSciFuncs`, please fork the repository and create a pull request. I welcome contributions that improve existing features, fix bugs, or add new functionality.

### Guidelines:
- Write clear, concise code and include comments where necessary.
- Ensure that your code passes all existing tests and add new tests for any new functionality.
- Follow the PEP 8 style guide for Python code.

## Documentation

This README serves as the primary documentation for `DataSciFuncs`, providing an overview of the package, installation instructions, and usage examples. For any additional details or updates, refer to this document.

## License

`DataSciFuncs` is licensed under the MIT License. See the [LICENSE](https://github.com/dlumian/DataSciFuncs/blob/main/LICENSE) file for more details.

## Roadmap

- Additional unit tests for submodules
- Link to example usage in a data science project
- More robust documentation
