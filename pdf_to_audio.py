import pyttsx3
import PyPDF2
import time

def read_pdf_to_audio(pdf_path):
    try:
        with open(pdf_path, 'rb') as book:
            play = pyttsx3.init()
            play.setProperty('rate', 150)  # Ajuste a velocidade da fala
            play.setProperty('volume', 1)  # Define o volume da fala (0.0 a 1.0)

            pdf_reader = PyPDF2.PdfReader(book)
            num_pages = len(pdf_reader.pages)

            print('Iniciando leitura do Audiolivro')

            for num in range(num_pages):
                page = pdf_reader.pages[num]
                data = page.extract_text()

                if data:
                    print(f"Lendo página {num + 1} de {num_pages}...")
                    play.say(data)
                    play.runAndWait()
                    time.sleep(1)  # Pausa entre as páginas
                else:
                    print(f"Página {num + 1} não contém texto legível ou está vazia.")

            print('Leitura concluída.')

    except FileNotFoundError:
        print(f"Erro: O arquivo '{pdf_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamada da função
pdf_path = 'mybook.pdf'  # Substitua pelo caminho correto do seu arquivo
read_pdf_to_audio(pdf_path)
