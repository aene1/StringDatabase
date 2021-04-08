# STRING Database
The Kekenes-Huskey lab focuses on computational approaches for understanding how heart and immune cells work. The lab particularly focuses on networks between proteins based on cellular pathways. The main pipeline of the main_cody.py file will help query the STRING database to find new edges between proteins in addition to the connections they have already discovered (seen in networkOverview.sif). The goal is to enrich their network with protein-protein interaction data from online databases.


Dependencies (run on command line): 

python3 -m pip install requests


Files:

-main_code.py: main pipeline that pulls requests from STRING API

-networkOverview.sif: overview file of networks already discovered by PKH lab (read into main_code.py as dictionary)

-receptorList.txt: list of test receptors provided by the PKH Lab 
