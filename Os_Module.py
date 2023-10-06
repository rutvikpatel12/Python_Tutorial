import os
# --- check folder is create for this code is not executed
# if(not os.path.exists("Data")):
#     os.mkdir("Data")

# --- Create multiple folder using single loop
# for i in range(0,5):
#     os.mkdir(f"data/Day{i+1}")

# --- Rename folder name
# for i in range(0,5):
#     os.rename(f"data/Tutorial_{i+1}", f"data/Tutorial {i+1}")


# # --- Show all folder name
# folders = os.listdir("data")
# print(folders)

# # Print using for loop
# for folder in folders:
#     # print folder
#     print(folder)
#     # print all file under the folder
#     print(os.listdir(f"data/{folder}"))

cwd = os.getcwd()
print(cwd)

# --- Change directory
# os.chdir("/Data")
# print(os.getcwd())

# Delete File
os.remove("requirements.txt")

