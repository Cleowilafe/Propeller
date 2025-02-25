import math

class Helice:
    
    def __init__(self, rho, c_t, D):
        self.rho = rho  # Densidade do ar
        self.c_t = c_t  # Coeficiente de empuxo
        self.D = D      # Diâmetro da hélice
        self.A = self.cross_section(D)  # Área da seção da hélice
    
    def cross_section(self, D):
        # Cálculo da área da seção transversal da hélice (A)
        A = (math.pi/4) * D**2
        return A
    
    def thrust(self, v):
        # Calculando empuxo
        T = self.rho * self.A * v**2 * self.c_t  # Empuxo (N)
        return T

    def power(self, T, v, P):
        # Potência útil (W) considerando a eficiência da hélice
        p_util = T * v

        # Eficiência
        eficiencia = p_util / P

        return p_util, eficiencia
    
    def torque(self, pot, n):
        # Cálculo do torque (N·m)
        Q = pot / (2 * math.pi * n)  # Torque
        return Q

    def arrasto(self, v, c_d):
        # Cálculo da força de arrasto (N)
        D = 0.5 * self.rho * v**2 * c_d * self.A  # Arrasto
        return D


#########################################painel############################################

# Parâmetros iniciais
rho = 1.225  # Densidade do ar (kg/m³)
c_t = 0.1    # Coeficiente de empuxo
D = 0.2      # Diâmetro da hélice (m)

# Criando uma instância da classe Hélice
helice = Helice(rho, c_t, D)

# Calculando empuxo
velocidade_relativa = 10  # Velocidade relativa do ar em m/s
empuxo = helice.thrust(velocidade_relativa)
print(f"Empuxo: {empuxo} N")

# Calculando potência útil e eficiência
potencia_motor = 200  # Potência do motor em W
potencia_util, eficiencia = helice.power(empuxo, velocidade_relativa, potencia_motor)
print(f"Potência Útil: {potencia_util} W, Eficiência: {eficiencia:.2f}")

# Calculando torque
n = 20  # Frequência de rotação (em Hz)
torque = helice.torque(potencia_motor, n)
print(f"Torque: {torque} N·m")

# Calculando arrasto (supondo um coeficiente de arrasto c_d)
c_d = 0.05  # Coeficiente de arrasto típico
arrasto = helice.arrasto(velocidade_relativa, c_d)
print(f"Arrasto: {arrasto} N")
