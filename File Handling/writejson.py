import json

data={"name":"Alice","age":23}

with open("data.json",'w') as f:
    json.dump(data,f)