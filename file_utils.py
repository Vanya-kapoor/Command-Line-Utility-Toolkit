import os
def file_size(path):
    if os.path.exists(path):
        return os.path.getsize(path)
    return -1