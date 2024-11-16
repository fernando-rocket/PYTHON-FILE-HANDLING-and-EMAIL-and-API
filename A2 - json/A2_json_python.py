import json

input_data ={
        "fefe": {
            "idade": 16,
            "earnigs_no_fortnite": 1200
        }
    }


with open("A2 - json/A2_data_file.json", "r") as file:
    x = json.load(file)
    x.update(input_data)
with open("A2 - json/A2_data_file.json", "w") as file:
    json.dump(x,file,indent=4)

