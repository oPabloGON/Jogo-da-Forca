import random as rnd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variáveis globais para o jogo
definir_numero = 0
definir_lista = 0
palavra = ""
letras_usadas = []
chances = 10
ganhou = False
tentativa_habilitada = True  # Flag para controlar se tentativas ainda são permitidas

# Lista de imagens da forca
imagens_forca = [
    "Jogo-da-Forca/imagens/imagem1 copy.png",
    "Jogo-da-Forca/imagens/imagem1.png",
    "Jogo-da-Forca/imagens/imagem2.png",
    "Jogo-da-Forca/imagens/imagem3.png",
    "Jogo-da-Forca/imagens/imagem4.png",
    "Jogo-da-Forca/imagens/imagem5.png",
    "Jogo-da-Forca/imagens/imagem6.png",
    "Jogo-da-Forca/imagens/imagem7.png",
    "Jogo-da-Forca/imagens/imagem8.png",
    "Jogo-da-Forca/imagens/imagem9.png",
    "Jogo-da-Forca/imagens/imagem10.png"
]

# Função para iniciar um novo jogo
def iniciar_jogo():
    global definir_numero, definir_lista, palavra, letras_usadas, chances, ganhou, tentativa_habilitada

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

    definir_numero = rnd.randint(0, 100)  # Exemplo de valor aleatório
    definir_lista = rnd.randint(1, 3)
    letras_usadas = []
    chances = 10
    ganhou = False
    tentativa_habilitada = True

    if definir_lista == 1:
        palavra = obj[definir_numero % len(obj)]  # Usando o operador % para garantir que o índice esteja dentro dos limites da lista
        categoria_label.config(text='Categoria: Objeto')
    elif definir_lista == 2:
        palavra = animal[definir_numero % len(animal)]
        categoria_label.config(text='Categoria: Animal')
    elif definir_lista == 3:
        palavra = frutas[definir_numero % len(frutas)]
        categoria_label.config(text='Categoria: Fruta')

    resultado_label.config(text="")  # Limpar o resultado ao iniciar um novo jogo
    letras_usadas.clear()  # Limpar letras usadas ao iniciar novo jogo
    letras_usadas_label.config(text="Letras usadas:")
    atualizar_imagem_forca()  # Atualiza a imagem da forca ao iniciar novo jogo
    atualizar_interface()  # Atualiza a interface com a palavra oculta e as chances

    # Habilita a entrada de letras
    tentativa_entry.config(state=tk.NORMAL)
    tentativa_entry.bind('<Return>', processar_tentativa)  # Vincular tecla Enter para processar a tentativa

# Função para atualizar a interface gráfica com a palavra e letras usadas
def atualizar_interface():
    palavra_oculta = ' '.join([letra if letra.lower() in letras_usadas else '_' for letra in palavra])
    palavra_label.config(text=palavra_oculta)
    chances_label.config(text=f'Chances restantes: {chances}')

# Função para verificar se o jogador ganhou ou perdeu
def verificar_resultado():
    global ganhou, tentativa_habilitada
    if all(letra.lower() in letras_usadas for letra in palavra):
        ganhou = True
        resultado_label.config(text=f'Parabéns, você acertou! A palavra era "{palavra}"!')
        mostrar_opcoes_fim_jogo()
        # Desabilita a entrada de letras
        tentativa_entry.config(state=tk.DISABLED)
        tentativa_entry.unbind('<Return>')  # Desvincula a tecla Enter
        jogar_novamente_button.pack()  # Mostra o botão de jogar novamente
        sair_button.pack()  # Mostra o botão de sair
    elif chances == 0:
        resultado_label.config(text=f'Game Over! Você perdeu. A palavra era "{palavra}".')
        mostrar_opcoes_fim_jogo()
        tentativa_habilitada = False  # Desabilita futuras tentativas
        tentativa_entry.config(state=tk.DISABLED)  # Desabilita a entrada de letras
        tentativa_entry.unbind('<Return>')  # Desvincula a tecla Enter
        jogar_novamente_button.pack()  # Mostra o botão de jogar novamente
        sair_button.pack()  # Mostra o botão de sair
    atualizar_imagem_forca()  # Garante que a imagem da forca seja atualizada em todas as situações

