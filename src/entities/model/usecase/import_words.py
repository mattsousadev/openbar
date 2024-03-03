import src.util.helper.interface as module_helper_interface
class ImportWordsResponse(module_helper_interface.EqualAttributes):

    def __init__(self, words_imported: int) -> None:
        self.words_imported = words_imported
