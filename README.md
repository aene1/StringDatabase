# [STRING Database](https://string-db.org/) 
 ![image](https://user-images.githubusercontent.com/69886501/117343733-33937400-ae6a-11eb-9081-40a8c75bb77e.png)

By: Abdullah Mazher, Adriana Ene, and Maryann Choy

[Link to Github](https://github.com/aene1/StringDatabase)

# Project Overview:


Dr. Peter Kekenes-Huskey (PKH)'s lab focuses on computational approaches for understanding how heart and immune cells work. The lab particularly focuses on networks between proteins based on cellular pathways.The main pipeline of the STRING_pipeline_script.py code will help query the STRING database to find new edges between proteins in addition to the connections they have already discovered (seen in networkOverview.sif). The goal is to enrich their network with protein-protein interaction data from online databases. 

# Software required:

* Python3

# Dependencies:

Python request module: 

* Run the following on the command line: python3 -m pip install requests

# Input data:

* receptorList.txt: list of target receptors for which we are looking for network connections for
   * Receptors used provided by PKH Lab found [here](https://bitbucket.org/pkhlab/pathwayanalysis/src/master/receptorlist.txt) (second column of that file was ommited). 

* [networkOverview.sif](https://bitbucket.org/pkhlab/pathwayanalysis/src/master/NetworkOverView.sif): overview file of networks already discovered by PKH lab 
   * read into STRING_pipeline_script.py as dictionary
   
# Script:

* STRING_pipeline_script.py: main pipeline
   * Submits a request to the STRING API for each target receptor
   * STRING API allows various methods that we can change that will give different outputs
    * Chosen method for our script: network

# Output files:

* STRING_edge_list.txt: list of new network outputs

* STRING-PHK_edge_list.txt: list of network new network outputs in addition to PKH network connections that have been implemented in network overview

# Running the script via command line

1. git clone https://github.com/aene1/StringDatabase

2. python3 STRING_pipeline.script.py

*NOTE: Another option would be to download the files and run given your chosen Python environment
