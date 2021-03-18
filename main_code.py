import requests

string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "interaction_partners"

with open('receptorList.txt','r') as f:
    s = f.read().strip()



params = {
    "identifiers" : "\r".join(["CCR3"]), # your protein list
    "species" : 9606, # species NCBI identifier  #homo sapiens
    "echo_query" : 1, # see your input identifiers in the output  #???
    "limit" : 100

}

##
## Construct URL
##

request_url = "/".join([string_api_url, output_format, method])

##
## Call STRING
##

results = requests.post(request_url, data=params)

##
## Read and parse the results
##


for line in results.text.strip().split("\n"):
    l = line.split("\t")
    print(len(l))
    # print(l)
    # input_identifier, string_identifier = l[0], l[2]
    # print("Input:", input_identifier, "STRING:", string_identifier, sep="\t")

