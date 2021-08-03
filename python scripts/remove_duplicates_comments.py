# Abhishek Choudhary 15.04.2021

from os import getcwd, makedirs, unlink, listdir
from os.path import join, exists, isfile, islink, isdir
import shutil


def remove_duplicate_files(path: str, copy_path: str):
    if not exists(copy_path):
        makedirs(copy_path)
    else:
        clear_folder(copy_path)
    filenames = listdir(path)
    filenames.sort(reverse=False)
    for filename in filenames:
        if isfile(join(path, filename)):
            list_of_copied_files = list(
                map(lambda x: '-'.join(x.split('-')[1:]), listdir(copy_path)))
            if ('-'.join(filename.split('-')[1:]) not in list_of_copied_files):
                shutil.copy(join(path, filename), copy_path)


def clear_folder(path: str):
    for filename in listdir(path):
        file_path = join(path, filename)
        try:
            if isfile(file_path) or islink(file_path):
                unlink(file_path)
            elif isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def remove_comments_from_atl_files(path: str, copy_path: str):
    if not exists(copy_path):
        makedirs(copy_path)
    else:
        clear_folder(copy_path)
    for filename in listdir(path):
        file = open(join(path, filename), mode='r', encoding="ISO-8859-1")
        file_content = file.readlines()
        copy_file = open(join(copy_path, filename),
                         mode='w', encoding="ISO-8859-1")
        for line in file_content:
            if (line.startswith('--')):
                pass
            elif (line.find('--') != -1):
                line = line[:line.index('--')]
                copy_file.write(line + '\n')
            else:
                copy_file.write(line + '\n')
        copy_file.close()
        file.close()


def main():
    """
    Directory path from which the files need to be cleaned
    """
    path = join(getcwd(), 'ATL')

    """
    Directory path to which the non-duplicate files need to be copied
    """
    copy_sorted_path = join(getcwd(), 'ATL_Sorted')

    """
    Directory path to which the comment wise cleaned files to be copied
    """
    copy_removed_comment_path = join(getcwd(), 'ATL_Comment_Removed')

    """
    removing duplicate files
    """
    remove_duplicate_files(path=path, copy_path=copy_sorted_path)

    """
    removing comment from files
    """
    remove_comments_from_atl_files(
        path=copy_sorted_path, copy_path=copy_removed_comment_path)


if __name__ == "__main__":
    main()
