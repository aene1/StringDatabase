import requests

string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "get_string_ids"

params = {

    "identifiers" : "\r".join(["p53", "BRCA1", "cdk2", "Q99835"]), # your protein list
    "species" : 9606, # species NCBI identifier
    "limit" : 1, # only one (best) identifier per input protein
    "echo_query" : 1, # see your input identifiers in the output
    "caller_identity" : "www.awesome_app.org" # your app name

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
    input_identifier, string_identifier = l[0], l[2]
    print("Input:", input_identifier, "STRING:", string_identifier, sep="\t")