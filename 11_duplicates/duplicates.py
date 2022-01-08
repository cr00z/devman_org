import os
from collections import defaultdict


def get_file_locations(start_path):
    file_locations = defaultdict(list)
    for directory, _, file_names in os.walk(start_path):
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                file_locations_key = (file_name, file_size)
                file_locations[file_locations_key].append(file_path)
    return file_locations


def find_duplicates(start_path):
    file_locations = get_file_locations(start_path)
    file_duplicates = dict()
    for file_info, file_paths in dict(file_locations).items():
        if len(file_paths) > 1:
            file_duplicates[file_info] = file_paths
    return file_duplicates


def print_duplicates(file_duplicates):
    for (file_name, file_size), file_paths in file_duplicates.items():
        print('\n{} ({})\n'.format(file_name, file_size))
        print('\n'.join(file_paths))


if __name__ == '__main__':
    start_path = input('Input start path to find duplicates: ')
    if not os.path.exists(start_path):
        exit('Path not exists')
    file_duplicates = find_duplicates(start_path)
    if file_duplicates:
        print_duplicates(file_duplicates)
    else:
        print('No matches')
