import os

def list_directory_contents(directory):
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory)
        
        # Print each entry
        print(f"Contents of directory '{directory}':")
        for entry in entries:
            print(entry)
    
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access the directory '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Specify the directory path
directory_path = '/MinGW'  # '.' refers to the current directory

# List the contents of the specified directory
list_directory_contents(directory_path)