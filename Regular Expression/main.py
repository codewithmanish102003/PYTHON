import re

#1.re.search()
str="My number is123"
ma = re.search(r"\d{3}", str)
if ma:
    print(ma.group())  # Output: 123

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.group())

# 2.re.split()
txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

# 3.match.span()
txt = "The rain in SpainS"
x = re.search(r"\bS", txt)
print(x)

# 4.match.string()
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)