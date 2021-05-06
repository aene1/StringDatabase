# STRING Database 
 ![image](https://user-images.githubusercontent.com/69886501/117343733-33937400-ae6a-11eb-9081-40a8c75bb77e.png)

By: Abdullah Mazher, Adriana Ene, and Maryann Choy

# Overview:


The Kekenes-Huskey lab focuses on computational approaches for understanding how heart and immune cells work. The lab particularly focuses on networks between proteins based on cellular pathways. The main pipeline of the STRING_pipeline_script.py file will help query the STRING database to find new edges between proteins in addition to the connections they have already discovered (seen in networkOverview.sif). The goal is to enrich their network with protein-protein interaction data from online databases.

# Software required:

-Python3

Dependencies:

Python request module: run "python3 -m pip install requests" on command line


# Script:

-STRING_pipeline_script.py: main pipeline that pulls requests from STRING API

# Input data:

-networkOverview.sif: overview file of networks already discovered by PKH lab (read into main_code.py as dictionary)

-receptorList.txt: list of test receptors provided by the PKH Lab

# Output files:

-STRING_edge_list.txt: list of new network outputs

-STRING-PHK_edge_list.txt: list of network new network outputs in addition to PKH network connections that have been implemented in network overview

# How to run at command line:

1. git clone https://github.com/aene1/StringDatabase

2. python3 STRING_pipeline.script.py
