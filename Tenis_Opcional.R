# Tenis avanzado
calculoPuntos2 <- function(p) {
  
  if ((puntuacion >= 3 && puntuacionRival >= 3 && abs(puntuacion - puntuacionRival) == 0) ||
      (juegos >= 5 && juegosRival >= 5 && abs(juegos - juegosRival) == 0)) {
    p <- 0.8
  }
  
  rd <- runif(1)
  if (rd < p) {
    puntuacion <<- puntuacion + 1
  } else {
    puntuacionRival <<- puntuacionRival + 1
  }
  
  if (puntuacion >= 4 || puntuacionRival >= 4) {
    diff <- puntuacion - puntuacionRival
    if (diff >= 2) {
      juegos <<- juegos + 1
      puntuacion <<- 0
      puntuacionRival <<- 0
    } else if (diff <= -2) {
      juegosRival <<- juegosRival + 1
      puntuacion <<- 0
      puntuacionRival <<- 0
    }
  }
  
  if ((juegos >= 6 || juegosRival >= 6) && abs(juegos - juegosRival) >= 2) {
    if (juegos > juegosRival) {
      sets <<- sets + 1
    } else {
      setsRival <<- setsRival + 1
    }
    juegos <<- 0
    juegosRival <<- 0
  }
}

resultadosT2 <- main(p_seq2, calculoPuntos2)
print(resultadosT2)

resultadosT2$simulacion <- "Puntos Tenis Avanzado"
resultadosComb2 <- rbind(resultadosT, resultadosT2)
print(resultadosComb2)

ggplot(resultadosComb2, aes(x = p, y = tasaVictoria, color = simulacion)) +
  geom_line(size = 1.2) +
  geom_point(size = 2) +
  labs(title = "Comparación de simulaciones",
       x = "Probabilidad p",
       y = "Tasa de victoria") +
  scale_x_continuous(limits = c(0.4, 0.6)) +
  theme_minimal() +
  theme(legend.title = element_blank(), 
        legend.position = "bottom")


# Tenis muy avanzado
calculoPuntos3 <- function(p1, p2) {
  
  if ((puntuacion >= 3 && puntuacionRival >= 3 && abs(puntuacion - puntuacionRival) == 0) ||
      (juegos >= 5 && juegosRival >= 5 && abs(juegos - juegosRival) == 0)) {
    p1 <- p2
  }
  
  rd <- runif(1)
  if (rd < p1) {
    puntuacion <<- puntuacion + 1
  } else {
    puntuacionRival <<- puntuacionRival + 1
  }
  
  if (puntuacion >= 4 || puntuacionRival >= 4) {
    diff <- puntuacion - puntuacionRival
    if (diff >= 2) {
      juegos <<- juegos + 1
      puntuacion <<- 0
      puntuacionRival <<- 0
    } else if (diff <= -2) {
      juegosRival <<- juegosRival + 1
      puntuacion <<- 0
      puntuacionRival <<- 0
    }
  }
  
  if ((juegos >= 6 || juegosRival >= 6) && abs(juegos - juegosRival) >= 2) {
    if (juegos > juegosRival) {
      sets <<- sets + 1
    } else {
      setsRival <<- setsRival + 1
    }
    juegos <<- 0
    juegosRival <<- 0
  }
}


main3 <- function(p_seq1, p_seq2) {
  resultados <- data.frame(
    p = numeric(),
    partidosGanados = numeric(),
    partidosPerdidos = numeric(),
    media = numeric()
  )
  
  for (p1 in p_seq1) {
    for (p2 in p_seq2){
      partidosGanados <- 0
      partidosPerdidos <- 0
      
      for (cont in 1:1000) {
        resetPartido()
        while (sets < 3 && setsRival < 3) {
          calculoPuntos3(p1, p2)
        }
        if (sets > setsRival) {
          partidosGanados <- partidosGanados + 1
        } else {
          partidosPerdidos <- partidosPerdidos + 1
        }
      }
      
      porcentaje <- partidosGanados / 1000
      
      resultados <- rbind(resultados, data.frame(
        p1 = p1,
        p2 = p2,
        partidosGanados = partidosGanados,
        partidosPerdidos = partidosPerdidos,
        tasaVictoria = porcentaje
      )
      )
    }
  }
  
  return(resultados)
}

resultadosT3 <- main3(p_seq2, p_seq3)
print(resultadosT3)

ggplot(resultadosT3, aes(x = p1, y = tasaVictoria, color = factor(p2), group = p2)) +
  geom_line(size = 1.2) +
  geom_point(size = 2) +
  labs(title = "Tasa de victoria según p1 y p2",
       x = "Probabilidad normal (p1)",
       y = "Tasa de victoria",
       color = "Prob. decisiva (p2)") +
  theme_minimal() +
  theme(legend.position = "bottom")