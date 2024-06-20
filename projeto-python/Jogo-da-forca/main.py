import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "inteligencia", "artificial", "dados", "desenvolvimento"]
    return random.choice(palavras)

def exibir_estado_atual(palavra, letras_adivinhadas):
    estado_atual = [letra if letra in letras_adivinhadas else '_' for letra in palavra]
    return ' '.join(estado_atual)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6
    letras_erradas = set()

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra antes de cometer 6 erros.")

    while tentativas_restantes > 0:
        print(f"\nPalavra: {exibir_estado_atual(palavra, letras_adivinhadas)}")
        print(f"Erros: {' '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra:
            letras_adivinhadas.add(tentativa)
            if set(palavra) == letras_adivinhadas:
                print(f"Parabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1
            if tentativas_restantes == 0:
                print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()