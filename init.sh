#!/bin/bash

# Part 1: export conda to PATH, and initiate it
# ---------------------------------------------------------
# Add Conda to PATH permanently for bash shells
echo "Adding Conda to PATH in .bashrc..."
echo 'export PATH=/opt/anaconda3/bin:$PATH' >> ~/.bashrc # use single quote to the literal string, not expanded $PATH 

# Reload .bashrc
source ~/.bashrc

# Check Conda Version
echo "Checking Conda version..."
conda --version

# Initiate conda
echo "Initiating Conda..."
conda init bash

# Reload .bashrc
source ~/.bashrc

echo "Conda setup completed"

# Part 2: Create conda environment for the course
# ---------------------------------------------------------
echo "Creating conda environment for the course..."
conda env create -f https://raw.githubusercontent.com/ICOA-SBC/GSON-cheminformatics/master/environment.yml

# Part 3: Clone the repo
# ---------------------------------------------------------
echo "Cloning the repo..."
git clone https://github.com/ICOA-SBC/GSON-cheminformatics
conda activate teachopencadd