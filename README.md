GSON "chimie informatique sous python"

This course is mostly based on [teachopencadd](https://github.com/volkamerlab/teachopencadd).  
Huge thanks to them for providing such good learning material.

**Launch notebooks directly in your browser:**  

- If you prefer the `jupyter lab` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD)

- Or if you prefer the traditional `jupyter notebook` interface: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ICOA-SBC/GSON-cheminformatics/HEAD?urlpath=/tree/)

The materials are exactly the same. The only difference is the appearance.  
Both can take around 10 minutes, but does not require any kind of setup on your machine.

**Remarks:**  

1. To save resources, your connection to the `Binder` server will be **automatically cut off** if you have no activity for around 10 mins

2. Your changes to the notebooks will **NOT be saved**. So if you reconnect, you lose all what you have done previously...

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

## Organisation of year 2023-2024

**Lundi 15 janvier 2024 13h30-17h30**

- Introduction
  - Slides 1_GSON_intro (30 min) XM & JM
  - Slides 2_introduction_informatique (30 min) XM
  - Talktorial Introductif 1 Intro Python, jupyter (40 min) XM
  - Talktorial Introductif 2 Intro chemoinfo - RDKit (1h20) JM

**Mardi 16 janvier 2024 13h30-17h30**

- Data Acquisition (2h-2h30) XM
  - Talktorial 1 Data acquisition from ChEMBL

- Filtering (1h45-2h) JM
  - Descriptors and ADME (1h30)
    - Slides 4_Descripteurs_fingerprints
    - Talktorial 2 Molecular filtering: ADME/Lipinski criteria

**Mercredi 17 janvier 2024 13h30-17h30**

- ACP (2h) JM
  - Slides 3_Intro_ACP
  - Notebook ACP

- Filtering (1h) XM
  - Talktorial 3 Substructure removal : PAINS

- Ligand based Screening (2h45) XM
  - Slides 5_fingerprint_similarity (45 mins)

**Jeudi 18 janvier 2024 13h30-17h30**

- Ligand based Screening (2h45) JM
  - Talktorial 4 Fingerprints and Molecular Similarity (2h)

- Clustering (1h45) XM
  - Talktorial 5 : Compound clustering (1h15)
  - Talktorial 6 : MCS (30 min)

**Vendredi 19 janvier 2024 13h30-17h30**

- Machine Learning (1h45) JM
  - Slides 6_Machine Learning
  - Talktorial 7 Machine Learning (ROC curve) JM

- Applications in chemoinformatic  (30 min) XM & JM
  - Slides 7_Applications

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
    - 17 students
    - Cleaned not used packages/channels in `environment.yml` for quicker env resolution
    - Added `Slide 7_Applications`, to showcase other fields of applications not covered in the course

## Installation

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

**Note for teachers:**  
Perhaps switch to Windows from next year?


### Work in progress, reserved for teachers

1. Open a terminal, and type `echo $PATH` to check the existing PATHS (normally you shoud not be able to find `/opt/anaconda3`).
2. Type `gedit ~/.bashrc`. A text editor interface will automatically appear.
3. Add `export PATH=/opt/anaconda3/bin:$PATH` to the end of the file, then save and close the file.
4. Reload the profile with `source ~/.bashrc`
5. Type the command `which conda`, you should be able to find it at `opt/anaconda3/`. 
6. Type the command `conda init bash` to initiate it. 
7. Reload the profile with `source ~/.bashrc`.  
After all these steps, you should now see `(base)` before your prompt.

### Another solution provided by service info (which seems easier, thus recommended):

1. Open a terminal, and change to the directory where `conda` is installed: `cd /opt/anaconda3/bin`
2. Initiate it by `./conda init`
3. Close the terminal, and re-open a new one
4. You should now see `(base)` before your prompt

### A more automatic way (WIP, since it requires restarting the terminal, it does not work for the moment):

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

## In case needed
### To roll-back to the original version, and update info in local repo

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