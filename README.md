# GSON module "chimie informatique sous python"

## TL;DR

Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD?urlpath=/tree/) to start your lesson.

## Acknowledgement

This course is mostly based on [teachopencadd](https://github.com/volkamerlab/teachopencadd).  
**Huge thanks to them for providing such good learning material!**

## Launch notebooks directly in your browser

- If you prefer the modern `jupyter lab` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD)
  - be careful that for the exos using `nbautoeval`, the cell output may return error
  - for the moment it is **NOT recommended to use above method**

- If you prefer the traditional `jupyter notebook` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD?urlpath=/tree/)

The materials are exactly the same. The only difference is the appearance.  
The 1st launch can take around 10 minutes, and it will be faster from 2nd time.  
It **does not require any setup/installation on your machine** (which is quite easy to use). You just need an Internet connection and a browser.

**Remarks:**  

1. To save resources, your connection to the `Binder` server will be **automatically cut off** if you have no activity (cell edit/cell execution) for around 10 mins

2. Your changes to the notebooks will **NOT be saved**. So if you close the browser and re-open `Binder`, you lose all what you have done previously...

### Note for session 2024-2025

- since an update of `Binder` server in 2025.01, the interface is fixed to the newer one, which is not compatible with the `nbautoeval`
  - it can still be used, except **we do not have the interactive evaluation of exercises and quiz**

## Organisation of session 2024-2025

### Lundi 13 janvier 2025 13h30-17h30

- Introduction
  - Slides 1_GSON_intro (80 min)
  - Slides 2_introduction_informatique (40 min)
  - Talktorial Introductif 1 Intro Python, jupyter (1h10)
  - Talktorial Introductif 2 Intro chemoinfo - RDKit (20 min)

### Mardi 14 janvier 2025 13h30-17h30

- Talktorial Introductif 2 Intro chemoinfo - RDKit (1h30)

- Data Acquisition (1h20)
  - Talktorial 1 Data acquisition from ChEMBL

### Mercredi 15 janvier 2025 13h30-17h30

- Filtering (1h45-2h)
  - Descriptors and ADME (1h20)
    - Slides 4_Descripteurs_fingerprints
    - Talktorial 2 Molecular filtering: ADME/Lipinski criteria

- Filtering (30 min)
  - Talktorial 3 Substructure removal : PAINS

- Ligand based Screening (1h)
  - Slides 5_fingerprint_similarity (20 min)
  - Talktorial 4 Fingerprints and Molecular Similarity (40 min)

### Jeudi 16 janvier 2025 13h30-17h30

- Live demo: Python, jupyter notebook, `pandas` (3h30)
- Ligand based Screening (15 min)

### Vendredi 17 janvier 2025 13h30-17h30

- Machine Learning (1h50)
  - Slides 6_Machine Learning (1h)
  - Talktorial 7 Machine Learning (45 min)

- Applications in chemoinformatics + review (55 min)
  - Slides 7_Applications

- Exam (60 min)

## Installation on local machine (Chromebook)

- from the feedback of the students, it seems impossible
- however, I DO found some trick which seems to allow it, for example:
  - https://gist.github.com/TomatOid/335f53d72cc3a93022e827d9f650aaa4
  - I have never tested, since I personnally do not have a Chromebook
  - but it requires quite high level IT technique, which students may not have

## Installation on local machine (Windows)

Follow the instructions step by step given by your professor during the course!

## Installation on local machine (Linux and MacOS)

Suppose that you are using **Linux** (**MacOS** should work the same way, since it is also **Unix**):

1. Install `miniconda` (or `anaconda` if you prefer)

