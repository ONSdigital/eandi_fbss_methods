from setuptools import setup, find_packages

setup(
    name='eandi_fbss_methods',
    version='0.1.0',
    description='Editing and Imputation methods for business statistics.',
    url='https://github.com/ONSdigital/eandi_fbss_methods',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(where="example_package"),
    # install_requires=,
    python_requires=">=3.10",
)
