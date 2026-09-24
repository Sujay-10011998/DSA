import sys

# Print the command line arguments
print("Number of arguments:", len(sys.argv))
print("Arguments:", sys.argv)

# Access individual arguments
if len(sys.argv) > 1:
    script_name = sys.argv[0]
    first_argument = sys.argv[1]
    print("Script name:", script_name)
    print("First argument:", first_argument)
