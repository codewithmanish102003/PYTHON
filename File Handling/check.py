# Overwriting existing content
f=open("example.txt", "a")
f.write("Hello, World!\n")
f.write("Welcome to file handling in Python.")

# Appending content
with open("example.txt", "a") as f:
    f.write("\nThis is an additional line.")
