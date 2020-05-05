import uuid

from App.setting import FILE_UP_LOADS_PATH, FILE_UP_LOADS


def transfor_file(file):
    exc = file.filename.rsplit(".")[1]
    uufilename = uuid.uuid4().hex

    file_loads_path = FILE_UP_LOADS_PATH + uufilename + "." + exc
    file.save(file_loads_path)

    file_path_name = FILE_UP_LOADS + uufilename + "." + exc

    return file_loads_path,file_path_name
