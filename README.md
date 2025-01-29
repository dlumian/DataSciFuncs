# Data Science Functions

 **DataSciFuncs** is provides a collection of utility functions and tools for common data operations including import, output, and formatting.

### Current features: 

1. **Tools:** read and write operations with formatting
1. **Metrics:** evaluation and visuals for classification models
1. **Project Reset:** use file pattern match and directory lists to remove intermediate files and reset notebooks
1. **Visualization Formatting:** settings for consistent and professional matplotlib and plotly visuals
1. **Build Pipeline:** CLI tool for uploading packages to Test PyPi and Pypi with clean test environments

## Installation

Install `DataSciFuncs` via PyPI or GitHub.

### Installing from PyPI

```bash
pip install datascifuncs
```

### Installing from GitHub

```bash
pip install git+https://github.com/dlumian/DataSciFuncs.git
```

## Submodules

### 1. `tools`
Tools for project setup and json manipulations for consistent formatting and ease of use. 

`check_directory_name` verfies correct current working directory of notebooks and scripts. Accepts a `target_name` and walks up the directory tree to match `target_name`. Ensures consistent import paths for datas and utils, especially useful in the context of teaching or training.

`load_json` requires a json filepath, returning the loaded data.

`write_json` requires data and filepath. Data is written to json filepath with set formatting including encoding and indent.

`print_json` requires data and prints to output with set indent.

#### Example Usage:
```python
from datascifuncs.tools import check_directory_name, load_json, print_json, write_json

target_dir_name = 'main_repo_dir'
check_directory_name(target_name=target_dir_name)

data = load_csv(file_path='data.json')
print_json(data=data)
write_json(data=data, file_path='data_out.json')
```

### 2. `metrics`
Provides functions to generate, visualize, and save classification metrics. Can be used with both training and test datasets and includes functionality for visualizing and comparing metrics when multiple evaluations exist.

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
Functions to remove directories and files, allowing for faster iteration, editing, and testing.

#### Example Usage:
```python
from datascifuncs.reset_project import remove_files, remove_directories

# Remove all CSV files and any JSON files in the current directory
remove_files(['intermediate_data/*.csv', 'imgs/*.png'])

# Remove a specific directory
remove_directories(['temp_dir'])
```

### 4. `data_viz_formatting`
Standardized formatting functions for visualizations created with matplotlib and plotly. Handle tasks like centering titles, setting font sizes, and ensuring consistent styling across plots.

#### Example Usage:
```python
from datascifuncs.data_viz_formatting import apply_default_matplotlib_styling
from datascifuncs.data_viz_formatting import apply_default_plotly_styling

fig, axs = apply_default_matplotlib_styling(fig, axs, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis')
plotly_fit = apply_default_plotly_styling(fig, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis', legend_title=None)
```

### 5. `build_pipeline`
Submodule for uploading packages to `Test PyPi` and `Pypi`. Full pipeline includes removing old build files and conda environment, using `twine` and `setup.py` files to upload package, and `anaconda` environment creation to test download. Main pipeline function can be called via command line. Arguments used are:
- **path:** path to directory with setup.py
- **env-name:** name for anaconda environment-NOTE: If env exists, it will be removed before new run is tested
- **package-name:** name for package as it appears in PyPi and Test PyPi
- **repository:** options are `testpypi` or `pypi`

***Process Steps:***
- **Version Check** 
    - If version exists in given repository, exits and returns existing version numbers.
- **Removes old build files**
- **Rebuilds package**
- **Uploads package to selected repository**
- **Removes conda env if it exists to ensure clean and complete install**
- **Creates new conda environment**
- **Installs package from repository**

Additional testing of package once installed may be warranted.


```bash
build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name test_env --package-name datascifuncs --repository testpypi

build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name prod_env --package-name datascifuncs --repository pypi
```

## CLI Steps
CLI steps for package build steps for clarity and debugging. Example steps direct to main PyPi, must edit for TestPypi.

Run in project directory.

***NOTE:*** rm -rf will force remove directories and files. Use with care. 

```bash
rm -rf dist/ build/ *.egg-info
python -m build 
twine upload dist/*
conda env remove --name prod_env
conda create -n prod_env python=3.11 -y
conda run --name prod_env pip install datascifuncs
```

## Running Tests

- Navigate to the root directory of the package (datascifuncs)
- Run following command:

```bash
python -m unittest discover
```

This will run unit tests and provide results of tests.

**NOTE:** Unit tests not currently implemented for `data_viz_formatting` and `build_pipeline`. 

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