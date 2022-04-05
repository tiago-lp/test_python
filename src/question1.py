class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        ids_to_ignore = {}
        for renegotiated in renegotiated_contracts:
            ids_to_ignore[renegotiated] = True
        
        open_contracts = list(filter(lambda c: not ids_to_ignore.get(c.id), open_contracts))
        open_contracts.sort(key=lambda c: c.debt, reverse=True)

        top_open_contracts = open_contracts[0:top_n]

        return list(map(lambda c: c.id, top_open_contracts))
