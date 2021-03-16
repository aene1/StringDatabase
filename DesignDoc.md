
# STRING Database Pipeline #

## Design Doc ##

### Overview ###

  Dr. Peter Kekenes-Huskey’s (PKH) Lab focuses on cell and molecular biophysics, which includes focusing on signaling molecules and pathways between proteins. The PKH Lab has a pipeline called “PathwayAnalysis”, which takes in a list of nodes and provides information on other connections that that node may have. The purpose of our STRING database project is to integrate another step in the already existing pipeline in order to allow additional analyses to be made in linking the receptors to gene up/down regulation. The goal of this project is to build a pipeline that takes as an input a list of receptors and outputs the activators and the downstream targets found within the STRING database. The biological goal of this project is to curate a signal transduction pathway network describing a transmembrane receptor (TM) dependent on activation of gene regulation. Our code should help the already active mechanism to find the “shortest path” analysis to link transmembrane receptors and to find a downstream target that is not another receptor.
  
  The STRING database contains information regarding known and predicted protein-protein interactions, including direct physical associations and indirect functional interactions. It has data for about 24.5 million proteins from over 5,000 organisms. These interaction data come from a variety of sources including genomic context predictions, high-throughput lab experiments, co-expression experiments, automated text mining of sources like PubMed, and previous knowledge in other databases. As expected from the nature of its data, this database is most often used to discern interactions between proteins of interest in an experiment and gather insight to the intersection of various biochemical pathways.
  
### Context ###

  This is necessary for this lab because it would significantly reduce the time that it takes to manually curate through the STRING database to find the activators of one receptor and the downstream targets for that specific receptor. The pipeline would also be able to take multiple receptors, such as a list of receptors, and output a comma separated value file which can be imputed in cytoscape to create a diagram of the connections. 
  
### Goals ##
  Create a pipeline which takes a receptor list as the input and outputs an edge list containing the activators and the downstream target of that receptor.
Pipeline should also output a second csv file with information such as the downregulation or upregulation of the proteins within the network
The pipeline should have a flag for human or mouse proteins

### Non-Goals ### 
  We met with Dr. Kekenes-Huskey and discussed that we will only change the tab delimited files to csv only to the files we are working on and not his whole pipeline. 
  
### Proposed solution ###
 
 STRING API : https://string-db.org/help/api/ 

<img src="https://github.com/aene1/StringDatabase/blob/main/overview_flowchart.png" width="614" height="2232">

### Milestone ###

|                    |                                                                            |                                                                            |                                                                            |
|--------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                    | Adriana                                                                    | Maryann                                                                    | Abdullah                                                                   |
| March 14 (Week 9)  | Complete design doc                                                        | Complete design doc                                                        | Help with design doc                                                       |
|                    | Meet with Dr. Kekenes-Huskey to retrieve sample data                       | Meet with Dr. Kekenes-Huskey to retrieve sample data                       | Meet with Dr. Kekenes-Huskey to retrieve sample data                       |
| March 21 (Week 10) | Using receptor list create list in python and parse it into the STRING API | Using receptor list create list in python and parse it into the STRING API | Test code                                                                  |
| March 28 (Week 11) | Use the .SIF files to get information about the nodes                      | Test code                                                                  | Using the receptor nodes find the antagonists                              |
| April 4 (Week 12)  | Parse the output from String                                               | Using the antagonists found make sure they are not repetitive              | Test code                                                                  |
| April 11 (Week 13) | Test code                                                                  | Using the receptor nodes find the antagonists                              | Using receptor list create list in python and parse it into the STRING API |
| April 18 (Week 14) | Debug                                                                      | Test code                                                                  | Debug                                                                      |
| April 25 (Week 15) | Test code                                                                  | Create final presentation                                                  | Create final presentation                                                  |
|                    |

