
# STRING Database Pipeline #

## Design Doc ##

### Overview ###

  The Kekenes-Huskey Lab has a pipeline called “PathwayAnalysis”. Our project is to integrate another step in the already existing pipeline. The goal of this project is to build a pipeline that takes as an input a list of receptors and outputs the activators and the downstream targets found within the STRING database. 
  
### Contex ###

  This is necessary for this lab because it would significantly reduce the time that it takes to manually curate through the STRING database to find the activators of one receptor and the downstream targets for that specific receptor. The pipeline would also be able to take multiple receptors, such as a list of receptors, and output a comma separated value file which can be imputed in cytoscape to create a diagram of the connections. 
  
### Goals ##
  Create a pipeline which takes a receptor list as the input and outputs an edge list containing the activators and the downstream target of that receptor.
Pipeline should also output a second csv file with information such as the downregulation or upregulation of the proteins within the network
The pipeline should have a flag for human or mouse proteins

### Non-Goals ### 
  We met with Dr. Kekenes-Huskey and discussed that we will only change the tab delimited files to csv only to the files we are working on and not his whole pipeline. 
  
### Proposed solution ###



### Milestone ###


![](overview_flowchart.png)
