import scriptExtractTweets
import scriptMaps
import scriptStatistics
import os
import webbrowser


def option():
    os.system('cls')
    print("Selecciona una opción")
    print("\t1) Recolección de tweets y guardado")
    print("\t2) Configurar mapa")
    print("\t3) Mostrar el mapa")
    print("\t4) Estadísticas")
    print("\t5) Salir")


def menu():

    while True:
        option()
        optionMenu = input("Digite un numero >> ")

        if optionMenu == "1":
            scriptExtractTweets.extractTweets()
        elif optionMenu == "2":
            print('Configurando Mapa... \nPor Favor espere unos segundos...')
            scriptMaps.setMaps()
        elif optionMenu == "3":
            print('file://'+os.getcwd() + "/index.html")
            webbrowser.open('file://'+os.getcwd() +
                            "/index.html", new=2, autoraise=True)
        elif optionMenu == "4":
            print("Preparando Estadisticas...")
            scriptStatistics.getStatistics()
        elif optionMenu == "5":
            print('Cerrando todos los servicios...\nVuelva Pronto :)')
            break
        else:
            input(
                "No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")


if __name__ == '__main__':
    menu()
