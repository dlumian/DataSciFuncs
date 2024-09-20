import re
import requests
from pathlib import Path

def get_version_from_setup():
    setup_path = Path("setup.py")
    with setup_path.open() as f:
        content = f.read()

    version_match = re.search(r"version=['\"]([^'\"]+)['\"]", content)
    if version_match:
        return version_match.group(1)
    else:
        raise ValueError("Version not found in setup.py")

def get_pypi_versions(package_name, test=False):
    if test:
        url = f"https://test.pypi.org/pypi/{package_name}/json"
    else:
        url = f"https://pypi.org/pypi/{package_name}/json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("releases", {}).keys()
    else:
        return []

def increment_version(version):
    parts = version.split('.')
    parts[-1] = str(int(parts[-1]) + 1)  # Increment the patch version
    return '.'.join(parts)

def check_version_and_prompt(package_name):
    current_version = get_version_from_setup()
    pypi_versions = get_pypi_versions(package_name)
    test_pypi_versions = get_pypi_versions(package_name, test=True)

    if current_version in pypi_versions or current_version in test_pypi_versions:
        new_version = increment_version(current_version)
        print(f"Version {current_version} already exists. Suggesting new version: {new_version}")
        # You can automate updating the version in setup.py if desired.
    else:
        print(f"Version {current_version} is available for release.")

# Replace 'your_package_name' with the actual name of your package.
check_version_and_prompt('your_package_name')