# Hoja de Trabajo 2 – Frozen Lake – Value Iteration

---

## Descripción del Proyecto

Este proyecto implementa un **Markov Decision Process (MDP)** para el entorno clásico *Frozen Lake* y resuelve el problema utilizando el algoritmo de **Value Iteration**.

---

## Entorno: Frozen Lake

El entorno consiste en un grid 4x4:

- **S** → Start (inicio)
- **F** → Frozen (seguro)
- **H** → Hole (terminal sin recompensa)
- **G** → Goal (terminal con recompensa +1)

El entorno es **estocástico**:

Al elegir una acción, el agente tiene:
- 1/3 probabilidad de ir hacia la dirección deseada
- 1/3 probabilidad de ir hacia cada dirección perpendicular

El factor de descuento utilizado es:

\[
\gamma = 0.9
\]

---

## Resultados

El programa imprime:

- Número de iteraciones hasta convergencia
- Matriz 4x4 con la acción óptima (flechas)
- Mapa de calor de los valores finales \( V(s) \)

---

## Cómo ejecutar

```bash
python main.py
```