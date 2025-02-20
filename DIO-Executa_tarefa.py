import speech_recognition as sr
import pywhatkit
import os
from IPython.display import display, Markdown

# Função para reconhecer a fala
def reconhecer_fala():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Diga um comando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {comando}")
        return comando
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento de fala.")
        return None

# Função para executar comandos
def executar_comando(comando):
    if "pesquisar" in comando:
        termo = comando.replace("pesquisar", "").strip()
        if termo:
            display(Markdown(f"🔍 **Pesquisando na Wikipédia:** {termo}"))
            pywhatkit.search(termo)
        else:
            print("Nenhum termo foi especificado para pesquisa.")

    elif "calculadora" in comando:
        print("Abrindo a calculadora...")
        os.system("gnome-calculator")  # Para Linux, use 'calc' no Windows
    
    else:
        print("Comando não reconhecido.")

# Loop principal
while True:
    comando = reconhecer_fala()
    if comando:
        executar_comando(comando)
