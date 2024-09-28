import os
import re
import sys
import pprint
import requests
import argparse
import subprocess
from pathlib import Path


def get_version_from_setup(path):
    setup_file_path = os.path.join(path, 'setup.py')
    setup_path = Path(setup_file_path)
    with setup_path.open() as f:
        content = f.read()

    version_match = re.search(r"version=['\"]([^'\"]+)['\"]", content)
    if version_match:
        return version_match.group(1)
    else:
        raise ValueError("Version not found in setup.py")

def get_versions(package_name, repository="testpypi"):
    if repository == "testpypi":
        url = f"https://test.pypi.org/pypi/{package_name}/json"
    else:
        url = f"https://pypi.org/pypi/{package_name}/json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("releases", {}).keys()
    else:
        return []

def check_version_and_prompt(path, package_name, repository="testpypi"):
    current_version = get_version_from_setup(path=path)
    url_versions = get_versions(package_name, repository=repository)
    if not current_version in url_versions:
        print(f"Version {current_version} is available for release.")
        print(f"Proceeding with upload...")
    else:
        print(f"Version {current_version} already exists.")
        print(f"Existing versions found are: {', '.join(url_versions)}.")
        print(f'Exiting this run. Please update version and try again.')
        sys.exit(1)

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

def conda_env_exists(env_name):
    result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
    return env_name in result.stdout

def remove_conda_env(env_name):
    """Check if env exists and remove if environment found."""
    if conda_env_exists(env_name):
        print(f"Environment '{env_name}' exists. Removing it now.")
        subprocess.run(['conda', 'remove', '--name', env_name, '--all', '-y'])
        print(f"Environment '{env_name}' has been removed.")
    else:
        print(f"Environment '{env_name}' does not exist. Nothing to remove.")

def create_conda_env(env_name):
    """Create a clean conda environment."""
    print(f"Creating a clean conda environment: {env_name}")
    run_command(f"conda create -n {env_name} python=3.11 -y")

def install_package(env_name, package_name, repository):
    """Install the package from the specified repository (Test PyPI or PyPI)."""
    print(f"Installing the package '{package_name}' from {repository} in environment '{env_name}'...")
    if repository == "pypi":
        run_command(f"conda run --name {env_name} pip install {package_name}")
    else:
        run_command(f"conda run --name {env_name} pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple {package_name}")

def full_pipeline(repo_path, env_name="testenv", package_name="datascifuncs", repository="testpypi"):
    """Run the full pipeline: clean, build, upload, create env, install."""
    check_version_and_prompt(path=repo_path,package_name=package_name, repository=repository)
    clean_build(repo_path)
    build_package(repo_path)
    upload_package(repo_path, repository)
    remove_conda_env(env_name)
    create_conda_env(env_name)
    install_package(env_name, package_name, repository)

def main():
    """Runs a package build based on passed arguments and a setup.py file.
    path: string of path to repository directory containing setup.py file
    env-name: name of conda envrionment created and used for testing
    package-name: string to use for name of package
    repository: string of either testpypi or pypi defining where to load package to

    Examples of shell usage after package install:

    build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name test_env --package-name datascifuncs --repository testpypi

    build-pipeline --path /Users/dsl/Documents/GitHub/DataSciFuncs --env-name prod_env --package-name datascifuncs --repository pypi
    """
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
    # Print all settings before beginning the run
    # Convert arguments to a dictionary
    args_dict = vars(args)

    print("Arguments received:")
    print("\n")
    pprint.pprint(args_dict, indent=4)
    print("\n\n")
    print("Proceeding with the script...")

    # Run the full pipeline with the provided arguments
    full_pipeline(args.path, env_name=args.env_name, package_name=args.package_name, repository=args.repository)


if __name__ == "__main__":
    main()