# Função para mostrar opções após o fim do jogo
def mostrar_opcoes_fim_jogo():
    opcoes_frame.pack(pady=20)

# Função para iniciar um novo jogo após perder
def jogar_novamente():
    opcoes_frame.pack_forget()  # Esconder opções
    resultado_label.config(text="")  # Limpar o resultado ao iniciar um novo jogo
    imagem_forca_label.config(image="")  # Limpa a imagem da forca
    iniciar_jogo()

# Função para sair do jogo
def sair_jogo():
    if messagebox.askokcancel("Sair do Jogo", "Tem certeza que deseja sair do jogo?"):
        myApp.destroy()

# Função para processar a tentativa do jogador
def processar_tentativa(event=None):
    global chances
    tentativa = tentativa_entry.get().lower()

    if tentativa == "":
        return

    # Verificar se é uma letra
    if not tentativa.isalpha():
        resultado_label.config(text='Por favor, digite apenas letras.')
        tentativa_entry.delete(0, tk.END)
        return

    if tentativa in letras_usadas:
        resultado_label.config(text='Você já tentou esta letra. Tente outra.')
    else:
        letras_usadas.append(tentativa)
        letras_usadas_label.config(text=f"Letras usadas: {' '.join(letras_usadas)}")
        if tentativa not in palavra:
            chances -= 1

    tentativa_entry.delete(0, tk.END)  # Limpar a entrada após processar a tentativa
    atualizar_interface()
    verificar_resultado()

# Função para atualizar a imagem da forca na interface
def atualizar_imagem_forca():
    if chances > 0:
        img_path = imagens_forca[10 - chances]  # Seleciona a imagem correspondente ao número de chances restantes
    else:
        img_path = imagens_forca[-1]  # Se chances == 0, exibir a última imagem da lista

    img = tk.PhotoImage(file=img_path)

    # Redimensiona a imagem ao carregá-la usando subsample
    largura = 200  # Largura desejada da imagem
    altura = 200   # Altura desejada da imagem
    img = img.subsample(max(img.width() // largura, img.height() // altura))

    imagem_forca_label.config(image=img)
    imagem_forca_label.image = img  # Atualiza a imagem na interface

# Configuração da interface gráfica
myApp = tk.Tk()
myApp.title("Jogo da Forca")
myApp.geometry("700x500")
myApp.resizable(width=False, height=False)
myApp.configure(background='white')

# Estilo para todas as janelas com cor branca
style = ttk.Style()
style.configure('.', background='white')

# Definindo localizações e tamanhos dos widgets
titulo_label = ttk.Label(myApp, text="Jogo da Forca", font=('Arial', 24))
titulo_label.place(x=275, y=10)

categoria_label = ttk.Label(myApp, text="", font=('Arial', 14))
categoria_label.place(x=300, y=70)

palavra_label = ttk.Label(myApp, text="", font=('Arial', 18))
palavra_label.place(x=300, y=120)

chances_label = ttk.Label(myApp, text="", font=('Arial', 14))
chances_label.place(x=296, y=160)

tentativa_label = ttk.Label(myApp, text="Digite uma letra:", font=('Arial', 14))
tentativa_label.place(x=300, y=220)

tentativa_entry = ttk.Entry(myApp, font=('Arial', 14))
tentativa_entry.place(x=300, y=250)

resultado_label = ttk.Label(myApp, text="", font=('Arial', 14))
resultado_label.place(x=300, y=320)

letras_usadas_label = ttk.Label(myApp, text="Letras usadas:", font=('Arial', 14))
letras_usadas_label.place(x=50, y=380)

# Frame para as opções de fim de jogo (inicialmente oculto)
opcoes_frame = ttk.Frame(myApp)

# Botão para jogar novamente
jogar_novamente_button = ttk.Button(opcoes_frame, text="Jogar Novamente", command=jogar_novamente)

# Botão para sair do jogo
sair_button = ttk.Button(opcoes_frame, text="Sair", command=sair_jogo)

# Label para exibir a imagem da forca
imagem_forca_label = ttk.Label(myApp)
imagem_forca_label.place(x=50, y=60)

# Iniciar o primeiro jogo ao abrir a aplicação
iniciar_jogo()

myApp.mainloop()
