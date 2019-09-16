import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='sgenet',  
     version='0.2',
     author="Akshat Gupta",
     author_email="akshat41121995@gmail.com",
     py_modules = ["sgenet"],
     description="Python package for spelling and grammar correction",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/akshat4112/sgenet",
     packages=setuptools.find_packages(),
     package_dir={'':'src'},
    )
