import sys
import os

# Pobierz ścieżkę do bieżącego folderu (tests)
current_folder = os.path.dirname(os.path.abspath(__file__))

# Pobierz ścieżkę do folderu głównego (zawierającego pliki .py)
main_folder = os.path.dirname(current_folder)

# Dodaj ścieżkę folderu głównego do sys.path
sys.path.insert(0, main_folder)
