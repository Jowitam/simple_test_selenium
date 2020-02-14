# Testy

Testy automatyczne napisane w Pythonie przy użyciu Selenium.

Testy obejmują logowanie do [testowej platformy Allegro](https://allegro.pl.allegrosandbox.pl/)


####Niezbędne do działania:
- Chrome 
- [Chromedriver](https://chromedriver.chromium.org/downloads)
  - linux:
    - po rozpakowaniu chromedriver przenieść do `/usr/local/share`:
      > sudo mv -f ~/Downloads/chromedriver /usr/local/share/
      >                                                                    
      > sudo chmod +x /usr/local/share/chromedriver
    - stworzyć link w bin
      > sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
      > 
      > sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
      >
  - windows:
    - chromdriver rozpakować do dowolnego katalogu (takiego którego nie usuniemy)
    - dodać ścieżkę do lokalizacji chromdrivera do zmiennych środowiskowych PATH 
    
- Python 3.6 lub nowszy
- zależności w pliku `requirements.txt`

####Uruchomienie testów
- uruchomienie wszystkich testów
`python -m unittest TestCase/test_start.py`
- uruchomienie testów z konkretnego katalogu
`python -m unittest discover TestCase/`
- uruchomienie pojedynczego testu
`pyton -m unittest TestCase/test_login.py`