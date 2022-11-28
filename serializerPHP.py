import json
import sys

with open(sys.argv[1],"r") as f:
    format = json.loads(f.read())

clss = format["class"]
atributes = format["atributes"]

#O:4:"User":2:{s:4:"name":s:6:"carlos"; s:10:"isLoggedIn":b:1;}
output = f"O:{len(clss)}:\"{clss}\":{len(atributes)}:" + "{"

for atribute in atributes:
    #Atributes types
    output += f's:{len(atribute["name"])}:\"{atribute["name"]}\";'

    #Values Types
    if atribute["type"].lower() == "string":
        output += f's:{len(atribute["value"])}:\"{atribute["value"]}\";'
    elif atribute["type"].lower() == "integer":
        output += f'i:{atribute["value"]};'
    elif atribute["type"].lower() == "null":
        output += 'N;'
    elif atribute["type"].lower() == "boolean":
        output += f'b;{1 if atribute["value"] else 0}'

output += "}"
print(output)