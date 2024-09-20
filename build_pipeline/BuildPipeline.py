import os
import subprocess
import sys
import argparse

def run_command(command, cwd=None):
    """Helper function to run a shell command and handle errors."""
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

def clean_build(repo_path):
    """Remove build artifacts."""
    print("Cleaning old build artifacts...")
    run_command(f"rm -rf {os.path.join(repo_path, 'dist/')} {os.path.join(repo_path, 'build/')} {os.path.join(repo_path, '*.egg-info')}")

def build_package(repo_path):
    """Build the package."""
    print("Building the package...")
    run_command("python -m build", cwd=repo_path)

def upload_package(repo_path, repository):
    """Upload the package to the specified repository (PyPI or Test PyPI)."""
    print(f"Uploading package to {repository}...")
    if repository == "pypi":
        run_command(f"twine upload {os.path.join(repo_path, 'dist/*')}")
    else:
        run_command(f"twine upload --repository testpypi {os.path.join(repo_path, 'dist/*')}")

def create_conda_env(env_name):
    """Create a clean conda environment."""
    print(f"Creating a clean conda environment: {env_name}")
    run_command(f"conda create -n {env_name} python=3.11 -y")

def install_package(env_name, package_name, repository):
    """Install the package from the specified repository (Test PyPI or PyPI)."""
    print(f"Installing the package '{package_name}' from {repository} in environment '{env_name}'...")
    run_command(f"conda init")
    if repository == "pypi":
        run_command(f"conda activate {env_name} && pip install {package_name}")
    else:
        run_command(f"conda activate {env_name} && pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple {package_name}")

def full_pipeline(repo_path, env_name="testenv", package_name="datascifuncs", repository="testpypi"):
    """Run the full pipeline: clean, build, upload, create env, install."""
    clean_build(repo_path)
    build_package(repo_path)
    upload_package(repo_path, repository)
    create_conda_env(env_name)
    install_package(env_name, package_name, repository)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run the build and upload pipeline for a Python package.")
    parser.add_argument(
        "--path",
        required=True,
        help="Path to the repository where the package is located."
    )
    parser.add_argument(
        "--env-name",
        default="testenv",
        help="Name of the conda environment to create and use. Defaults to 'testenv'."
    )
    parser.add_argument(
        "--package-name",
        default="datascifuncs",
        help="Name of the package to install from PyPI or Test PyPI. Defaults to 'datascifuncs'."
    )
    parser.add_argument(
        "--repository",
        choices=["testpypi", "pypi"],
        default="testpypi",
        help="Choose the repository to upload to: 'testpypi' or 'pypi'. Defaults to 'testpypi'."
    )

    args = parser.parse_args()

    # Run the full pipeline with the provided arguments
    full_pipeline(args.path, env_name=args.env_name, package_name=args.package_name, repository=args.repository)

# ### Example:
# - To run the pipeline and upload to **Test PyPI**:
#    ```bash
#    python BuildPipeline.py --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name test_env --package-name datascifuncs --repository testpypi
#    ```
  
# - To run the pipeline and upload to **PyPI**:
#    ```bash
#    python BuildPipeline.py --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name prod_env --package-name datascifuncs --repository pypi
#    ```