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
        ("bin", [
            "mothulity.config",
            "preproc_template.sh.j2",
            "output_template.html.j2",
            "analysis_template.sh.j2",
            ]),
        ("bin/blast/bin", [
            "bin/mothur/blast/bin/bl2seq",
            "bin/mothur/blast/bin/blastall",
            "bin/mothur/blast/bin/blastclust",
            "bin/mothur/blast/bin/blastpgp",
            "bin/mothur/blast/bin/copymat",
            "bin/mothur/blast/bin/fastacmd",
            "bin/mothur/blast/bin/formatdb",
            "bin/mothur/blast/bin/formatrpsdb",
            "bin/mothur/blast/bin/impala",
            "bin/mothur/blast/bin/makemat",
            "bin/mothur/blast/bin/megablast",
            "bin/mothur/blast/bin/rpsblast",
            "bin/mothur/blast/bin/seedtop",
        ]),
        ("bin", [
            "bin/mothur/mothur",
            "bin/mothur/uchime",
            "bin/mothur/vsearch",
        ]),
    ],
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
