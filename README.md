[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# genomon_rna_gce

This is a software to perform cancer transcriptome sequence analysis using Google Compute Engine.
More specifically, it execute alignment of fastq files (assuming these are set up at Google Cloud Storage) using [STAR](https://github.com/alexdobin/STAR), 
and then fusion transcripts are identified using our inhouse software ([fusionfusion](https://github.com/Genomon-Project/fusionfusion)).
Key result files (BAM files and fusion transcripts are loaded to Google Cloud Storage).
This software heavily rely on a great batch job engine software, [dsub](https://github.com/googlegenomics/dsub).

1. Assume the paired-end fastq files (transcriptome sequencing data) are at Google Cloud Storage
1. First, these fastq files are extracted to the virtual machines at 
Perform Genomon RNA pipeline in Google Compute Engine.

# Installation

```sh
git clone git@github.com:friend1ws/genomon_rna_gce.git
cd genomon_rna_gce
pip install . --upgrade
```

# Quick Start

```sh
genomon_rna_gce \
  ./example/sample-conf.tsv \
  gs://rnaseq_cellline/test171113 \
  ./example/param.cfg
```

# Prerequisites

- Python2.7
- dsub
- gsutil

And `GOOGLE_APPLICATION_CREDENTIALS` on your machine and JSON file representing the credentials, which is created by `gcloud application-default login`.

See [here](https://developers.google.com/identity/protocols/application-default-credentials) for more information.
