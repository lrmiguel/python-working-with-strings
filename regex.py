import re


def regex_telefone():
    padrao = "(\\+55)?\\s?(\\(?[1-9]{2}\\)?)?\\s?[0-9]{4,5}-?[0-9]{4}"
    telefone1 = '1234-4321'
    telefone2 = '(11)91234-4321'
    telefone3_incorreto = '(00)91234-4321'
    telefone4 = '+55 (11) 91234-4321'
    telefone5 = '+5511912344321'

    print(f'Telefone1: {valida_telefone(padrao, telefone1)}')
    print(f'Telefone2: {valida_telefone(padrao, telefone2)}')
    print(f'Telefone3 incorreto: {valida_telefone(padrao, telefone3_incorreto)}')
    print(f'Telefone4: {valida_telefone(padrao, telefone4)}')
    print(f'Telefone5: {valida_telefone(padrao, telefone5)}')


def valida_telefone(padrao_telefone, telefone):
    match_result = re.fullmatch(padrao_telefone, telefone)
    return 'Incorreto' if match_result is None else match_result.group()


def regex_descricao_contato():
    contato1 = 'Meu número é 1234-1234'
    contato2 = 'Fale comigo em 1234-1234. Esse é o meu telefone'
    contato3 = '1234-1234 é o meu celular'
    contato4 = 'lalaalalalaal 9543-1254 hsduoihfuioasofa qawrawdfds'
    padrao = '[0-9]{4}[-][0-9]{4}'
    retorno1 = re.search(padrao, contato1)
    retorno2 = re.search(padrao, contato2)
    retorno3 = re.search(padrao, contato3)
    retorno4 = re.search(padrao, contato4)
    print(f'Contato1: {retorno1.group()}')
    print(f'Contato2: {retorno2.group()}')
    print(f'Contato3: {retorno3.group()}')
    print(f'Contato4: {retorno4.group()}')


if __name__ == '__main__':
    regex_descricao_contato()
    print('-------------------------------')
    regex_telefone()
