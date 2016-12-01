import os
def get_filepaths_td(directory):
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(filename)
            if filename.endswith(".csv"):
                file_paths.append(root + "\\" + filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths_td(r"C:\Users\firlyarmanda\PycharmProjects\EkstraksiBerita")
for f in full_file_paths:
     print(f)


