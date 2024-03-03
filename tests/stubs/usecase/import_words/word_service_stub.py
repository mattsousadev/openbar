import src.service.word as module_service_word

class WordServiceStub(module_service_word.WordService):
    def persist_words(self, table_words:tuple[str, str]) -> int:
        return 1