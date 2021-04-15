import requests

string_api_url = "https://string-db.org/api"
output_format = "tsv"
method = "network"
#method can be changed based on what we are searching for
#options: interaction_partners, network, functional_annotation, enrichment

with open('receptorList.txt','r') as f:
    s = f.read().strip()

outfile = open(method+'_output-RAW.txt', 'w') #file to write to, named based on method used above

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
# also, read the nodes into a dictionary similar to sif_dict: key=node, value=list of connections
string_dict = {}
prev_line = ''
for line in results.text.strip().split("\n"):
    if line != prev_line:
        l = line.split("\t")
        outfile.write(str(l) + '\n')
        # input_identifier, string_identifier = l[0], l[2]
        # print("Input:", input_identifier, "STRING:", string_identifier, sep="\t")
        node1 = l[2]
        node2 = l[3]
        if node1 in string_dict.keys(): #if node1 already exists as key, add node2 to corresponding list
            string_dict[node1].append(node2)
        else: #if node1 doesn't exist as key, create new entry and a list containing node2 as the value
            string_dict[node1] = [node2]
    prev_line = line
outfile.close()
string_dict.pop('preferredName_A') #remove the header from the dictionary

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

print(len(string_dict.keys()))
print(len(sif_dict.keys()))

# for key,value in string_dict.items():
#     if key not in sif_dict.items(): #check if key is in value
#         print(key)
#     # for i in value:
#     #     if i not in sif_dict.items():
#     #         print(i)


string_output_file = open('STRING_edge_list.txt','w')
results_output_file = open("STRING-PHK_edge_list.txt",'w')
string_set = set()
sif_set = set()

#create edge list in a set form for STRING database retrieval
for key in string_dict:
    # iterate through set
    for i in string_dict[key]:
        string_set.add((key, i))

#create edge list in a set form for PHK database retrieval
for key in sif_dict:
    # iterate through set
    for i in sif_dict[key]:
        sif_set.add((key, i))


#results = string database - PHK database
results = string_set-sif_set

#write out to files
for i in string_set:
    string_output_file.write(str(i[0]) + ',' + str(i[1])+ '\n')


for i in string_set:
    results_output_file.write(str(i[0]) + ',' + str(i[1])+ '\n')

