import file_handler
import logger


def search_files_with_file_type(search, path, file_type):
    files = search_files(search, path)
    return filter(lambda found_file: file_handler.get_file_type(found_file) == file_type, files)


def search_files(search, path):
    files = []
    keywords = search.split()  # Split on whitespace
    for file_name in file_handler.get_directory_content(path):
        file_path = path + '/' + file_name

        match = __match_file(keywords, file_name)
        if match:
            logger.log('Found file/folder: ' + file_path)
            files.append(file_path)

    if not files:
        logger.log('No matching files found: ' + search)
    return files


def __match_file(keywords, file_name):
    for keyword in keywords:
        if not __is_keyword_part_of_filename(keyword, file_name):
            return False
    return True


def __is_keyword_part_of_filename(keyword, file_name):
    return keyword.lower() in file_name.lower()  # keyword is part of name

