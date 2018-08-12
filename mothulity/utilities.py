#! /usr/bin/env python


from __future__ import print_function
import six
import sys
import os
from glob import glob
from six.moves import configparser
import jinja2 as jj2
import pandas as pd
from bs4 import BeautifulSoup as bs



def get_dir_path(file_name=""):
    """
    Find out what is the script system path and return its location. Optionally
    put desired file name at the end of the path. Facilitates access to files
    stored in the same directory as executed script. Requires the executed
    script being added to the system path

    Parameters
    --------
    file_name: str, default <"">
        File name to put at the end of the path. Use empty string if want just
        the directory.

    Returns
    --------
    str
        System path of the executable.

    Examples
    -------
    >>> get_dir_path() # doctest: +SKIP
    '/home/user/program/bin/'
    >>> get_dir_path("foo") # doctest: +SKIP
    '/home/user/program/bin/foo'
    """
    # prog_path = sys.argv[0].replace(sys.argv[0].split("/")[-1],
    #                                 file_name)
    prog_path = "/".join(sys.argv[0].split("/")[:-1] + [file_name])
    return os.path.abspath(prog_path)


def path2name(path,
              slash="/",
              hid_char=".",
              extension=False):
    """
    Returns just filename with or without extension from the full path.

    Parameters
    -------
    path: str
        Input path.
    slash: str
        Slash to use. Backslash does NOT work properly yet. Default: </>.
    hid_char: str
        Character indicating that file is hidden. Default: <.>
    extension: bool
        Return filename with extension if <True>. Remove extension\
        otherwise. Default: <False>.

    Returns
    -------
    str
        Filename from the path.

    Examples
    -------
    >>> path2name("/home/user/foo.bar")
    'foo'
    >>> path2name("/home/user/.foo.bar")
    'foo'
    >>> path2name("/home/user/foo.bar", extension=True)
    'foo.bar'
    >>> path2name("/home/user/.foo.bar", extension=True)
    'foo.bar'
    """
    if extension is True:
        return str(path.split(slash)[-1].strip(hid_char))
    else:
        return str(path.split(slash)[-1].strip(hid_char).split(".")[0])


def set_config(filename,
               section,
               options,
               values,
               clean=False):
    if os.path.exists(filename):
        config = configparser.ConfigParser()
        config.read(os.path.abspath(filename))
        if clean and section in config.sections():
            config.remove_section(section)
        if section not in config.sections():
            config.add_section(section)
        for o, v in zip(options, values):
            config.set(section, o, v)
        with open(filename, "w") as fout:
            config.write(fout)
    else:
        return None


def load_template_file(template_file,
                       searchpath="/"):
    """
    Load jinja2 template file. Search path starts from root directory so no
    chroot.

    Parameters
    -------
    template_file: str
        Template file name.
    searchpath: str, default </>
        Root directory for template lookup.

    Returns
    -------
    jinja2.Template

    Examples
    -------
    >>> import jinja2
    >>> lt = load_template_file("./tests/test.jj2", searchpath=".")
    >>> isinstance(lt, jinja2.environment.Template)
    True
    """
    template_Loader = jj2.FileSystemLoader(searchpath=searchpath)
    template_Env = jj2.Environment(loader=template_Loader)
    template = template_Env.get_template(template_file)
    return template


def render_template(template_loaded,
                    template_vars):
    """
    Render jinja2.Template to unicode.

    Parameters
    -------
    loaded_template: jinj2.Template
        Template to render.
    template_vars: dict
        Variables to be rendered with the template.

    Returns
    -------
    unicode
        Template content with passed variables.

    Examples
    -------
    >>> lt = load_template_file("./tests/test.jj2",\
    searchpath=".")
    >>> vars = {"word1": "ipsum", "word2": "adipisicing", "word3": "tempor"}
    >>> rt = render_template(lt, vars)
    >>> str(rt)
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.'
    """
    template_rendered = template_loaded.render(template_vars)
    return template_rendered


def save_template(out_file_name,
                  template_rendered):
    """
    Save rendered template to file.

    Parameters
    -------
    out_file_name: str
        Output file name.
    template_rendered: unicode
        Temlplate rendered to unicode object.
    """
    with open(out_file_name, "wb") as fout:
        fout.write(template_rendered.encode("utf-8"))


def read_info_shared(input_file_name,
                     min_fold=5,
                     label_col="label",
                     group_col="Group",
                     otu_col="Otu",
                     num_col="numOtus",
                     sep="\t",
                     format_junk_grps=True):
    """
    Extracts information from mothur's shared file.

    Parameters
    -------
    input_file_name: str
        Input file name.
    min_fold: int
        Fraction of mean group size below which groups will be removed before
        analysis.
    label_col: str
        Label column name in shared file.
    group_col: str
        Group column name in shared file.
    otu_col: str
        OTU column name prefix in shared file.
    num_col: str
        Number of OTUs column name in shared file.
    sep: str, default <\t>
        Delimiter to use for reading-in shared file.
    format_junk_grps: bool, default <True>
        Join names of groups to remove by <-> before passing to mothur.

    Returns
    -------
    dict
        Information about label, number of samples and groups to remove.

    Examples
    -------
    >>> shared_info = read_info_shared(input_file_name="./tests/test.shared")
    >>> shared_info["samples_number"]
    9
    >>> float(shared_info["label"])
    0.03
    >>> shared_info["junk_grps"]
    'F3D141-F3D143-F3D144'
    """
    dtypes = {label_col: "str"}
    shared_df = pd.read_csv(input_file_name, sep=sep, dtype=dtypes)
    otus_cols = [i for i in shared_df.columns if otu_col in i and i != num_col]
    grps_sizes = shared_df[[group_col] + otus_cols].sum(axis=1)
    label = shared_df[label_col][0]
    grps_num = len(shared_df[group_col])
    sizes_df = pd.DataFrame({"GROUPS": shared_df[group_col],
                             "GROUP_SIZES": grps_sizes})
    threshold = sizes_df.GROUP_SIZES.mean() / min_fold
    size_bool = (sizes_df.GROUP_SIZES < threshold)
    junk_grps = list(sizes_df[size_bool].GROUPS)
    if format_junk_grps is True:
        junk_grps = "-".join(junk_grps)
    out_dict = {"label": label,
                "samples_number": grps_num,
                "junk_grps": junk_grps}
    return out_dict


def parse_html(input_file_name,
               html_type,
               parser="html.parser",
               newline="\n"):
    """
    Extract particular tags from html so that they can be placed in
    another html without iframe.

    Parameters
    -------
    input_file_name: str
        Input file name.

    """
    with open(input_file_name) as fin:
        html = fin.read()
    soup = bs(html, parser)
    if html_type == "krona":
        head = [str(i) for i in soup.head if i != newline]
        body = [str(i) for i in soup.body if i != newline]
        return {"head": {"link": head[1],
                         "script_not_found": head[2],
                         "script_functional": head[3]},
                "body": {"img_hidden": body[0],
                         "img_loading": body[1],
                         "img_logo": body[2],
                         "noscript": body[3],
                         "div_krona": body[4]}}
    elif html_type == "summary":
        tags = [str(i) for i in list(soup.children) if i != "\n"]
        return {"link": tags[0],
                "table": tags[1],
                "googleapis_script": tags[3],
                "datatables_script": tags[4],
                "script": tags[5]}
    elif html_type == "rarefaction" or html_type == "nmds":
        return {"div": str(soup.div),
                "script": str(soup.script)}
