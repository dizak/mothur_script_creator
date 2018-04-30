# Contributing to mothulity

You are more than welcome to contribute and if you do - great thanks! :+1:
Below you can find description of mothulity structure and contribution guidelines.

## mothulity structure

The phylosophy behind mothulity is simple:

1. gather all the info from the user which short one-liner.

2. run Mothur

3. gather the Mothur's output and present it with

### mothulity_fc

Mothur needs

```
creates mothur-suitable <.files> file just upon the input file names. Removes
<-> from file names

positional arguments:
  path/to/files         input directory path.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -o , --output         output file name. Default <mothur.files>
  -s , --split-sign     first group of characters before this sign is
                        recognized as sample name. Default <_>
  -e , --files-extension
                        reads files are recognized by this. Default <fastq>
  -l , --left-reads-sign
                        left reads files are recognized by this. Default <R1>
  -r , --right-reads-sign
                        right reads files are recognized by this. Default <R2>
  --original-names      use if you do not want to modify file names
```

## Branch names

It is strongly suggested to name your branches as name-of-issue#number-of-issue.
For instance: no-email-notification#13 or cleaner-code-in-decision-tree#17.
Such naming convention is simple and informative.
