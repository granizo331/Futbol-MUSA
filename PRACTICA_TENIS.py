import random
import matplotlib.pyplot as plt

# ------------------ TENIS ------------------
def jugar_tiebreak(p):
    puntos_tb = 0
    puntos_tb_rival = 0
    while True:
        if random.random() < p:
            puntos_tb += 1
        else:
            puntos_tb_rival += 1
        if (puntos_tb >= 7 or puntos_tb_rival >= 7) and abs(puntos_tb - puntos_tb_rival) >= 2:
            return puntos_tb > puntos_tb_rival

def simular_tenis(p):
    puntuacion = 0
    puntuacion_rival = 0
    juegos = 0
    juegos_rival = 0
    sets = 0
    sets_rival = 0

    while sets < 3 and sets_rival < 3:
        if random.random() < p:
            puntuacion += 1
        else:
            puntuacion_rival += 1

        if puntuacion >= 4 or puntuacion_rival >= 4:
            diff = puntuacion - puntuacion_rival
            if diff >= 2:
                juegos += 1
                puntuacion = 0
                puntuacion_rival = 0
            elif diff <= -2:
                juegos_rival += 1
                puntuacion = 0
                puntuacion_rival = 0

        if juegos == 6 and juegos_rival == 6:
            if jugar_tiebreak(p):
                sets += 1
            else:
                sets_rival += 1
            juegos = 0
            juegos_rival = 0
        elif (juegos >= 6 or juegos_rival >= 6) and abs(juegos - juegos_rival) >= 2:
            if juegos > juegos_rival:
                sets += 1
            else:
                sets_rival += 1
            juegos = 0
            juegos_rival = 0

    return sets > sets_rival

# ------------------ BÁDMINTON ------------------
def simular_badminton(p):
    sets = 0
    sets_rival = 0
    while sets < 2 and sets_rival < 2:
        puntos = 0
        puntos_rival = 0
        while True:
            if random.random() < p:
                puntos += 1
            else:
                puntos_rival += 1
            if (puntos >= 21 or puntos_rival >= 21) and abs(puntos - puntos_rival) >= 2:
                if puntos > puntos_rival:
                    sets += 1
                else:
                    sets_rival += 1
                break
    return sets > sets_rival

# ------------------ TENIS DE MESA ------------------
def simular_tenis_mesa(p):
    sets = 0
    sets_rival = 0
    while sets < 3 and sets_rival < 3:
        puntos = 0
        puntos_rival = 0
        while True:
            if random.random() < p:
                puntos += 1
            else:
                puntos_rival += 1
            if (puntos >= 11 or puntos_rival >= 11) and abs(puntos - puntos_rival) >= 2:
                if puntos > puntos_rival:
                    sets += 1
                else:
                    sets_rival += 1
                break
    return sets > sets_rival

# ------------------ Simulación y gráfica ------------------
probabilidades = [round(i / 100, 2) for i in range(0, 101)]
porcentajes_tenis = []
porcentajes_badminton = []
porcentajes_tenis_mesa = []

for p in probabilidades:
    total_partidos = 1000
    victorias_tenis = sum(simular_tenis(p) for _ in range(total_partidos))
    victorias_badminton = sum(simular_badminton(p) for _ in range(total_partidos))
    victorias_tenis_mesa = sum(simular_tenis_mesa(p) for _ in range(total_partidos))

    porcentajes_tenis.append((victorias_tenis / total_partidos) * 100)
    porcentajes_badminton.append((victorias_badminton / total_partidos) * 100)
    porcentajes_tenis_mesa.append((victorias_tenis_mesa / total_partidos) * 100)

    if p == 0.54:
        print("Esta es la probabilidad obtenida usando p =", p)
        print("Tenis - Partidos ganados:", victorias_tenis)
        print("Tenis - Partidos perdidos:", total_partidos - victorias_tenis)
        print("Bádminton - Partidos ganados:", victorias_badminton)
        print("Bádminton - Partidos perdidos:", total_partidos - victorias_badminton)
        print("Tenis de Mesa - Partidos ganados:", victorias_tenis_mesa)
        print("Tenis de Mesa - Partidos perdidos:", total_partidos - victorias_tenis_mesa)

# ------------------ Gráfica ------------------
plt.figure(figsize=(10, 6))
plt.plot(probabilidades, porcentajes_tenis, label='Tenis', color='blue', marker='o', markersize=3)
plt.plot(probabilidades, porcentajes_badminton, label='Bádminton', color='green', marker='s', markersize=3)
plt.plot(probabilidades, porcentajes_tenis_mesa, label='Tenis de Mesa', color='red', marker='^', markersize=3)
plt.title('Porcentaje de Partidos Ganados vs. Probabilidad de Ganar un Punto')
plt.xlabel('Probabilidad de Ganar un Punto (p)')
plt.ylabel('Porcentaje de Partidos Ganados (%)')
plt.grid(True)
plt.xlim(0.3, 0.7)
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.show()