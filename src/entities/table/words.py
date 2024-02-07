class TableWords:
    def __init__(self, table: list[tuple[str, str]] = []) -> None:
        self.table = table

    def items(self) -> list[tuple[str, str]]:
        return self.table
