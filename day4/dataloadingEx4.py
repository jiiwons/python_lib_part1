import json
import pandas as pd

obj = '''
{
    "name":"Wes",
    "place_lived":["United States", "Spain", "Germany"],
    "siblings":[{"name":"scott","age":25, "pet":"zuko"},
                {"name":"kim","age":30, "pet":"kitty"}]
}
'''
data = json.loads(obj)
print(data)
print(type(obj)) # str
print(type(data)) # dict
print()
print(data['siblings'])

frame = pd.DataFrame(data['siblings'])
print(frame)