# STRING Database
Project Overview:


The Kekenes-Huskey lab focuses on computational approaches for understanding how heart and immune cells work. The lab particularly focuses on networks between proteins based on cellular pathways. The main pipeline of the main_cody.py file will help query the STRING database to find new edges between proteins in addition to the connections they have already discovered (seen in networkOverview.sif). The goal is to enrich their network with protein-protein interaction data from online databases.

Software required:

-Python3

Dependencies:

Python request module: run "python3 -m pip install requests" on command line


Main Files:

-STRING_pipeline_script.py: main pipeline that pulls requests from STRING API

-networkOverview.sif: overview file of networks already discovered by PKH lab (read into main_code.py as dictionary)

-receptorList.txt: list of test receptors provided by the PKH Lab

-STRING_edge_list.txt: list of network outputs
