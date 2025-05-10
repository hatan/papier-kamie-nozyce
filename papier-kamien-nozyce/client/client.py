import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class GameClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Papier, Kamien, Nozyce")
        
        self.server_address = ('localhost', 12345)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        try:
            self.client_socket.connect(self.server_address)
        except Exception as e:
            messagebox.showerror("Blad", f"Nie udalo sie polaczyc z serwerem: {e}")
            self.master.destroy()
            return
        
        # Ask for the player's name
        self.name = simpledialog.askstring("Imie", "Podaj swoje imie:")
        if not self.name:
            messagebox.showinfo("Informacja", "Musisz podac imie, aby grac.")
            self.master.destroy()
            return
        
        self.client_socket.sendall(self.name.encode("utf-8"))
        
        # Wait for server messages
        server_message = self.client_socket.recv(1024).decode()
        messagebox.showinfo("Informacja", server_message)
        
        # Create buttons for choices
        self.label = tk.Label(master, text="Wybierz swoja opcje:")
        self.label.pack(pady=10)
        
        self.button_rock = tk.Button(master, text="Kamien", command=lambda: self.send_choice("kamien"))
        self.button_rock.pack(pady=5)
        
        self.button_paper = tk.Button(master, text="Papier", command=lambda: self.send_choice("papier"))
        self.button_paper.pack(pady=5)
        
        self.button_scissors = tk.Button(master, text="Nozyce", command=lambda: self.send_choice("nozyce"))
        self.button_scissors.pack(pady=5)
    
    def send_choice(self, choice):
        try:
            # Send the player's choice to the server
            self.client_socket.sendall(choice.encode("utf-8"))
            
            # Receive the result from the server
            result = self.client_socket.recv(1024).decode()
            messagebox.showinfo("Wynik", result)
        except Exception as e:
            messagebox.showerror("Blad", f"Nie udalo sie wyslac wyboru: {e}")
        finally:
            self.client_socket.close()
            self.master.destroy()

def main():
    root = tk.Tk()
    app = GameClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()