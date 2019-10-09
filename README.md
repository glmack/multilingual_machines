**[summary](#multilingual_machines) | [usage](#usage) | [running in a notebook](#running-the-notebooks) | [license](#license)**

## Measuring Multilingual Machines
#### Exploring BLEU Scores using Translated Patent Data

[![Binder](https://hub.gke.mybinder.org/user/glmack-multilingual_machines-9q2foo49/notebooks/multilingual_machines.ipynb)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<img src="img.png" width=60% align="middle">

This repo accompanies the Medium article titled "Measuring Multilingual Machines"

Implements walk-through of BLEU score example using cross-lingual patent documents

#### Summary
This repo accompanies an article that takes an initial dive into the lessons, implementations, and limits of BLEU, a machine translation evaluation algorithm, using examples drawn from multilingual patent documents. 

### Business understanding
How might a researcher or business leader quickly evaluate the quality of machine translations? This question encapsulates the basic challenge that gives rise to the BLEU metric. BLEU, which stands for bilingual language understudy, is a default measure of machine translation quality and is also sometimes applied to cross-lingual natural language processing (NLP) tasks. The metric is well-established in the machine translation space but some analysts question its application to a wider set of tasks beyond the original purpose for which the algorithm was developed. This article explores these issues.

#### Data
A growing share of patents in the machine learning space is written and filed in Chinese according to a recent report by WIPO (World Intellectual Property Organization), the global organization that governs patents. To explore the basics of BLEU in this multilingual space, this repo uses example data from a recent Chinese patent of an NLP innovation that the e-commerce company Alibaba extended to patent coverage on a global scale. For additional details on the example patent, WIPO's data query tool provides both [English](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2019085779) and [Chinese](https://patentscope.wipo.int/search/zh/detail.jsf?docId=WO2019085779) language versions that you can inspect in your browser. 

#### Usage
Dependencies are specified in requirements.txt

pip install -r requirements.txt
To run the notebooks locally, you will need to have python installed, preferably through anaconda .

To clone this repository from a command line, run

git clone https://github.com/glmack/multilingual_machines
Then cd into the multilingual_machines directory: cd multilingual_machines

To setup your software environment, you use the provided conda environment:

conda env create -f environment.yml
conda activate multilingual_machines-env
You can then launch Jupyter in your web browser

jupyter notebook

nbviewer is a web application that lets you enter the URL of a Jupyter Notebook file, renders that notebook as a static HTML web page, and gives you a stable link to that page which you can share with others. nbviewer also supports browsing collections of notebooks (e.g., in a GitHub repository) and rendering notebooks in other formats (e.g., slides, scripts).

nbviewer is an open source project under the larger Project Jupyter initiative along with other projects like Jupyter Notebook, JupyterLab, and JupyterHub.

https://nbviewer.jupyter.org/github/glmack/multilingual_machines/blob/master/multilingual_machines.ipynb
