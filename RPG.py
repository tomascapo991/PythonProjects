"""
                RPG BÁSICO EN PYTHON
                    by Tomber991

           simulando sistema de batalla rpg

"""
Comandos="""
                ATK / Atacar al enemigo activo
                RUN / Huir del combate
                INV / Abrir inventario del Jugador
                EST / Ver estadisticas del Jugador
"""
Menu="""
                --- PYDUNGEON ---
            [escribe uno de los comandos]

                    * Explorar
                    * Salir

                    @Tomber991
"""

import random
import time

Juego_Config={
    "MSG_DIE": True
}

class Jugador:
    def __init__(self, nombre, nvl, exp, hp, ataque, defensa):
        self.nombre = nombre
        self.nvl = nvl
        self.exp = exp
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa

        self.Atacando=False

    def atacar(self, ENM):
        Danio_producido = random.randint(1,self.ataque)

        print(f"~ Has quitado {Danio_producido} puntos de daño")
        if Danio_producido==self.ataque:
            print("!!! Ataque Critíco")

        ENM.hp -= Danio_producido

class Enemigo_Class:
    def __init__(self, hp, ataque, defensa, nvl, exp):
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.nvl = nvl
        self.exp = exp
class Murcielago(Enemigo_Class):
      def __init__(self, hp, ataque, defensa, nvl, exp):
        super().__init__(self, hp, ataque, defensa, nvl, exp)
        def Especial_mismo (): #Efectos hacia sí mismo
          self.hp += self.hp/4
          print ("Murcielago regeneró puntos de vida")
        def Especial_contra (jd): #Efecto contra el jugador
          jd.hp -= jd.hp/8
          print ("El muercielago te ha dado un mordisco")

class Esqueleto(Enemigo_Class):
    def __init__(self, hp, ataque, defensa, nvl, exp, escudo):
        super().__init__(hp, ataque, defensa, nvl, exp)
        self.escudo = escudo
        self.nombre = "Esqueleto"
        print(" ! ESQUELETO ha aparecidó ! ")
    def Especial_mismo ():
      self.ataque += 1
      print ("Esqueleto aumento su ataque en 1")
      pass
    def Especial_contra (jd):
      jd.hp -= self.ataque
      print ("Esqueleto ha hecho un ataque doblo")
      pass

  
    def Salir(self):
        print("El esquelo está bailando antes de morir :´)")
        print("...")
        time.sleep(3)
        print("~ El esqueleto cayó :(")

    def ATK(self, jugador):
        jugador.hp-=self.ataque
        print(f"--- El Esqueleto te ha quitado {self.ataque}")

class Slime(Enemigo_Class):
    def __init__(self, hp, ataque, defensa, nvl, exp):
        super().__init__(hp, ataque, defensa, nvl, exp)
        self.nombre = "Slime"
        print(" ! SLIME ha aparecidó !")
    
  def Especial_mismo ():
    self.defensa += self.ataque/8
    print ("Slime aumento su defensa")
    print (f" ~ {self.defensa}")
      pass
    def Especial_contra (jd):
      print (f"Slime acaricia a {jd.nombre}")
      pass
   
def Salir(self):
        print("~ El Slime está saltando :D")
        time.sleep(3)
        print("El slime cayó")

    def ATK(self, jugador):
        jugador.hp-=self.ataque
        print(f"--- El Slime te ha quitado {self.ataque}")

def Spawn_Enemigo():
    Id=random.randint(1,2)
    HP=random.randint(5,10)
    ATK=random.randint(2,5)
    DEF=random .randint(1,3)
    BONUS=random.randint(2,3)

    Enemigo=None

    if Id==1:
        Enemigo=Esqueleto(HP, ATK, DEF, 1, 0, BONUS)
        return Enemigo

    elif Id==2:
        Enemigo=Slime(HP, ATK, DEF,1, 0)
        return Enemigo
    else:
        print("Al parecer no spawneo nada :/")

    print(f"--- Ha aparecido un {Enemigo.nombre}")

def main():
    # Obtenemos datos del jugador
    Nombre = input("""
            Antes de comenzar...
                ~ ¿Cual será tu nombre?: """)

    jugador = Jugador(Nombre, 1, 0, 100, 2, 0)

    while not jugador.Atacando:
        print(Menu)
        # --- BUCLE DE MENU ---
        msg=input(" - Ingresé acción: ")
        Enemigo=None

        if msg=="Explorar":
            jugador.Atacando=True
            Enemigo=Spawn_Enemigo()

        if msg=="Salir":
            print("!!! GRACIAS POR JUGAR <3 !!!")
            break

        while jugador.Atacando:
            Turno=jugador.nombre
            if Turno==jugador.nombre:
                print(f"Es el turno de {Nombre}")
                Act=input("~ ¿Que harás?: ")

                # CONTROLAR ACCIONES
                if Act=="ATK":
                    print(" - Estás atacando!")
                    jugador.atacar(Enemigo)

                    Turno=Enemigo.nombre

                elif Act=="RUN":
                    print(" - Estás huyendo!")
                    Turno=Enemigo.nombre
                    jugador.Atacando=False  # Esto detendrá el bucle de la batalla
                    break  # Esto romperá el bucle y volverá al bucle del menú
                elif Act=="INV":
                    print(" - Abres tu inventario")
                    Turno=Enemigo.nombre
                    pass
                elif Act=="EST":
                    print(f"""
--- ESTADISTICAS ---
 hp: {jugador.hp}
atk: {jugador.ataque}
def: {jugador.defensa}
nvl: {jugador.nvl}
exp: {jugador.exp}
                    """)
                elif Act=="EST ENM":
                    print(f"""
--- ESTADISTICAS DEL ENEMIGO ---
  hp: {Enemigo.hp}
 atk: {Enemigo.ataque}
 def: {Enemigo.defensa}
 nvl: {Enemigo.nvl}
 exp: {Enemigo.exp}
                    """)
                elif Act=="HELP":
                    print(Comandos)
                else:
                    print("!!! No puedes hacer eso ahora !!!")

            if Turno==Enemigo.nombre:
                if Enemigo.hp > 0:
                    print("El enemigo está atacando")
                    Enemigo.ATK(jugador)
                    print (f"{jugador.nombre}: {jugador.hp}")
                    print (f"{Enemigo.nombre}:{Enemigo.hp}")

                    dado=random.randint (0,16)
                    if dado>=8:
                      Enemigo.Especial_mismo ()
                    if dado==16:
                      Enemigo.Especial_contra (jugador)
                else:
                    if Juego_Config["MSG_DIE"]:
                        Enemigo.Salir()
                    else:
                        print("--- El Enemigo cayó")

                    jugador.Atacando=False

                if jugador.hp<=0:
                    print("""
!!! HAS PERDIDÓ !!!
                    """)
                    break

if __name__ == "__main__":
    main()
