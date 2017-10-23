import re

phoneRegex = re.compile(r'(\d\d\d\d\d\d\d\d\d\d\d)')
mo = phoneRegex.findall('my mobile is 13410387029, 13410566741')
print(str(mo))

