import random as rnd

while True:
    definir_numero = rnd.randint(1, 9)
    definir_lista = rnd.randint(1, 3)
    palavra = []
    ganhou = False
    letras_usadas = []
    chances = 10

    obj = [
       'cadeira', 'mesa', 'televisão', 'geladeira', 
       'fogão', 'armário', 'escrivaninha', 
       'cadeira de rodas', 'chuveiro'
    ]

    animal = [
        'cachorro', 'gato', 'papagaio', 'cavalo', 'galinha', 
         'camelo', 'elefante', 'girafa', 'hipopótamo', 
         'pinguin', 'urso', 'macaco', 'arara', 'tartaruga'
    ]

    frutas = [
      'maçã', 'pera', 'laranja', 'banana', 
      'morango', 'abacaxi', 'melancia', 'limão', 'bergamota', 'pessêgo', 'mamão',
      'goiaba', 'abacate', 'acerola'
    ]

    if definir_lista == 1:
        palavra = frutas[definir_numero]
        print('Sua palavra é uma fruta')
        print()
    elif definir_lista == 2:
        palavra = animal[definir_numero]
        print('Sua palavra é um animal')
        print()
    elif definir_lista == 3:
        palavra = obj[definir_numero]
        print('Sua palavra é um objeto')
        print()

    while True:
        acertos = 0
        for letra in palavra:
            if letra.lower() in letras_usadas:
                print(letra, end=' ')
                acertos += 1
            else:
                print('_', end=' ')

        print(f'      Você tem {chances} chances restantes')
        print()

        if acertos == len(palavra):
            ganhou = True
            break

        if chances == 0:
            break

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in letras_usadas:
            print('Você já tentou esta letra. Tente outra.')
            continue

        letras_usadas.append(tentativa)

        if tentativa not in palavra:
            chances -= 1

    if ganhou:
        print(f'Parabéns, você acertou! A palavra era {palavra}!')
    else:
        print(f'Você perdeu! A palavra era {palavra}.')

    resposta = input('Deseja jogar novamente? (s/n): ').lower()
    if resposta != 's':
        print('Obrigado por jogar!')
        break
    print()


