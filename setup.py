import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='SGnet',  
     version='0.1',
     scripts=['sgnet.py'] ,
     author="Akshat Gupta",
     author_email="akshat41121995@gmail.com",
     description="Python package for spelling and grammar correction",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/akshat4112/sgnet",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "License :: OSI Approved :: BSD Clause 3 License",
         "Operating System :: OS Independent",
     ],
 )