from setuptools import find_packages, setup

setup(
    name="fbr",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
        "requests",
        "pandas",
        "django",
        "dj_database_url",
    ],
    entry_points={
        "console_scripts": [
            # Define command-line scripts here if needed
            # e.g., 'my-command = fbr.module:function',
        ],
    },
)
