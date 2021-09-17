#constants
h = 6.62607015 * 10 ** (-34)
kB = 1.380649 * 10 ** (-23)
lightspeed = 299792458
T0 = 298.15
R = 8.31446261815324
v_o2 = 1579.78
v_h2o_3 = 3755.79
v_h2o_1 = 1594.78
v_h2o_2 = 3656.65
v_co2_1 = 667.40
v_co2_2 = 667.40
v_co2_3 = 1388.15
v_co2_4 = 2349.16
n_he = 0.3125
n_o2 = 0.8
n_h2o = 0.2
n_co2 = 0.1
C_he = (3 / 2) * R * n_he
honey = 0


# t_char
def temp(v):
    return h * lightspeed / kB * 100 * v


# Tm
def Tm(c_n, t_n, t_prev, c_prev):
    t_k = - T0 * C_he / ((1 / 10) * c_n - (9 / 10) * C_he)
    if t_k < t_n:
        t_k = (-c_n * (t_n - t_prev) + c_n * t_n - c_prev * t_prev - T0 * C_he) / (
                    c_n - (9 / 10) * c_prev - (9 / 10) * C_he)
    return t_k


# Q
def heat(q_n, c_n, t_n, t1):
    return q_n + c_n * (t1 - t_n)


T = [(298, None)]
T.append((temp(v_o2), "O2"))
T.append((temp(v_h2o_1), "H2O"))
T.append((temp(v_h2o_2), "H2O"))
T.append((temp(v_h2o_3), "H2O"))
T.append((temp(v_co2_1), "CO2"))
T.append((temp(v_co2_2), "CO2"))
T.append((temp(v_co2_3), "CO2"))
T.append((temp(v_co2_4), "CO2"))
T.sort()

for N in range(1, 9):
    Q = 0
    C_co2 = R * 5 / 2 * n_co2
    C_h2o = R * 3 * n_h2o
    C_o2 = R * 5 / 2 * n_o2
    C = C_co2 + C_h2o + C_o2
    C_prev = 0
    for k in range(1, N + 1):
        Q += C * (T[k][0] - T[k - 1][0])
        if T[k][1] == "CO2":
            C_co2 += R * n_co2
        elif T[k][1] == "H2O":
            C_h2o += R * n_h2o
        elif T[k][1] == "O2":
            C_o2 += R * n_o2
        C_prev = C
        C = C_co2 + C_h2o + C_o2
    t = Tm(C, T[N][0], T[N - 1][0], C_prev)
    if (T[N][0] <= t) and ((N < 8) and t <= T[N + 1][0]):
        honey = 1
    if honey == 1:
        print("Cn", C)
        print("Tn", T[N][0])
        print("temp", t)
        print("heat", heat(Q, C, T[N][0], t))
    honey = 0
