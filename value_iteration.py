import numpy as np

def build_transition_matrices(mdp):
    S, A = mdp.n_states, mdp.n_actions
    P = np.zeros((S, A, S))
    R = np.zeros((S, A, S))

    # Recorrer todos los estados y acciones
    for s in range(S):
        for a in range(A):
            # probabilidad y siguiente estado
            transitions = mdp.get_transitions(s, a)
            for prob, s_next in transitions:
                P[s, a, s_next] += prob
                R[s, a, s_next]  = mdp.reward(s, a, s_next)

    return P, R

def value_iteration(mdp, epsilon=1e-6):
    P, R = build_transition_matrices(mdp)
    gamma = mdp.gamma

    # Inicializar matrices con ceros
    V = np.zeros(mdp.n_states)

    n_iter = 0
    while True:
        # Calcular el valor espearado de cada acción
        
        Q = np.sum(P * (R + gamma * V), axis=2) # Q(s,a) = Σ_{s'} P(s,a,s') * [ R(s,a,s') + γ V(s') ]
        V_new = np.max(Q, axis=1) #V_new(s) = max_a Q(s,a)

        delta = np.max(np.abs(V_new - V))
        V = V_new
        n_iter += 1

        if delta < epsilon:
            break

    return V, n_iter, P, R
