import socket
import random


country_codes = {
    "Россия": "+7 (9XX) XXX-XX-XX",
    "США": "+1 (XXX) XXX-XXXX",
    "Германия": "+49 (XXXX) XXXXXX",
    "Франция": "+33 (X) XX XX XX XX",
    "Япония": "+81 (XXX) XXX-XXXX"
}

def generate_number(country_code):
    digits = '0123456789'
    phone_num = ''
    for char in country_code:
        if char == 'X':
            phone_num += random.choice(digits)
        else:
            phone_num += char
    return phone_num


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345


server_socket.bind((host, port))


server_socket.listen(5)
print(f'Сервер запущен на {host}:{port}')

while True:

    client_socket, addr = server_socket.accept()
    print(f'Получено подключение от {addr}')


    countries = '\n'.join(country_codes.keys())
    client_socket.sendall(countries.encode('utf-8'))


    selected_country = client_socket.recv(1024).decode('utf-8')


    if selected_country in country_codes:
        phone_format = country_codes[selected_country]
        phone_number = generate_number(phone_format)
        response = f"Сгенерированный номер телефона для {selected_country}: {phone_number}"
    else:
        response = "Такая страна не найдена в списке."

    client_socket.sendall(response.encode('utf-8'))


    client_socket.close()


server_socket.close()
