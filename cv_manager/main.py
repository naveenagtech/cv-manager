## Import All CV processing functions like process_doc, process_img etc
## Import DB manager function create_profile

def process_cv():

    # List all the files from the uploads dir and save it in all_files variable

    # Run a loop and check the file type of each file
    # based on the file type pass the file_path to the related function to process the data
    # The function will return dict data which can be passed to the create_profile function to create DB entry
    # Once processing is done move the file from upload folder to processed folder

    print("processing")