#Cele:
#Generowanie losowej sekwencji DNA
#Wstawienie imienia użytkownika w sposób, który nie wpływa na statystyki
#Zapisanie sekwencji w formacie FASTA
#Obliczenie i wyświetlenie statystyk sekwencji
#Interaktywny interfejs użytkownika

#Kontekst zastosowań:
#Generowanie przykładowych danych do testów i eksperymentów:
#Edukacja i nauka:
#Badania naukowe:
#Testowanie algorytmów w bioinformatyce:
#Generowanie syntetycznych danych do celów demonstracyjnych:
#Tworzenie "fikcyjnych" baz danych genomowych:

import random  # Importujemy moduł 'random', który pozwala losować elementy (nukleotydy)

# Funkcja generująca losową sekwencję DNA z wstawionym imieniem
def generate_dna_sequence(length, name):
    # Lista możliwych nukleotydów w DNA
    nucleotides = ['A', 'C', 'G', 'T']
    
    # ORIGINAL:
    # sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    # MODIFIED (dodajemy osobne przechowywanie sekwencji DNA bez imienia do analizy statystycznej):
    # Generujemy losową sekwencję DNA (bez imienia) o zadanej długości
    dna_only = ''.join(random.choice(nucleotides) for _ in range(length))
    
    # Wybieramy losową pozycję, gdzie zostanie wstawione imię
    insert_position = random.randint(0, length - 1)
    
    # ORIGINAL:
    # sequence = sequence[:insert_position] + name + sequence[insert_position+len(name):]
    # MODIFIED (analiza tylko dna_only, imię dołączone tylko w wersji wyjściowej):
    # Tworzymy pełną sekwencję z imieniem wstawionym w losowe miejsce
    sequence_with_name = dna_only[:insert_position] + name + dna_only[insert_position:]
    
    # Zwracamy obie wersje sekwencji: z imieniem oraz czystą DNA
    return sequence_with_name, dna_only

# Funkcja obliczająca statystyki sekwencji DNA (bez imienia)
def calculate_statistics(sequence):
    # Liczymy wystąpienia każdego z nukleotydów
    A_count = sequence.count('A')
    C_count = sequence.count('C')
    G_count = sequence.count('G')
    T_count = sequence.count('T')

    # Obliczamy długość sekwencji DNA
    sequence_length = len(sequence)

    # Obliczamy procentową zawartość każdego nukleotydu
    A_percent = (A_count / sequence_length) * 100
    C_percent = (C_count / sequence_length) * 100
    G_percent = (G_count / sequence_length) * 100
    T_percent = (T_count / sequence_length) * 100

    # Obliczamy stosunek C+G do A+T (jako procent)
    CG_ratio = ((C_count + G_count) / (A_count + T_count)) * 100 if (A_count + T_count) != 0 else 0

    # Zwracamy obliczone statystyki
    return A_percent, C_percent, G_percent, T_percent, CG_ratio

# Funkcja zapisująca sekwencję do pliku w formacie FASTA
def save_to_fasta(sequence, sequence_id, description):
    # Tworzymy nazwę pliku z rozszerzeniem .fasta na podstawie ID
    filename = f"{sequence_id}.fasta"

    # Otwieramy plik do zapisu (tworzymy go, jeśli nie istnieje)
    with open(filename, 'w') as file:
        # Zapisujemy nagłówek FASTA w formacie: >ID Opis
        file.write(f">{sequence_id} {description}\n")

        # ORIGINAL:
        # file.write(sequence + "\n")
        # MODIFIED (zachowanie standardu FASTA: 60 znaków na linię):
        # Zapisujemy sekwencję w liniach po 60 znaków (standard FASTA)
        for i in range(0, len(sequence), 60):
            file.write(sequence[i:i+60] + "\n")

# Główna funkcja programu
def main():
    # ORIGINAL:
    # length = int(input("Podaj długość sekwencji: "))
    # MODIFIED (dodanie walidacji danych wejściowych dla długości sekwencji):
    # Pętla, która wymusza poprawne wprowadzenie długości sekwencji
    while True:
        try:
            # Pobieramy długość sekwencji od użytkownika i próbujemy skonwertować ją do liczby całkowitej
            length = int(input("Podaj długość sekwencji: "))
            # Sprawdzamy, czy długość jest większa od zera
            if length <= 0:
                print("Długość sekwencji musi być większa od zera.")
                continue
            break  # Wyjście z pętli jeśli dane są poprawne
        except ValueError:
            # Obsługa sytuacji, gdy użytkownik poda niepoprawny typ danych (np. litery)
            print("Proszę podać poprawną liczbę całkowitą.")

    # Pobieramy ID sekwencji od użytkownika
    sequence_id = input("Podaj ID sekwencji: ")

    # Pobieramy opis sekwencji od użytkownika
    description = input("Podaj opis sekwencji: ")

    # Pobieramy imię użytkownika (zostanie wstawione do sekwencji)
    name = input("Podaj imię: ")

    # Generujemy sekwencję DNA oraz wersję tylko z nukleotydami
    full_sequence, dna_only = generate_dna_sequence(length, name)

    # Zapisujemy sekwencję do pliku FASTA
    save_to_fasta(full_sequence, sequence_id, description)

    # Informujemy użytkownika o zapisanym pliku
    print(f"Sekwencja została zapisana do pliku {sequence_id}.fasta")

    # Obliczamy statystyki na podstawie sekwencji DNA bez imienia
    A_percent, C_percent, G_percent, T_percent, CG_ratio = calculate_statistics(dna_only)

    # Wyświetlamy statystyki sekwencji
    print("Statystyki sekwencji:")
    print(f"A: {A_percent:.1f}%")  # Procent A
    print(f"C: {C_percent:.1f}%")  # Procent C
    print(f"G: {G_percent:.1f}%")  # Procent G
    print(f"T: {T_percent:.1f}%")  # Procent T
    print(f"%CG: {CG_ratio:.1f}%")  # Procentowy stosunek (C+G)/(A+T)

# Uruchamiamy funkcję main(), jeśli plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()

