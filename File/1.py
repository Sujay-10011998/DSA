import os

# Syntax: os.environ.get('variable_name', 'default_value')
# If the environment variable 'variable_name' is present, its value is returned.
# If 'variable_name' is not present, the method returns the specified 'default_value' (which is optional).

# Example:
value = os.environ.get('var')

# In this example, if the environment variable 'MY_VARIABLE' is set, 'value' will be its value.
# If 'MY_VARIABLE' is not set, 'value' will be 'default_value'.
print(value)






import os

# Example usage
path1 = "folder1"
path2 = "folder2"
filename = "file.txt"

full_path = os.path.join(path1, path2, filename)

print(full_path)



