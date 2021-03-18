class ExtratorArgumentoURL:
    def __init__(self, url):
        if self.string_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moeda_origem, moeda_destino = self.__extrai_argumentos()
        string = f'Valor: {self.extrai_valor()}, Moeda Origem: {moeda_origem.title()}, ' \
                 f'Moeda Destino: {moeda_destino.title()}'
        return string

    @staticmethod
    def string_eh_valida(url):
        if url and url.startswith('https://bytebank.com'):
            return True
        else:
            return False

    def __extrai_argumentos(self):
        chave_moeda_origem = 'moedaorigem'.lower()
        chave_moeda_destino = 'moedadestino'.lower()

        index_inicial_moeda_origem = self.__encontra_indice_inicio_substring(chave_moeda_origem)
        index_final_moeda_origem = self.url.find('&')

        moeda_origem = self.url[index_inicial_moeda_origem:index_final_moeda_origem]

        moeda_origem = self.__lida_com_troca_moedas(chave_moeda_origem, moeda_origem)

        index_inicial_moeda_destino = self.__encontra_indice_inicio_substring(chave_moeda_destino)
        index_final_moeda_destino = self.url.find('&valor')
        moeda_destino = self.url[index_inicial_moeda_destino:index_final_moeda_destino]

        return moeda_origem, moeda_destino

    def __lida_com_troca_moedas(self, chave_moeda_origem, moeda_origem):
        if moeda_origem == 'moedadestino':
            self.__troca_moeda_origem()
            index_inicial_moeda_origem = self.__encontra_indice_inicio_substring(chave_moeda_origem)
            index_final_moeda_origem = self.url.find('&')
            moeda_origem = self.url[index_inicial_moeda_origem:index_final_moeda_origem]
        return moeda_origem

    def retorna_moedas(self):
        busca_moeda_origem = "moedaorigem"
        busca_moeda_destino = "moedadestino"

        inicio_substring_moeda_origem = self.__encontra_indice_inicio_substring(busca_moeda_origem)
        chave_moeda_origem_end = self.url.find("&")
        chave_valor = self.url.find("&valor")

        final_substring_moeda_origem = chave_valor \
            if inicio_substring_moeda_origem > chave_moeda_origem_end else chave_moeda_origem_end
        moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

        inicio_substring_moeda_destino = self.__encontra_indice_inicio_substring(busca_moeda_destino)

        final_substring_moeda_destino = self.url.find('&moedaorigem') \
            if inicio_substring_moeda_destino < inicio_substring_moeda_origem else chave_valor
        moeda_destino = self.url[inicio_substring_moeda_destino:final_substring_moeda_destino]

        return moeda_origem, moeda_destino

    def __encontra_indice_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor) + 1

    def __troca_moeda_origem(self):
        self.url = self.url.replace('moedadestino', 'real', 1)

    def extrai_valor(self):
        chave_valor_buscado = 'valor'
        indice_inicial_valor = self.__encontra_indice_inicio_substring(chave_valor_buscado)
        return self.url[indice_inicial_valor:]
