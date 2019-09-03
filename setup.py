import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='spellygrammarc',  
     version='0.1',
     author="Akshat Gupta",
     author_email="akshat41121995@gmail.com",
     py_modules = ["spellygrammarc"],
     description="Python package for spelling and grammar correction",
     url="https://github.com/akshat4112/sgnet",
     package_dir={'':'src'},
    )
