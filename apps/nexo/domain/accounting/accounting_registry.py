class AccountingRegistry:

    def __init__(self):
        self._entries = []

    def register(
        self,
        entry: dict,
    ) -> dict:

        self._entries.append(entry)

        return entry

    def get_all(self):

        return self._entries