- For installation details, please refer to their [official documentation](https://docs.conda.io/en/latest/miniconda.html).

2. Open a terminal, you should normally see `(base)` before your prompt. (See below FAQ part if you cannot see `(base)`)  
Create the virtual environment for this course from given file:  

```bash
conda env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml
```

- This file contains a list of `conda`/`pip` packages that are required for this course.  
- You are encouraged to check the content of this file, to make sure it does not contain malicious software.

3. Open a terminal, and clone the repo to your local PC:

```bash
git clone https://github.com/ICOA-SBC/GSON-cheminformatics
```

4. Activate the virtual environment:

```bash
conda activate teachopencadd
```

- You should observe that the `(base)` has become `(teachopencadd)`, meaning that you are now in this new virtual environment.

5. You are ready to go. Simply launch the `notebook` interface with command:

```bash
jupyter notebook
```

## Special instructions for promo 2023-2024

If you are using `Windows` on your own PC, before each course, please execute the command `git pull` in your terminal, to get the latest version of material.

If you are using the `Linux` session on the PCs of "salle info", here are the commands to follow, from Tuesday to Friday:

1. Open a terminal, copy-paste below command into it, and execute it:

```bash
/opt/anaconda3/bin/conda init
```

2. Normally, the message of the terminal will suggest you to close and re-open the terminal after above command is executed successfully.  
Simply close and re-open another terminal.  
You should now see `(base)` on the leftmost of your prompt. (ask the teachers if you still cannot see it)  

3. Create the virtual environment for this course from given file, by copy-paste below command into your terminal, and execute it:

```bash
conda env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml
```

- This file contains a list of `conda`/`pip` packages that are required for this course.  
- You are encouraged to check the content of this file, to make sure it does not contain malicious software.
- This command will take 3-10 mins, depending on the configuration of your PC, and the Internet connection

4. Once above command finishes with success, you can now clone the repo to your local PC, by copy-paste below command into your terminal, and execute it:

```bash
git clone https://github.com/ICOA-SBC/GSON-cheminformatics
```

5. Activate the virtual environment:

```bash
conda activate teachopencadd
```

- You should observe that the `(base)` has become `(teachopencadd)`, meaning that you are now in this new virtual environment.

6. You are ready to go. Simply launch the `notebook` interface with command:

```bash
jupyter notebook
```

## History of previous years

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
  - 17 students (16 inscriptions + 1 volunteer participant)
  - Cleaned not used packages/channels in `environment.yml` for quicker env resolution
  - Added `Slide 7_Applications`, to showcase other fields of applications not covered in the course

- 2025: Xiaojun
  - 12 students (11 present, 1 absent)
  - local installation of `Anaconda` on students' PC (due to problems of "salle info" and `Binder`)
  - live demo of 3h30 on Python, jupyter notebook and `pandas` added

- 2026: ?

## FAQ

### What if you cannot find `conda` by typing `which conda`, or you do not see `base` before your prompt?

Experience 2024:  
In the computer rooms of COST, `conda` is installed at `/opt/anaconda3`, not under each user's `/home`.  
Furthermore, it is NOT added to the `$PATH`, making it unfindable by `which conda` command.  
Even more, the `/home` of each student will be automatically deleted on the 2nd day of the course, after restarting the PC...(by default the PCs are automatically shut down during the night).  

So it means the students have to repeat the steps of

- initiate `conda`
- create `conda` virtual environment
- clone the course material

from Tuesday to Friday, before each course starts (which is annoying!)  

### Work in progress, reserved for teachers

1. Open a terminal, and type `echo $PATH` to check the existing PATHS (normally you shoud not be able to find `/opt/anaconda3`).
2. Type `gedit ~/.bashrc`. A text editor interface will automatically appear.
3. Add `export PATH=/opt/anaconda3/bin:$PATH` to the end of the file, then save and close the file.
4. Reload the profile with `source ~/.bashrc`
5. Type the command `which conda`, you should be able to find it at `opt/anaconda3/`.
6. Type the command `conda init bash` to initiate it.
7. Reload the profile with `source ~/.bashrc`.  
After all these steps, you should now see `(base)` before your prompt.

### Another solution provided by service info (which seems easier, thus recommended)

1. Open a terminal, and change to the directory where `conda` is installed: `cd /opt/anaconda3/bin`
2. Initiate it by `./conda init`
3. Close the terminal, and re-open a new one
4. You should now see `(base)` before your prompt

### A more automatic way (WIP, since it requires restarting the terminal, it does not work for the moment)

An `init.sh` script is also included in the repo. It automates all the 3 major steps:

- export conda to `$PATH`
- create environment
- clone the repo

To use it under Linux:

- Download this file, and put it at your `/home`
- Open a terminal, and execute the downloaded script by `bash init.sh`
- This process will take ~3 mins (the resolution of environment may take extra time)
- If the script success, you will need to close and open another terminal

Voilà! You are ready to go!
