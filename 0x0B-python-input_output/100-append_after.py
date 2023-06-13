def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Move the file pointer to the beginning

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()  # Remove any remaining content after writing the modified lines
