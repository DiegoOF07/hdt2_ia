from frozenlake import FrozenLakeMDP
from value_iteration import value_iteration


def main():
    grid_name = './grid/grid.txt'
    epsilon = 1e-6

    mdp = FrozenLakeMDP(grid_name)

    print("Grid:")
    for _, row in enumerate(mdp.grid):
        print(" ".join(
            f"\033[31m{c}\033[0m" if c == 'H' else
            f"\033[33m{c}\033[0m" if c == 'G' else
            f"\033[36m{c}\033[0m" if c == 'S' else c
            for c in row
        ))

    V, n_iter, P, R = value_iteration(mdp)
    print(f"\nConvergencia en {n_iter} iteraciones.\n")

if __name__ == "__main__":
    main()
