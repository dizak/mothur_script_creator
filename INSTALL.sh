#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

_db_answer=''

### Read CLI arguments

while getopts ":p:t:" opt; do
  case $opt in
    p )
    _db_answer='yes'
    _db_path=$OPTARG
      ;;
    t )
    _db_type=$OPTARG
      ;;
    \? )
    printf "Invalid option: -$OPTARG.
    Execute script without any additional arguments to perform guided
    installation.

    To predefine installation parameters use following arguments:
    - p <database_output_path>
    - t <database_names>.
    "
    exit 1
      ;;
  esac
done

### Download database function

download_database() {
  # $1 = ${_db_type}
  # $2 = ${_db_path}
  case $1 in
    1)
    ./mothulity_dbaser.py $2 --unite-ITS-02 &&
    ./mothulity.py . --set-align-database-path "$2/Unite_ITS_02/
    UNITEv6_sh_99.fasta" --set-taxonomy-database-path "$2/UNITEv6_sh_99.tax"
    break
    ;;
    2)
    ./mothulity_dbaser.py $2 --unite-ITS-s-02 &&
    ./mothulity.py . --set-align-database-path "$2/Unite_ITS_s_02/
    UNITEv6_sh_97_s.fasta" --set-taxonomy-database-path "$2/UNITEv6_sh_97_s.tax"
    break
    ;;
    3)
    ./mothulity_dbaser.py $2 --silva-102 &&
    printf 'Silva-102 is not handled automatically yet.
    It was NOT set as default database.'
    break
    ;;
    4)
    ./mothulity_dbaser.py $2 --silva-119 &&
    ./mothulity.py . --set-align-database-path "$2/silva.nr_v119.align"
    --set-taxonomy-database-path "$2/silva.nr_v119.tax"
    break
    ;;
    5)
    ./mothulity_dbaser.py $2 --silva-123 &&
    ./mothulity.py . --set-align-database-path "$2/"
    --set-taxonomy-database-path "$2/"
    break
    ;;
    *)
    echo 'No such database.'
    ;;
  esac
}

### Verify path existance function

verify_path(){
  # $1 = _db_path
  if [ -e "$1" ]; then
    printf "$1 will be set as default database path.\n"
    break
  else
    printf 'Cannot find path. Try again.\n'
  fi
}

### Define variables

_bye_msg="\nThanks for installing mothulity. Hope it will save you as much work as possible!
Report bugs and other issues at https://github.com/dizak/mothulity/issues.\n"
# ~/.bashrc path
_bashrc_path=${HOME}/.bashrc
# mothulity path
cd $(dirname $0)
_mothulity_path=$(pwd)
# is Anaconda installed
_conda_path=$(which conda)
if [ ${#_conda_path} -eq 0 ]; then
  printf 'Please install Anaconda first.\n';
  exit
else
  printf "Found Anaconda in: ${_conda_path}.\n";
fi

### Add mothulity to PATH in .bashrc

printf "\nDo you wish the installer to add mothulity location to PATH in your ~/.bashrc?
[yes|no]\n"
while read _path_export; do
  if [ "${_path_export}" = 'yes' ]; then
    # Backup .bashrc before editing it
    cp ${_bashrc_path} "${_bashrc_path}.bak"
    # Add mothulity to PATH, source it and export PATH just for case
    echo "export PATH=\"${_mothulity_path}:\$PATH\"" >> ${_bashrc_path}
    export PATH=$HOME/${_mothulity_path}:$PATH
    . ${_bashrc_path}
    printf "mothulity location added to PATH in your .bashrc.\n\n"
    break
  elif [ "${_path_export}" = 'no' ]; then
    printf "You may wish to edit your .bashrc"
    printf "or export the mothulity location to PATH later.\n\n"
    break
  else
    printf "Unknown option. Type 'yes' or 'no'.\n"
  fi
done


### Set up and test mothulity

# Create regular mothulity env from mothulity.yaml
conda env create --file "${_mothulity_path}/mothulity.yaml" --force
# Create no-mothur mothulity env from mothulity_sm.yaml
conda env create --file "${_mothulity_path}/mothulity_sm.yaml" --force
# Get python interpreter's location from the env
. activate mothulity
ENV_PYTHON=$(which python)
# Replace shebangs in *py files in mothulity directory
for i in "${_mothulity_path}/*.py"; do
  sed -i "s@/usr/bin/env python@${ENV_PYTHON}@g" $i;
done
# Run doc tests in all the python files
for i in "${_mothulity_path}/*.py"; do
  python -m doctest $i -v;
done
# Go to mothulity directory
cd ${_mothulity_path}
# Run unittests
python -m unittest -v tests.tests;

### Database download
### NOT FINISHED

if [ -z "$_db_answer" ]; then
  printf "Mothulity needs databases to work its magic. Would you like to download them now?
[yes|no]\n"
  while read _db_answer; do
    if [ "${_db_answer}" = 'yes' ]; then
      printf "Where would you like to download it?\n"
      while read _db_path; do
        verify_path ${_db_path}
      done
      break
    elif [ "${_db_answer}" = 'no' ]; then
      printf "${_bye_msg}"
      exit
    fi
  done
fi

echo "1234"
