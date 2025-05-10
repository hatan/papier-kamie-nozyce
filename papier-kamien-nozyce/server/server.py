import socket

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Remis!"
    elif (choice1 == "papier" and choice2 == "kamien") or \
         (choice1 == "kamien" and choice2 == "nozyce") or \
         (choice1 == "nozyce" and choice2 == "papier"):
        return "Gracz 1 wygrywa!"
    else:
        return "Gracz 2 wygrywa!"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(2)

print("Serwer oczekuje na graczy...")

# Accept connection from Player 1
conn1, addr1 = server_socket.accept()
name1 = conn1.recv(1024).decode().strip()  # Receive Player 1's name
print(f"Gracz 1 polaczony: {addr1}, Imie: {name1}")
conn1.sendall("Czekaj na drugiego gracza...".encode("utf-8"))

# Accept connection from Player 2
conn2, addr2 = server_socket.accept()
name2 = conn2.recv(1024).decode().strip()  # Receive Player 2's name
print(f"Gracz 2 polaczony: {addr2}, Imie: {name2}")
conn2.sendall("Gracz 1 jest juz polaczony. Mozecie zaczynac gre.".encode("utf-8"))
conn1.sendall("Drugi gracz sie polaczyl. Mozecie zaczynac gre.".encode("utf-8"))

# Ask for choices
conn1.sendall("Podaj swoj wybor (papier, kamien, nozyce): ".encode("utf-8"))
choice1 = conn1.recv(1024).decode().strip()

conn2.sendall("Podaj swoj wybor (papier, kamien, nozyce): ".encode("utf-8"))
choice2 = conn2.recv(1024).decode().strip()

# Determine the winner
result = determine_winner(choice1, choice2)

# Send the result to both players
conn1.sendall(result.encode())
conn2.sendall(result.encode())

# Close connections
conn1.close()
conn2.close()
server_socket.close()