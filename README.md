# module_find_position_image
- This module is written from [Imagededup](https://github.com/idealo/imagededup) and makes it easier to find exactly position of an image in a folder 
- We use this module and Imagededup to find an image from a folder
- We need to save that image in folder to find duplicated imaged

# Installation
- Firstly, we need to install Imagededup:
  
    ```
    pip install imagededup
    ```
    
- Next, we need to install this module:
    ```
    git clone https://github.com/luongdangvp2000/module_find_position_image.git
    ```
    
# Get started:
- Before we fine duplicated image, we have to import module, declare path of image directory and file name:
    ```
    from module_find_position_image import encodings_and_duplicates_images_dir, image_dir, name_image
    
    image_dir = image_dir(path of image directory)
    filename = name_image(name of image)
    ```
- Next step, we generate encodings for all images:
    ```
    duplicates= encodings_and_duplicates_images_dir(image_dir= image_dir)
    ```
- After that, we can find the most similar image and its position:
    ```
    from module_find_position_image import find_position_duplicated_image
    from module_find_position_image import find_name_duplicated_image
    
    duplicated_filename= find_name_duplicated_image(duplicates= duplicates, filename= filename)
    print(duplicated_filename)
    print(find_position_duplicated_image(duplicates= duplicates, filename=filename))
    ```
- We can also display two image to compare:
    ```
    from module_find_position_image import display_images_to_compare

    display_images_to_compare(filename= filename, duplicated_filename= duplicated_filename, image_dir= image_dir)
    ```
