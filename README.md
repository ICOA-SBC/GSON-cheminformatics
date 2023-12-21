GSON "chimie informatique sour python"
========================================

This course is mostly based on [teachopencadd](https://github.com/volkamerlab/teachopencadd).  
Huge thanks to them for providing such good learning material.

Launch notebooks directly in your browser:  

- If you prefer the `jupyter lab` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD)

- Or if you prefer the traditional `jupyter notebook` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD?urlpath=/tree/)

The materials are exactly the same. The only difference is the appearance.  
Both can take around 10 minutes, but does not require any kind of setup on your machine.

## Organisation of year 2023-2024

**Lundi 15 janvier 2024 13h30-17h30**

- Introduction
  - Slides 1_GSON_intro (30 min) PYL
  - Slides 2_introduction_informatique (30 min) XM
  - Talktorial Introductif 1 Intro Python, jupyter (40 min) XM
  - Talktorial Introductif 2 Intro chemoinfo - RDKit (1h20) XM

**Mardi 16 janvier 2024 13h30-17h30**

- Data Acquisition (2h-2h30) XM
  - Talktorial 1 Data acquisition from ChEMBL

- Filtering (1h45-2h) PYL
  - Descriptors and ADME (1h30)
    - Slides 4_Descripteurs_fingerprints
    - Talktorial 2 Molecular filtering: ADME/Lipinski criteria

**Mercredi 17 janvier 2024 13h30-17h30**

- ACP (2h) PYL
  - Slides 3_Intro_ACP
  - Notebook ACP

- Filtering (1h) PYL
  - Talktorial 3 Substructure removal : PAINS

- Ligand based Screening (2h45) XM
  - Slides 5_fingerprint_similarity (45 mins)

**Jeudi 18 janvier 2024 13h30-17h30**

- Ligand based Screening (2h45) XM
  - Talktorial 4 Fingerprints and Molecular Similarity (2h)

- Clustering (1h45) XM
  - Talktorial 5 : Compound clustering (1h15)
  - Talktorial 6 : MCS (30 min)

**Vendredi 19 janvier 2024 13h30-17h30**

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
    - 5 students (4 present, 1 absent)
    - Created a pre-course questionnaire to better adapt the course to future students attending the course

- 2024: Xiaojun, Jérémy
    - 16 students
    - Cleaned not used packages/channels in `environment.yml` for quicker env resolution

## Installation

Suppose that you are using Linux:

1. Install `miniconda`

For installation details, please refer to their [official documentation](https://docs.conda.io/en/latest/miniconda.html).

2. Create the virtual environment for this course from given file:
```
conda env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml
```

3. Open a terminal, and clone the repo to your local PC:
```
git clone https://github.com/ICOA-SBC/GSON-cheminformatics
```

4. Activate the virtual environment:

```
conda activate teachopencadd
```

5. You are ready to go. Simply launch the `notebook` interface with command:
```
jupyter notebook
```

## To roll-back to the original version, and update info in local repo
1. In a terminal, `cd` to the folder where you cloned the repo, and run
```
git status
```
Normally you will see some files that are created/modified during the last cours.

2. Since we want to **all start from the same place**, we can run below command to **discard all the changes that have been made since cloning**:
```
git restore *
```
This will restore everything back to the state just after cloning.

3. Update your local repo by pulling from GitHub:
```
git pull
```
You will have the most recent version of notebooks on your local PC.  