class Orders:
    def combine_orders(self, requests, n_max):
        """Calcula a quantidade mínima de viagens necessárias
        para transportar requisições, agrupadas em no máximo 2, que somado os valores
        atinja no máximo o número do parâmetro n_max.

        Parameters:
        requests (list): Lista de requisições com valores inteiros.
        n_max (int): Valor máximo permitido por viagem.

        Returns:
        int: Número mínimo de viagens necessárias para transportar toda a lista.
        """
        travels = 0
        requests_size = len(requests)
        if requests_size > 0:
            last_request = requests[0]
            travels += 1

            for i in range(1, requests_size):
                current_request = requests[i]

                if last_request is None:
                    traves += 1
                    last_request = current_request
                    continue
                if last_request + current_request <= n_max:
                    last_request = None
                else:
                    last_request = current_request
                    travels += 1

        return travels
