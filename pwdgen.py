import random
import string
import json
import datetime
import PySimpleGUI as sg

# Função para gerar senhas aleatórias
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Função para salvar a senha no arquivo JSON
def save_password_to_file(site, password):
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%d/%m/%Y %H:%M")

    if site in data:
        data[site].insert(0, {
            'password': password,
            'date_generated': formatted_time
        })
    else:
        data[site] = [{
            'password': password,
            'date_generated': formatted_time
        }]

    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

# Função principal para criar a interface gráfica
def main():
    sg.theme('SystemDefault1')

    layout = [
        [sg.Text('Site/Aplicativo:'), sg.InputText(key='-SITE-')],
        [sg.Button('Gerar Senha'), sg.Button('Ver Senhas Anteriores')],
        [sg.Output(size=(50, 3), key='-OUTPUT-PASSWORD-')],
        [sg.Output(size=(50, 10), key='-OUTPUT-PREVIOUS-PASSWORDS-')]
    ]

    window = sg.Window('Gerador de Senhas', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Gerar Senha':
            site = values['-SITE-'].strip()
            if site:
                password = generate_password()
                save_password_to_file(site, password)
                window['-OUTPUT-PASSWORD-'].update(f"Senha gerada: {password}")
            else:
                sg.popup_error("Por favor, informe o site/aplicativo para o qual a senha será gerada.")

        if event == 'Ver Senhas Anteriores':
            site = values['-SITE-'].strip()
            if site:
                try:
                    with open('passwords.json', 'r') as file:
                        data = json.load(file)
                        if site in data:
                            passwords = data[site]
                            previous_passwords = "\n".join([f"Senha: {entry['password']} - Data: {entry['date_generated']}" for entry in passwords])
                            window['-OUTPUT-PREVIOUS-PASSWORDS-'].update("Senhas Anteriores:\n" + previous_passwords)
                        else:
                            window['-OUTPUT-PREVIOUS-PASSWORDS-'].update("Nenhuma senha encontrada para este site.")
                except (FileNotFoundError, json.JSONDecodeError):
                    window['-OUTPUT-PREVIOUS-PASSWORDS-'].update("Nenhuma senha encontrada.")
            else:
                sg.popup_error("Por favor, informe o site/aplicativo para o qual deseja ver as senhas anteriores.")

    window.close()

if __name__ == "__main__":
    main()
