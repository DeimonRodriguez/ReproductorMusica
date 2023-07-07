class ListaReproduccion:
    def __init__(self):
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"Canción '{cancion}' agregada a la lista de reproducción.")

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            print(f"Canción '{cancion}' eliminada de la lista de reproducción.")
        else:
            print(f"Canción '{cancion}' no existe en la lista de reproducción.")

    def reproducir_lista(self):
        if self.canciones:
            print("Reproduciendo lista de reproducción:")
            for cancion in self.canciones:
                print(cancion)
        else:
            print("La lista de reproducción está vacía.")

    def mostrar_lista(self):
        if self.canciones:
            print("Lista de reproducción:")
            for i, cancion in enumerate(self.canciones, 1):
                print(f"{i}. {cancion}")
        else:
            print("La lista de reproducción está vacía.")

lista_reproduccion = ListaReproduccion()
lista_reproduccion.agregar_cancion("¿A dodne vamos?")
lista_reproduccion.agregar_cancion("Hades")
lista_reproduccion.mostrar_lista()
lista_reproduccion.eliminar_cancion("Hades")
lista_reproduccion.reproducir_lista()