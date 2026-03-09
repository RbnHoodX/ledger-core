class Account:
    """A ledger account that tracks its balance from journal entries.

    The balance is always computed from entries -- never stored directly.
    This guarantees the balance is always consistent with the journal.
    """

    def __init__(self, name, kind="asset"):
        self._name = name
        self._kind = kind
        self._entries = []

    @property
    def name(self):
        return self._name

    @property
    def kind(self):
        return self._kind

    @property
    def balance(self):
        total = 0
        for entry in self._entries:
            if entry.debit_account is self:
                total += entry.amount
            elif entry.credit_account is self:
                total -= entry.amount
        return total

    def _add_entry(self, entry):
        self._entries.append(entry)

    def entries(self):
        return list(self._entries)

    def __repr__(self):
        return f"Account(name={self._name!r}, kind={self._kind!r})"
