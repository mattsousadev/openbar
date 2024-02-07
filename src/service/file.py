
import src.entities.table.words as module_table_words
# TODO: Create base class for file service
class FileService:
    def move_to_processing(self, file_dir:str) -> None:
        pass
    
    def exists(self, path) -> bool:
        pass

    def read_words_file(self, file_path: str) -> module_table_words.TableWords:
        pass