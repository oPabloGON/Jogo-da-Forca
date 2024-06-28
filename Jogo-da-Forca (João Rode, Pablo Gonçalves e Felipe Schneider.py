import random as rnd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

definir_numero = 0
definir_lista = 0
palavra = ""
letras_usadas = []
chances = 10
ganhou = False
tentativa_habilitada = True  

imagens_forca = [
    "imagens\imagem1 copy.png",
    "imagens\imagem1.png",
    "imagens\imagem2.png",
    "imagens\imagem3.png",
    "imagens\imagem4.png",
    "imagens\imagem5.png",
    "imagens\imagem6.png",
    "imagens\imagem7.png",
    "imagens\imagem8.png",
    "imagens\imagem9.png",
    "imagens\imagem10.png"
]

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

    definir_numero = rnd.randint(0, 100) 
    definir_lista = rnd.randint(1, 3)
    letras_usadas = []
    chances = 10
    ganhou = False
    tentativa_habilitada = True

    if definir_lista == 1:
        palavra = obj[definir_numero % len(obj)]  
        categoria_label.config(text='Categoria: Objeto')
    elif definir_lista == 2:
        palavra = animal[definir_numero % len(animal)]
        categoria_label.config(text='Categoria: Animal')
    elif definir_lista == 3:
        palavra = frutas[definir_numero % len(frutas)]
        categoria_label.config(text='Categoria: Fruta')

    resultado_label.config(text="") 
    letras_usadas.clear()  
    letras_usadas_label.config(text="Letras usadas:")
    atualizar_imagem_forca()  
    atualizar_interface()  
  
    tentativa_entry.config(state=tk.NORMAL)
    tentativa_entry.bind('<Return>', processar_tentativa)


def atualizar_interface():
    palavra_oculta = ' '.join([letra if letra.lower() in letras_usadas else '_' for letra in palavra])
    palavra_label.config(text=palavra_oculta)
    chances_label.config(text=f'Chances restantes: {chances}')


def verificar_resultado():
    global ganhou, tentativa_habilitada
    if all(letra.lower() in letras_usadas for letra in palavra):
        ganhou = True
        resultado_label.config(text=f'Parabéns, você acertou! A palavra era "{palavra}"!')
        mostrar_opcoes_fim_jogo()

        tentativa_entry.config(state=tk.DISABLED)
        tentativa_entry.unbind('<Return>')  
        jogar_novamente_button.pack()  
        sair_button.pack()  
    elif chances == 0:
        resultado_label.config(text=f'Game Over! Você perdeu. A palavra era "{palavra}".')
        mostrar_opcoes_fim_jogo()
        tentativa_habilitada = False
        tentativa_entry.config(state=tk.DISABLED) 
        tentativa_entry.unbind('<Return>') 
        jogar_novamente_button.pack() 
        sair_button.pack()  
    atualizar_imagem_forca()  

def mostrar_opcoes_fim_jogo():
    opcoes_frame.pack(pady=20)

def jogar_novamente():
    opcoes_frame.pack_forget() 
    resultado_label.config(text="")  
    imagem_forca_label.config(image="") 
    iniciar_jogo()

def sair_jogo():
    if messagebox.askokcancel("Sair do Jogo", "Tem certeza que deseja sair do jogo?"):
        myApp.destroy()

def processar_tentativa(event=None):
    global chances
    tentativa = tentativa_entry.get().lower()

    if tentativa == "":
        return

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

    tentativa_entry.delete(0, tk.END)
    atualizar_interface()
    verificar_resultado()

def atualizar_imagem_forca():
    if chances > 0:
        img_path = imagens_forca[10 - chances]  
    else:
        img_path = imagens_forca[-1]  

    img = tk.PhotoImage(file=img_path)

    largura = 200 
    altura = 200  
    img = img.subsample(max(img.width() // largura, img.height() // altura))

    imagem_forca_label.config(image=img)
    imagem_forca_label.image = img

myApp = tk.Tk()
myApp.title("Jogo da Forca")
myApp.geometry("700x500")
myApp.resizable(width=False, height=False)
myApp.configure(background='white')

style = ttk.Style()
style.configure('.', background='white')

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
resultado_label.place(x=225, y=320)

letras_usadas_label = ttk.Label(myApp, text="Letras usadas:", font=('Arial', 14))
letras_usadas_label.place(x=50, y=380)

opcoes_frame = ttk.Frame(myApp)

jogar_novamente_button = ttk.Button(opcoes_frame, text="Jogar Novamente", command=jogar_novamente)

sair_button = ttk.Button(opcoes_frame, text="Sair", command=sair_jogo)

imagem_forca_label = ttk.Label(myApp)
imagem_forca_label.place(x=50, y=60)

iniciar_jogo()

myApp.mainloop()
