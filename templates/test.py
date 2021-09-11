import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)
