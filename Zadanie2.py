# Korzystając z modułu socket i wiedzy o zapytaniach HTTP, 
# uzyskaj informację jaki serwer i w jakiej wersji jest uruchumiony pod adresem kretes.xyz
# Na wyjściu programu powinieneś uzyskać tylko informację o serwerze 
#
# Podpowiedź 1:
# http używa \r\n. Przy podziale na nowe linie zostaje \r. Aby temu zapobiec, użyteczna może być finkcja strip()
#
# Podpowiedź 2:
# Zadanie można wykonać korzystając z wyrażeń regularnych, jednak łatwiej będzie to zrobić 
# wykorzystując funkcję startswitch() objektu string
#
# Wykorzystaj poniższy szkielet kodu

import socket


def http_response():
    target_host = "kretes.xyz"

    target_port = 80
    
    ###########################
    ### Miejsce na Twój kod ###
    
    ###########################


if __name__ == "__main__":
    http_response()
