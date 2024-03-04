import src.util.helper.interface as module_helper_interface
class ImportWordsRequest(module_helper_interface.EqualAttributes):
    def __init__(self, file_dir:str):
        self.file_dir = file_dir

class ImportWordsResponse(module_helper_interface.EqualAttributes):
    def __init__(self, file_list:list[str], words_imported: int, description_imported: int):
        self.file_list = file_list
        self.words_imported = words_imported
        self.description_imported = description_imported