This course is mostly based on [teachopencadd](https://github.com/volkamerlab/teachopencadd).

Launch notebooks with Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD)

GSON Chimie-informatique
========================
___Organisation of "GSON chimie informatique sous python" lessons :___

**Lundi 10 janvier 2022 13h30-17h30**

- Introduction

  - Slides 1_GSON_intro (30 min) PYL
  - Slides 2_introduction_informatique (30 min) XM
  - Talktorial Introductif 1 Intro Python, jupyter (40 min) XM
  - Talktorial Introductif 2 Intro chemoinfo - RDKit (1h20) XM

**Mardi 11 janvier 13h30-17h30**

- Data Acquisition (2h-2h30) XM

  - Talktorial 1 Data acquisition from ChEMBL

- Filtering (1h45-2h) PYL

  - Descriptors and ADME (1h30)

    - Slides 4_Descripteurs_fingerprints
    - Talktorial 2 Molecular filtering: ADME/Lipinski criteria

**Mercredi 12 janvier 13h30-17h30**

- ACP (2h) PYL
  - Slides 3_Intro_ACP
  - Notebook ACP

- Filtering (1h) PYL

  - Talktorial 3 Substructure removal : PAINS

- Ligand based Screening (2h45) XM

  - Slides 5_fingerprint_similarity (45 mins)

**Jeudi 13 janvier 13h30-17h30**

- Ligand based Screening (2h45) XM

  - Talktorial 4 Fingerprints and Molecular Similarity (2h)

- Clustering (1h45) XM

  - Talktorial 5 : Compound clustering (1h15)
  - Talktorial 6 : MCS (30 min)

**Vendredi 14 janvier 13h30-17h30**

- Machine Learning (1h45) PYL

  - 6_Machine Learning
  - Talktorial 7 Machine Learning (ROC curve) PYL

- Exam + correction explication (2h)

## History

- 2018: Fabrice, Colin

- 2019: Colin, Gautier

- 2020: Gautier, Pierre-Yves

    - 21 students
    - Integration of TeachOpenCADD and binder

- 2021: Gautier, Pierre-Yves

    - 22 students
    - Distance learning, via TEAMS
    - Integration of nbautoeval (Exercises and Quiz)

- 2022: Pierre-Yves, Xiaojun
    - 9 studentds (7 present, 2 absent)
    - Introduce ```mamba``` for quicker env resolution
    - Added short introduction of Linux Commands 
## How to install the anaconda env required for this course?

Use ```mamba```:

1st, install ```mamba``` and ```conda-forge``` channel:
```
conda install mamba -n base -c conda-forge
```
2nd, create env from given file:
```
mamba env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml
```
## What if ChEMBL web client import error?

Simply update its version to 0.10.5 or later:

First, activate the env:
```
conda activate teachopencadd
```
Second, install newer version using pip:
```
pip install chembl_webresource_client -U
```
