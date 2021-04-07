import requests

string_api_url = "https://string-db.org/api"
output_format = "tsv"
method = "interaction_partners"
#method can be changed based on what we are searching for
#options: interaction_partners, network, functional_annotation, enrichment

with open('receptorList.txt','r') as f:
    s = f.read().strip()

outfile = open(method+'_output.txt', 'w') #file to write to, named based on method used above

params = {
    "identifiers" : "\r".join(["s"]), # your protein list
    "species" : 9606, # species NCBI identifier  #homo sapiens
    "echo_query" : 1, # see your input identifiers in the output  #???
    "limit" : 100
}

# Construct URL for STRINGdb
request_url = "/".join([string_api_url, output_format, method])

# Call STRING
results = requests.post(request_url, data=params)

# Read and parse the results (write to outfile)
for line in results.text.strip().split("\n"):
    l = line.split("\t")
    outfile.write(str(l) + '\n')
    #print(len(l))
    # print(l)
    # input_identifier, string_identifier = l[0], l[2]
    # print("Input:", input_identifier, "STRING:", string_identifier, sep="\t")
outfile.close()

# read in networkOverview.sif as a dictionary
## key=node1, value=list of connections to node1
sif_file = open('networkOverview.sif', 'r')
sif_dict = {}
for line in sif_file: #for each line in file, extract the nodes
    line_list = line.strip().split('\t')
    node1 = line_list[0]
    node2 = line_list[2]
    if node1 in sif_dict.keys(): #if node1 already exists as key, add node2 to corresponding list
        sif_dict[node1].append(node2)
    else: #if node1 doesn't exist as key, create new entry and a list containing node2 as the value
        sif_dict[node1] = [node2]

