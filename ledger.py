from account import Account
from journal import Entry, Journal


class Ledger:
    """Double-entry bookkeeping ledger.

    Every transaction is a journal entry that debits one account and
    credits another by the same amount. This keeps the books balanced:
    total debits always equal total credits.
    """

    def __init__(self):
        self._accounts = {}
        self._journal = Journal()

    def create_account(self, name, kind="asset"):
        if name in self._accounts:
            raise ValueError(f"account {name!r} already exists")
        acct = Account(name, kind)
        self._accounts[name] = acct
        return acct

    def get_account(self, name):
        return self._accounts[name]

    def accounts(self):
        return list(self._accounts.values())

    def post(self, debit_name, credit_name, amount, memo=""):
        if amount <= 0:
            raise ValueError("amount must be positive")
        debit_acct = self._accounts[debit_name]
        credit_acct = self._accounts[credit_name]
        entry = Entry(debit_acct, credit_acct, amount, memo)
        self._journal.record(entry)
        return entry

    def journal_entries(self):
        return self._journal.entries()

    def trial_balance(self):
        total_debits = 0
        total_credits = 0
        for entry in self._journal.entries():
            total_debits += entry.amount
            total_credits += entry.amount
        return total_debits, total_credits
