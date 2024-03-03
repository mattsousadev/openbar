import src.service.file as module_service_file
import src.entities.table.words as module_table_words

class FileServiceStub(module_service_file.FileService):
    def move_to_processing(self, file_dir:str) -> list[str]:
        return ['processing/moved_file']

    def move_to_processed(self, files_path:list[str]) -> list[str]:
        return ['processed/moved_file']
    
    def exists(self, path) -> bool:
        return True

    def read_words_file(self, file_path: str) -> module_table_words.TableWords:
        return module_table_words.TableWords([
            ('any_word','any_description'),
            ('any_word_1','any_description_1')
        ])

    def persist_file(self, base64_file:str, file_path:str):
        return True

    def encode_to_base64(self, file_path:str, encoding: str) -> str:
        return 'any_base64'