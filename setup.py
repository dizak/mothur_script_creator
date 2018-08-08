from setuptools import find_packages
from distutils.core import setup
from mothulity import __version__ as VERSION
from mothulity import __author__ as AUTHOR


setup(
    name="mothulity",
    version=VERSION,
    author=AUTHOR,
    packages=find_packages(exclude=["*test*"]),
    include_package_data=True,
    data_files=[
        ("bin", ["mothulity.config"])
    ],# NOTE: tells where files should be installed - see https://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    install_requires=open("requirements.txt").readlines(),
    description="Easy-to-use tool facilitating work with Mothur.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="dariusz.izak@ibb.waw.pl",
    url="https://github.com/dizak/mothulity",
    license="BSD",
    py_modules=[
        "__author",
        "__version",
        "utilities",
    ],
    scripts=[
        "mothulity.py",
        "mothulity_draw.py",
        "mothulity_dbaser.py",
        "mothulity_fc.py",
     ],
    keywords=[
        "mothur",
        "diversity",
        "microbial-communities",
        "microbial-ecology",
        "16s",
        "16s-rrna",
        "its",
        "microbial",
        "fungal",
        "easy-to-use",
        ""
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
