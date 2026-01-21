# Step 1: Create and write to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This file is created using Python.\n")

print("Data written to file successfully.")

# Step 2: Read the file
print("\nReading file content:")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Step 3: Append data to the file
with open("example.txt", "a") as file:
    file.write("This line is appended later.\n")

print("\nData appended successfully.")

# Step 4: Read again after appending
print("\nUpdated file content:")
with open("example.txt", "r") as file:
    print(file.read())
