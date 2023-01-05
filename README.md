This course is mostly based on [teachopencadd](https://github.com/volkamerlab/teachopencadd).

Launch notebooks with Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD?urlpath=/tree/)

GSON Chimie-informatique
========================
___Organisation of "GSON chimie informatique sous python" lessons, year 2023:___

**Lundi 9 janvier 2023 13h30-17h30**

- Introduction

  - Slides 1_GSON_intro (30 min) PYL
  - Slides 2_introduction_informatique (30 min) XM
  - Talktorial Introductif 1 Intro Python, jupyter (40 min) XM
  - Talktorial Introductif 2 Intro chemoinfo - RDKit (1h20) XM

**Mardi 10 janvier 2023 08h30-12h30**

- Data Acquisition (2h-2h30) XM

  - Talktorial 1 Data acquisition from ChEMBL

- Filtering (1h45-2h) PYL

  - Descriptors and ADME (1h30)

    - Slides 4_Descripteurs_fingerprints
    - Talktorial 2 Molecular filtering: ADME/Lipinski criteria

**Mercredi 11 janvier 2023 13h30-17h30**

- ACP (2h) PYL
  - Slides 3_Intro_ACP
  - Notebook ACP

- Filtering (1h) PYL

  - Talktorial 3 Substructure removal : PAINS

- Ligand based Screening (2h45) XM

  - Slides 5_fingerprint_similarity (45 mins)

**Jeudi 12 janvier 2023 13h30-17h30**

- Ligand based Screening (2h45) XM

  - Talktorial 4 Fingerprints and Molecular Similarity (2h)

- Clustering (1h45) XM

  - Talktorial 5 : Compound clustering (1h15)
  - Talktorial 6 : MCS (30 min)

**Vendredi 13 janvier 2023 08h30-12h30**

- Machine Learning (1h45) PYL

  - Slides 6_Machine Learning
  - Talktorial 7 Machine Learning (ROC curve) PYL

- Exam (30 min) + correction explication (30 min)

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
    - 9 students (7 present, 2 absent)
    - Introduce ```mamba``` for quicker env resolution
    - Added short introduction of Linux Commands

- 2023: Pierre-Yves, Xiaojun
    - Created a pre-course questionnaire to better adapt the course to future students attending the course

## Installation

Suppose that you are using Linux:

1. Install `miniconda`

For installation details, please refer to their [official documentation](https://docs.conda.io/en/latest/miniconda.html).

2. Install `mamba` in the `base` environment of `conda`, and set `conda-forge` channel as priority:
```
conda install mamba -n base -c conda-forge
```

3. Create the virtual environment for this course from given file:
```
mamba env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml
```

4. Clone the repo to your local PC:
```
git clone git@github.com:ICOA-SBC/GSON-cheminformatics.git
```

5. Activate the virtual environment:

```
conda activate teachopencadd
```

Voilà! You are ready to go.

## What if `404 error` when launching `Binder`?
`Binder` changed the default user interface from traditional `jupyter notebook` to `jupyter lab` in Feb, 2022.

The quickest solution is to [change the ending of the Binder launcher address from `lab` to `tree`](https://discourse.jupyter.org/t/previous-built-binder-repo-suddenly-with-404-error/13047). After that, the traditional interface will come back.