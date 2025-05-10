import socket

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Remis!"
    elif (choice1 == "papier" and choice2 == "kamień") or \
         (choice1 == "kamień" and choice2 == "nożyce") or \
         (choice1 == "nożyce" and choice2 == "papier"):
        return "Gracz 1 wygrywa!"
    else:
        return "Gracz 2 wygrywa!"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(2)

print("Serwer oczekuje na graczy...")

conn1, addr1 = server_socket.accept()
print(f"Gracz 1 połączony: {addr1}")

conn2, addr2 = server_socket.accept()
print(f"Gracz 2 połączony: {addr2}")

conn1.sendall("Podaj swój wybór (papier, kamień, nożyce): ".encode("utf-8"))
choice1 = conn1.recv(1024).decode().strip()

conn2.sendall("Podaj swój wybór (papier, kamień, nożyce): ".encode("utf-8"))
choice2 = conn2.recv(1024).decode().strip()

result = determine_winner(choice1, choice2)

conn1.sendall(result.encode())
conn2.sendall(result.encode())

conn1.close()
conn2.close()
server_socket.close()