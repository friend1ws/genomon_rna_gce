#! /usr/bin/env python

from genomon_rna_gce.run import *
import argparse

def main():

    parser = argparse.ArgumentParser(prog = "genomon_rna_gce")

    parser.add_argument("--version", action = "version", version = "genomon_rna_gce-0.1.0")
    
    parser.add_argument("sample_conf_file", default = None, type = str, help = "Sample config file")

    parser.add_argument("output_dir", default = None, type = str,
                        help = "Output directory for Google Cloud Storage")

    parser.add_argument("param_conf_file", help = "Parameter config file", type = str)

    args = parser.parse_args()

    run(args)

