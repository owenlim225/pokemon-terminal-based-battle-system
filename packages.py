import subprocess
import sys
import importlib.util

# =======================================
# List of dependencies to install
#
# Add your dependencies here
# =======================================
dependencies = [
    "rich"
]

def install_package(package):
    # Install a package using pip, with better error handling
    result = subprocess.run([sys.executable, "-m", "pip", "install", package], check=False)
    if result.returncode != 0:
        raise Exception(f"Failed to install {package}. Exit code: {result.returncode}")

def check_and_install_pip():
    # Check if pip is installed, and install if it's not
    if importlib.util.find_spec("pip") is not None:
        print("pip is already installed.")
    else:
        print("pip is not installed. Installing pip...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])

def initialize_packages():
    # Check if pip is installed
    check_and_install_pip()

    for package in dependencies:
        try:
            install_package(package)
            print(f"Installed {package}.")
        except Exception as e:
            print(f"Failed to install {package}: {e}")
            continue  # Continue with other dependencies even if one fails

if __name__ == "__main__":
    initialize_packages()
