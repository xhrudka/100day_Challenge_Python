with open("/Users/Operator/Documents/GIT_Personal/100day_Challenge_Python/file_folder/new_destination.txt") as file:
    contents = file.read()
    print(contents)
    
with open("/Users/Operator/Documents/GIT_Personal/100day_Challenge_Python/file_folder/new_destination.txt", mode="a") as file:
    file.write("\nSpecial new text.")
    