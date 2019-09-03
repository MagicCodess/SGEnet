import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='spellygrammar',  
     version='0.2',
     author="Akshat Gupta",
     author_email="akshat41121995@gmail.com",
     py_modules = ["spellygrammar"],
     description="Python package for spelling and grammar correction",
     url="https://github.com/akshat4112/sgnet",
     package_dir={'':'src'},
    )
