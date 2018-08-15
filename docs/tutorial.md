---
layout: default
---

[Home](./index.md)
[FAQs](./faqs.html)
[Tutorial](./tutorial.html)


# Tutorial


## Table of Contents

[Minimal Example](#minimal-example)

[Installing](#installing)

[Downloading Databases](#downloading-databases)

[Setting Persistent Database Path](#setting-persistent-database-path)

[Running Analysis](#running-analysis)

```mothulity``` is simple to use. Nevertheless, it won't hurt to show some brief usage example.


## Minimal Example


Below you can find a minimal example of installation, setting things up and usage.
It should be self-explainatory. If not - each step is explained in the subsequent sections.


```bash
mkdir databases_directory
pip install mothulity
mothulity_dbaser databases_directory --silva-119
--set-align-database-path databases_directory/silva.nr_v119.align
--set-taxonomy-database-path databases_directory/silva.nr_v119.tax
mothulity project/fastq/directory -r bash -n project_name
```


## Installing


```mothulity``` is available as Python package. It can be installed with pip:


```bash
pip install mothulity
```


```mothulity``` comes with [Mothur](https://mothur.org/wiki/Main_Page) bundled.
If you are fine with this, go ahead and install it system-wide.
Nevertheless, it is a good practise to install software in a separate, [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/).


## Downloading Databases


There would be no 16S/ITS analysis with a database.
```mothulity_dbaser``` can help with that - give it a path where you want your files to be downloaded and type of the database.


### Example


```bash
mothulity_dbaser ~/databases --silva-119
```


## Setting Persistent Database Path


```mothulity``` needs to know where the databases live.You can specify the path each time you run the analysis with:



```bash
--align-database ~/databases/silva.nr_v119.align
```


and


```bash
--taxonomy-database ~/databases/silva.nr_v119.tax
```


or you can set it persistently with:


```bash
--set-align-database-path ~/databases/silva.nr_v119.align
```


and


```bash
--set-taxonomy-database-path ~/databases/silva.nr_v119.tax
```


## Running Analysis


Once the databases path is set up, you can easily run your analysis:

```bash
mothulity project/path -r bash -n project_name
```

```project/path``` tells ```mothulity``` where are your fastq files.

```-r bash``` indicates shell to use. If you are using some *exotic* shell, pass its name here. If you are using workload manager, use a command to submit a job. For [SLURM](https://slurm.schedmd.com/) it would be ```sbatch```

```-n project_name``` is used to name files, directories and title the final output.
