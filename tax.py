class Helice:
    
    def _init_(self, rho, A):
        
        self.rho = rho  # Densidade do ar
        self.A = A      # Área da hélice

    def thrust(self, v):
       
        m = self.A * self.rho * v  # Fluxo de massa (kg/s)
        T = m * v  # Empuxo (N)
        
        return T

    def power(self, T, omega, P):

        p = omega * T  # Potência útil (W)
        e = p / P      # Eficiência (potência útil / potência do motor)
        
        return p, e

# Exemplo de uso da classe
helice = Helice(rho=1.225, A=0.5)  # Criando uma instância da classe Helice

# Calculando empuxo
velocidade_relativa = 10  # Velocidade relativa do ar em m/s
empuxo = helice.thrust(velocidade_relativa)
print(f"Empuxo: {empuxo} N")

# Calculando potência e eficiência
omega = 20  # Velocidade angular em rad/s
potencia_motor = 200  # Potência do motor em W
potencia_util, eficiencia = helice.power(empuxo, omega, potencia_motor)
print(f"Potência Útil: {potencia_util} W, Eficiência: {eficiencia:.2f}"
