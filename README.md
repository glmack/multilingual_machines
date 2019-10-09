**[summary](#multilingual_machines) | [usage](#usage) | [running in a notebook](#running-the-notebooks) | [license](#license)**

## Measuring Multilingual Machines
#### Exploring BLEU Scores using Translated Patent Data

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/glmack/multilingual_machines/master?filepath=blob%2Fmaster%2Fmultilingual_machines.ipynb)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<img src="translator_cartoon.jpg" width=60% align="middle">

This repo accompanies the Medium article titled "Measuring Multilingual Machines"

Implements walk-through of BLEU score example using cross-lingual patent documents

#### Summary
This repo accompanies an article that takes an initial dive into the lessons, implementations, and limits of BLEU, a machine translation evaluation algorithm, using examples drawn from multilingual patent documents. 

### Business understanding
How might a researcher or business leader quickly evaluate the quality of machine translations? This question encapsulates the basic challenge that gives rise to the BLEU metric. BLEU, which stands for bilingual language understudy, is a default measure of machine translation quality and is also sometimes applied to cross-lingual natural language processing (NLP) tasks. The metric is well-established in the machine translation space but some analysts question its application to a wider set of tasks beyond the original purpose for which the algorithm was developed. This article explores these issues.

#### Data
A growing share of patents in the machine learning space is written and filed in Chinese according to a recent report by WIPO (World Intellectual Property Organization), the global organization that governs patents. To explore the basics of BLEU in this multilingual space, this repo uses example data from a recent Chinese patent of an NLP innovation that the e-commerce company Alibaba extended to patent coverage on a global scale. For additional details on the example patent, WIPO's data query tool provides both [English](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2019085779) and [Chinese](https://patentscope.wipo.int/search/zh/detail.jsf?docId=WO2019085779) language versions that you can inspect in your browser. 

#### Usage
*Option 1*: Access on Binder
Interact with the English language notebooks in a live environment on Binder, which builds a Docker image of this repository. A JupyterHub server hosts the repository's contents that you can access through a reusable link.

*Option 2*: Access on nbviewer 
Nbviewer, an open source project under the Project Jupyter initiative, is a web application that renders the notebook as a static HTML web page, and provides a stable link to browse the notebook in this repo.

https://nbviewer.jupyter.org/github/glmack/multilingual_machines/blob/master/multilingual_machines.ipynb

*Option 3*: Clone repo

To clone this repository from a command line, run

git clone https://github.com/glmack/multilingual_machines
Then cd into the multilingual_machines directory: cd multilingual_machines

Dependencies are specified in requirements.txt

pip install -r requirements.txt
To run the notebooks locally, you will need to have python installed, preferably through anaconda .

To setup your software environment, you use the provided conda environment:

conda env create -f environment.yml
conda activate multilingual_machines-env
You can then launch Jupyter in your web browser

jupyter notebook
