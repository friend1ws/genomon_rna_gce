[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# genomon_rna_gce

This is a software to perform cancer transcriptome sequence analysis using Google Compute Engine.
More specifically: 
* Execute alignment of fastq files (assuming these are set up at Google Cloud Storage) using [STAR](https://github.com/alexdobin/STAR).
* Identify fusion transcripts using our inhouse software ([fusionfusion](https://github.com/Genomon-Project/fusionfusion)).
* Key result files (BAM files and fusion transcripts) are put in Google Cloud Storage.
This software heavily rely on a great batch job engine software, [dsub](https://github.com/googlegenomics/dsub).

# Installation

```sh
git clone git@github.com:friend1ws/genomon_rna_gce.git
cd genomon_rna_gce
pip install . --upgrade
```

# Prerequisites

Since this software heavily rely on the dsub software,
You need to set up for dsub.

1. Sign up for a Google Cloud Platform accout and create your project.
1. Enable the APIs.
1. Install the Google Cloud SDK.
1. And `GOOGLE_APPLICATION_CREDENTIALS` on your machine and JSON file representing the credentials, which is created by `gcloud application-default login` (See [here](https://developers.google.com/identity/protocols/application-default-credentials) for more information).
1. Create a Google Cloud Storage bucket.

See **Getting started on Google Cloud** section in the README.md file in the dsub repository.

# Quick Start

```sh
genomon_rna_gce \
  ./example/sample-conf.tsv \
  gs://rnaseq_cellline/test171113 \
  ./example/param.cfg
```

