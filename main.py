import numpy as np
import matplotlib.pyplot as plt
from frozenlake import FrozenLakeMDP
from value_iteration import value_iteration, extract_policy


def print_policy(policy, mdp):
    arrows = {
        0: "↑",
        1: "↓",
        2: "→",
        3: "←"
    }

    policy_grid = np.array([
        arrows[action] if not mdp.is_terminal(s) else mdp.grid[s // mdp.n_cols][s % mdp.n_cols]
        for s, action in enumerate(policy)
    ]).reshape(mdp.n_rows, mdp.n_cols)

    print("\nPolítica Óptima:")
    for row in policy_grid:
        print(" ".join(row))


def plot_values(V, mdp):
    V_grid = V.reshape(mdp.n_rows, mdp.n_cols)

    plt.figure()
    plt.imshow(V_grid)
    plt.colorbar()
    plt.title("Mapa de Calor de V(s)")
    plt.show()


def main():
    grid_name = './grid/grid.txt'
    epsilon = 1e-6

    mdp = FrozenLakeMDP(grid_name)

    print("Grid:")
    for row in mdp.grid:
        print(" ".join(row))

    V, n_iter, P, R = value_iteration(mdp)

    print(f"\nConvergencia en {n_iter} iteraciones.\n")

    policy = extract_policy(V, P, R, mdp.gamma)
    print_policy(policy, mdp)
    plot_values(V, mdp)


if __name__ == "__main__":
    main()
