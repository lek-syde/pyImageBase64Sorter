import os
import base64
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def generateSQL(name):
    # Use a breakpoint in the code line below to debug your script.


    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Function to encode image to base64 string
def image_to_base64(image_folder):
    # Check if the directory is empty
    if not os.listdir(image_folder):
        print("Directory is empty. No images found.")
        return []

    base64_images = []
    # Iterate through files in the folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(image_folder, filename)
            if os.path.isfile(image_path):
                with open(image_path, "rb") as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
                # Remove file extension from the filename
                filename_without_extension = os.path.splitext(filename)[0]
                base64_images.append((filename_without_extension, encoded_string))
            else:
                print(f"Error: File '{filename}' not found or is not a regular file.")
    return base64_images

# Function to generate SQL update statement
def generate_sql_statement(filename, base64_string):
    return f"UPDATE employee SET photo='{base64_string}' WHERE pf_num='{filename}';\n"

# Folder containing images
image_folder = "images"

# Output SQL file
sql_file = "output.sql"

# Get base64 encoded images
base64_images = image_to_base64(image_folder)

# Open SQL file in append mode
with open(sql_file, "a") as f:
    # Write SQL statements for each image
    for filename, base64_string in base64_images:
        # Generate SQL statement
        sql_statement = generate_sql_statement(filename, base64_string)
        # Write SQL statement to file
        f.write(sql_statement)

print("SQL statements have been written to", sql_file)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_to_base64(image_folder)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
