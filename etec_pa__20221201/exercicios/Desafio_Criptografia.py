import string

print('---Bem vindo ao Criptador; Informe o tipo de chave a ser gerada [ CRIPT ] ou [ DESCRIPT ]')
tipo = input('digite aqui -> ')
alfa = list(string.ascii_lowercase)
mensagem = list(input('insira a mensagem -> '))
chave = int(input('insira quantas chaves serão necessarias para criptorafia -> '))
cripto = []

if tipo == 'cript':
    for letra in mensagem:
        indice = ord(letra)
        novoIndice = (indice + chave)
        if novoIndice > 122:
            novoIndice = (indice + chave)-len(alfa)
        cripto.append(chr(novoIndice))
    print(f'--MENSAGEM CRIPGRTAFADA É -- {cripto} ---')
    print('============ PROGRAMA ENCERRADO ============')

elif tipo == 'descript':
    for letra in mensagem:
        indice = ord(letra)
        novoIndice = (indice - chave)+len(alfa)
        if novoIndice > 122:
            novoIndice = (indice - chave)
        cripto.append(chr(novoIndice))
    print(f'--MENSAGEM DESCRIPGRTAFADA É -- {cripto} ---')
    print('============ PROGRAMA ENCERRADO ============')

'''
- links de referencia de conteúdo 

- https://github.com/python-cafe/exemplos/blob/master/criptografia/cripto.py
- https://en.wikipedia.org/wiki/List_of_Unicode_characters
- https://www.programiz.com/python-programming/methods/built-in/chr
'''



    