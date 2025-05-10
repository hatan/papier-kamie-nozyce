# Papier, Kamień, Nożyce

## Opis projektu
Projekt "Papier, Kamień, Nożyce" to gra wieloosobowa, w której dwóch graczy rywalizuje ze sobą, wybierając jedną z trzech opcji: papier, kamień lub nożyce. Gra jest realizowana za pomocą gniazd sieciowych, co pozwala na interakcję między klientem a serwerem.

## Pliki projektu
- `server/server.py`: Implementacja serwera, który obsługuje połączenia dwóch graczy, odbiera ich wybory, określa zwycięzcę i przesyła wynik z powrotem do graczy.
- `client/client.py`: Logika po stronie klienta, która łączy się z serwerem, wysyła wybór gracza i odbiera wynik gry.

## Instrukcje uruchomienia

### Uruchamianie serwera
1. Otwórz terminal i przejdź do katalogu `server`.
2. Uruchom serwer za pomocą polecenia:
   ```
   python server.py
   ```
3. Serwer będzie nasłuchiwał na porcie 12345 na połączenia od graczy.

### Uruchamianie klienta
1. Otwórz nowy terminal i przejdź do katalogu `client`.
2. Uruchom klienta za pomocą polecenia:
   ```
   python client.py
   ```
3. Klient połączy się z serwerem i poprosi o wybór (papier, kamień, nożyce).

## Zasady gry
- Papier pokonuje kamień.
- Kamień pokonuje nożyce.
- Nożyce pokonują papier.
- Jeśli obaj gracze wybiorą tę samą opcję, gra kończy się remisem.