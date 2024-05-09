import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345


client_socket.connect((host, port))


countries = client_socket.recv(1024).decode('utf-8')
print("Выберите страну:")
print(countries)


selected_country = input("Введите название страны: ")
client_socket.sendall(selected_country.encode('utf-8'))


response = client_socket.recv(1024).decode('utf-8')
print(response)


client_socket.close()
