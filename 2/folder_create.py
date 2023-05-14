import os
day = "Day"
file_path = ("") #Path of the directory which you wanted to create folder with file name
# Eg : file_path = ("C:/Users/Admin/OneDrive/Desktop/My_Folder")

# Make multiple folder inside before created folder
for i in range(1,100): # range for which you wanted ot create the folder
    # Make folder like below
    os.mkdir("C:/Users/Admin/OneDrive/Desktop/My_Folder" + f"\\{i}")