import os

def exercise_1():
    enter = input('Enter the path to the directory: ')
    my_path = os.path.abspath(enter)

    if os.path.isdir(my_path):
        print(f'Path to the catalog {my_path}')
        directory = os.listdir(my_path)
        print(directory)

        print('\nOption:')
        print('1. Create directory')
        print('2. Delete directory')
        print('3. Go to subdirectory')
        print('4. Go back to the level above')

        choice = input('Enter the options (1-4): ')

        if choice == '1':
            create_directory(my_path)
        elif choice == '2':
            delete_directory(my_path)
        elif choice == '3':
            subdirectory(my_path)
        elif choice == '4':
            level_above(my_path)
        else:
            print('The wrong choice')
    else:
        print('This directory is not find')

def create_directory(path):
    dir_name = input('Enter the name directory: ')
    dir_path = os.path.join(path, dir_name)
    try:
        os.mkdir(dir_path)
        print(f'Directory {dir_name} is create')
    except Exception as error_create:
        print(f'Error creating a directory: {error_create}')

def delete_directory(path):
    del_name = input('Enter the name directory for delete ')
    del_dir = os.path.join(path, del_name)
    try:
        os.rmdir(del_dir)
        print(f'The directory {del_dir} is deleted.')
    except Exception as delete_dir:
        print(f'Deletion error: {delete_dir}')
def subdirectory(cur_path):
    sub = input('Enter the name of the subdirectory: ')
    sub_dir = os.path.join(cur_path, sub)


    if os.path.isdir(sub_dir):
        print(f'Successfully entered the subdirectory: {sub}')
        return sub_dir
    else:
        print('This directory is not found')
        return cur_path

def level_above(current_path):
    dir_up = os.path.abspath(os.path.join(current_path, os.pardir))
    contents = os.listdir(dir_up)

    print(f'Content of the parent directory {dir_up}:')
    print(contents)

    return dir_up
exercise_1()
