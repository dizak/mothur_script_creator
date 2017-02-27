# mothulity

Simple tool to facilitate work with [mothur](https://www.mothur.org/).
It can download a proper database, run SOP provided with just fastq files directory, draw few figures and wrap it all into fancy html. Handles slurm and sends e-mail notifications when the job is done (using [headnode_notifier](https://github.com/dizak/headnode_notifier/releases)).


### Installation

1. Requirements.
  * jinja2
  * argparse
  * requests
  * tqdm
  * Biopython
  * matplotlib
  * pylab
  * mpld3
  * pandas
  * seaborn

2. External scripts/programs.
  * [headnode_notifier](https://github.com/dizak/headnode_notifier/releases))
  * [mothur_krona](https://github.com/accaldwell/mothur_krona.git)

3. How to install.
  1. Use python package manager to download and install dependencies.
  2. Add python scripts to system path.

### Usage

The simplest example is:

```
mothulity.py /path/to/fastq/files -r sh
```

Above command will run MiSeq SOP, draw plots, render html output and zip everything.
Omit ```-r``` if you do not want the produced bash script to be executed.
The ```-r``` option accepts any shell of choice. On a regular Linux machine it will be probably ```-r sh```. On, let's say SLURM Queueing System: ```-r -sbatch```. On TORQUE: ```-r qsub```. Mothulity does not really care, it is the matter of the user's system.

You can send results in the email notification with:

```
mothulity.py /path/to/fastq/files -r sh --notify-email your.email@your.domain
```

As ```--notify-email``` depends on headnode_notifier.py, please check its repo for configuration instructions.
