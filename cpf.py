from gerar_cpf import gerar
from validar_cpf import validar

# Mensagem de Boas vindas
print()
print('### Olá! Este é um simples sistema de gerar e validar CPF, o sistema não é 100% perfeito e por conta disto eu '
      'peço paciência.')
print('### Criei o projeto com fins educacionais')
print()
print()

# Code
print('# Escolhe entre "gerar" e "validar".')
escolher_metodo = input('> ')

escolher_metodo = escolher_metodo.lower()

if escolher_metodo == 'gerar':
    gerar()
elif escolher_metodo == 'validar':
    validar()
else:
    print()
    print(f'### Método "{escolher_metodo}" não reconhecido')
    print()
