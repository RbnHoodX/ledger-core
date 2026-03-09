class Entry:
    """A double-entry journal entry linking two accounts."""

    def __init__(self, debit_account, credit_account, amount, memo=""):
        self._id = 0
        self._debit_account = debit_account
        self._credit_account = credit_account
        self._amount = amount
        self._memo = memo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def debit_account(self):
        return self._debit_account

    @property
    def credit_account(self):
        return self._credit_account

    @property
    def amount(self):
        return self._amount

    @property
    def memo(self):
        return self._memo

    def __repr__(self):
        return (f"Entry(id={self._id}, debit={self._debit_account.name!r}, "
                f"credit={self._credit_account.name!r}, amount={self._amount})")


class Journal:
    """Append-only journal of double-entry transactions."""

    def __init__(self):
        self._entries = []
        self._counter = 0

    def record(self, entry):
        self._counter += 1
        entry.id = self._counter
        self._entries.append(entry)
        entry.debit_account._add_entry(entry)
        entry.credit_account._add_entry(entry)
        return entry

    def entries(self):
        return list(self._entries)
