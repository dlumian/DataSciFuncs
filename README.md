# Tidbits

 **Tidbits** is a Python package providing a collection of utility functions and tools for common import, input, and output operations used by data scientists and developers.

Current features are grouped into: 

1. Tools: read and write operations with formatting
1. Metrics generation: evaluation and visuals for classification models
1. Project resetting: remove options for files and dirs, reset operations on notebooks
1. Data visualization formatting: standardized formatting for matplotlib and plotly visuals

## Installation

You can install the `tidbits` package via PyPI or directly from GitHub.

### Installing from PyPI

To install the latest stable release from PyPI, run:

```bash
pip install tidbits
```

### Installing from GitHub

To install the latest development version directly from GitHub, run:

```bash
pip install git+https://github.com/dlumian/tidbits.git
```

## Submodules

### 1. `tidbit_tools`
This submodule includes a variety of utility functions that support common data science tasks such as data loading, saving, and preprocessing utilities.

`check_directory_name` is a helpful function for controlling the current working directory of notebooks and scripts. This function accepts a `target_name` and walks up the directory to try and match given directory name. This function is of particular use when training and teaching to ensure current working directory is correct and, therefore, all imports will function as expected. 

#### Example Usage:
```python
from tidbits.tidbit_tools import load_json, write_json, check_directory_name

target_dir_name = 'main_repo_dir'
check_directory_name(target_dir_name)

data = load_csv('data.json')
save_json(data, 'data.json')
```

### 2. `metrics`
The `metrics` submodule provides functions to generate and save classification metrics and confusion matrices. Can be used with both training and test datasets and includes functionality for visualizing and comparing metrics when multiple evaluations exist.

#### Example Usage:
```python
from tidbits.metrics import generate_classification_metrics

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
from tidbits.reset_project import remove_files, remove_directories, reset_notebooks

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
from tidbits.data_viz_formatting import apply_default_matplotlib_styling
from tidbits.data_viz_formatting import apply_default_plotly_styling

fig, axs = apply_default_matplotlib_styling(fig, axs, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis')
plotly_fit = apply_default_plotly_styling(fig, title='Main Title', xaxis_title='X-axis', yaxis_title='Y-axis', legend_title=None)
```

## Running Tests

Unit tests exist for all submodules except `data_viz_formatting`. 

To run the tests, navigate to the root directory of the package and execute:

```bash
python -m unittest discover
```

This will run all the unit tests and provide feedback on the correctness of the various functions within the package.

## Contributing

If you’d like to contribute to the development of `tidbits`, please fork the repository and create a pull request. I welcome contributions that improve existing features, fix bugs, or add new functionality.

### Guidelines:
- Write clear, concise code and include comments where necessary.
- Ensure that your code passes all existing tests and add new tests for any new functionality.
- Follow the PEP 8 style guide for Python code.

## Documentation

This README serves as the primary documentation for `tidbits`, providing an overview of the package, installation instructions, and usage examples. For any additional details or updates, refer to this document.

## License

`tidbits` is licensed under the MIT License. See the [LICENSE](https://github.com/yourusername/tidbits/blob/main/LICENSE) file for more details.


## Roadmap

- Data visualization tests
- Link to example usage in a data science project
- More robust documentation
