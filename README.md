[summary](#multilingual_machines) | [usage](#usage) | [run notebooks](#running-the-notebooks)
## Measuring Multilingual Machines
#### Exploring BLEU Scores using Patent Data

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/glmack/multilingual_machines/master?filepath=blob%2Fmaster%2Fmultilingual_machines.ipynb)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<img src="translator_cartoon.jpg" width=80% align="middle">

This repo accompanies the article titled "Multilingual Machine Learning"

#### Summary
This repo accompanies an article that takes an initial dive into the lessons, implementations, and limits of BLEU, a machine translation evaluation algorithm, using examples drawn from multilingual patent documents. 

### Business understanding
How might a researcher or business leader quickly evaluate the quality of machine translations? This question encapsulates the basic challenge that gives rise to the BLEU metric. BLEU, which stands for bilingual language understudy, is a default measure of machine translation quality and is also sometimes applied to cross-lingual natural language processing (NLP) tasks. The metric is well-established in the machine translation space but some analysts question its application to a wider set of tasks beyond the original purpose for which the algorithm was developed. This article explores these issues using patent texts.

#### Data
A growing share of patents in the machine learning space is written and filed in Chinese according to a recent report by WIPO (World Intellectual Property Organization), the global organization that governs patents. To explore the basics of BLEU in this multilingual space, this repo uses example data from a recent Chinese patent of an NLP innovation that the e-commerce company Alibaba extended to global coverage. For additional details on the example patent, titled "Machine Processing and Text Correction Method and Device, Computing Equipment and Storage Media", WIPO's data query tool provides both [English](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2019085779) and [Chinese](https://patentscope.wipo.int/search/zh/detail.jsf?docId=WO2019085779) language versions that you can inspect in your browser. 

#### Usage
*Option 1*: Access on [Binder](https://mybinder.org/v2/gh/glmack/multilingual_machines/master?filepath=blob%2Fmaster%2Fmultilingual_machines.ipynb)
Interact with the English language notebooks in a live environment on Binder, which builds a Docker image of this repository. A JupyterHub server hosts the repository's contents that you can access through a reusable link.


*Option 2*: Access on [nbviewer](https://nbviewer.jupyter.org/github/glmack/multilingual_machines/blob/master/multilingual_machines.ipynb)
Nbviewer, an open source project under the Project Jupyter initiative, is a web application that renders the notebook as a static HTML web page, and provides a stable link to browse the notebook in this repo.

*Option 3*: Clone repository from a command line:

1. git clone https://github.com/glmack/multilingual_machines
2. cd into the multilingual_machines directory: cd multilingual_machines
