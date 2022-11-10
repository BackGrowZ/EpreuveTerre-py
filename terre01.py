# Afficher le nom du fichier

file_path = __file__
file_split = file_path.split("/")
file_name =file_split[(len(file_split) - 1)]

print(file_name)