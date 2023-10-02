from setuptools import setup, find_packages

setup(
    name="ezplotly",
    version="1.0.4",
    description="Package to make the use of Plotly library easier",
    author="Saeid Alizadeh",
    author_email="saeidalz96@gmail.com",
    url="https://github.com/saeidalz13/ezplotly",
    packages=find_packages(),
    install_requires=[
        "plotly",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization"
    ]
)