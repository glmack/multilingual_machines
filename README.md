[summary](#summary) | [usage](#usage)
## Measuring Multilingual Machines
#### Exploring BLEU Scores using Patent Data

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<img src="headline_img.jpg" width=80% align="middle">

This repo accompanies the article ["Multilingual Machine Learning"](https://towardsdatascience.com/multilingual-machine-learning-972de4248218)

#### Summary
This repo accompanies an article that takes an initial dive into the lessons, implementations, and limits of BLEU, a machine translation evaluation algorithm, using examples drawn from multilingual patent documents. 

#### Business understanding
How might a researcher or business leader quickly evaluate the quality of machine translations? This question encapsulates the basic challenge that gives rise to the BLEU metric. BLEU, which stands for bilingual language understudy, is a default measure of machine translation quality and is also sometimes applied to cross-lingual natural language processing (NLP) tasks. The metric is well-established in the machine translation space but some analysts question its application to a wider set of tasks beyond the original purpose for which the algorithm was developed. This article explores these issues using patent texts.

#### Data
A growing share of patents in the machine learning space is written and filed in Chinese according to a recent report by WIPO (World Intellectual Property Organization), the global organization that governs patents. To explore the basics of BLEU in this multilingual space, this repo uses example data from a recent Chinese patent of an NLP innovation that the e-commerce company Alibaba extended to global coverage. For additional details on the example patent, titled "Machine Processing and Text Correction Method and Device, Computing Equipment and Storage Media", WIPO's data query tool provides both [English](https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2019085779) and [Chinese](https://patentscope.wipo.int/search/zh/detail.jsf?docId=WO2019085779) language versions that you can inspect in your browser. 

#### Usage for notebooks

*Option 1*: Access [English language notebook via nbviewer](https://nbviewer.jupyter.org/github/glmack/multilingual_machines/blob/master/multilingual_machines_en.ipynb)
, an open source web application that renders the notebook as a static HTML web page to browse the notebook

Access [Chinese language notebook via nbviewer](https://nbviewer.jupyter.org/github/glmack/multilingual_machines/blob/master/multilingual_machines_ch.ipynb)
, an open source web application that renders the notebook as a static HTML web page to browse the notebook

*Option 2*: Clone repository from command line:
1. Clone repository: git clone https://github.com/glmack/multilingual_machines

2. Navigate into multilingual_machines directory: cd multilingual_machines

3. Set up software environment:
      conda env create -f environment.yml
      conda activate default-env
 
4. Run English language notebook: 
      jupyter notebook multilingual_machines/blob/master/multilingual_machines_en.ipynb
 
5. Run Chinese language notebook: 
      jupyter notebook multilingual_machines/blob/master/multilingual_machines_ch.ipynb
