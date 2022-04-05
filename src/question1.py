class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """Dada uma lista de elementos do tipo Contract, retorna os top_n ids
        referente aos maiores débitos, ignorando os contratos já renegociados.

        Parameters:
        open_contracts (list): Lista de contratos em aberto.
        renegotiated_contracts (list): Lista dos ids dos contratos já renegociados.
        top_n (int): Quantidade de ids que devem ser retornados.

        Returns:
        list: ids referente aos maiores débitos, ordenados do maior para o menor.
        """

        ids_to_ignore = {}
        for renegotiated in renegotiated_contracts:
            # adicionando ids dos renegociados a um map para ser consultado
            # posteriormente em complexidade de O(1)
            ids_to_ignore[renegotiated] = True
        
        # filtrando os contratos para ignorar os contratos já renegociados
        open_contracts = list(filter(lambda c: not ids_to_ignore.get(c.id), open_contracts))
        # usando o sort nativo do python, que no pior dos casos tem complexidade O(n log n)
        open_contracts.sort(key=lambda c: c.debt, reverse=True)

        top_open_contracts = open_contracts[0:top_n]

        return list(map(lambda c: c.id, top_open_contracts))
