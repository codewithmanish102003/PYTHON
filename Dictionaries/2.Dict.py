person={"name":"Huxn","age":22}
employee={"occ":"developer","company":"google"}

person.update(employee)

sorted_dict=dict(sorted(person.items(),reverse=True))

print(person)
print(sorted_dict)
print(person.keys())
print(person.items())
print(person.values())
print(person.pop("name"))
print(person.popitem())