#!/usr/bin/env bash
# ==================================================================== #
# Written by: Manu M. on 2023                                          #
# Purpose: Generate a basic template for data science projects         #
# Instructions: Execute using >source initialize.sh                    #
# ==================================================================== #
currentPath=$(pwd)
activatePath="/.venv/bin/activate"
echo "************** Initialize project template **************"
python -m venv .venv
source ${currentPath}${activatePath}
python -m pip install ipykernel nbformat pytest black[jupyter] requests
python -m pip install python-dotenv pandas seaborn requests graphrag 
python -m pip install --upgrade pip
python -m pip freeze > requirements.txt
echo -e ".venv\n.env\n__pycache__" > .gitignore
echo "# README" > README.md
mkdir -p data/{raw,baking,final}
mkdir notebooks src app img docs
echo "******************* Template finished *******************"