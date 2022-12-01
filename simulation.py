from PySpice.Spice.Netlist import Circuit

circuit = Circuit('Maxima transferencia de potencia')
Vin = 10
Rl = 50
circuit.V('input', 1, circuit.gnd, Vin)
R1 = circuit.R(1, 1, 2)
R2 = circuit.R(2, 2, circuit.gnd)
circuit.R(3, 2, circuit.gnd, Rl)
simulator = circuit.simulator(temperature=25, nominal_temperature=25)

def simulate(rs):
	r1 = 10**rs[0]
	r2 = 10**rs[1]
	R1.resistance = r1
	R2.resistance = r2
	analysis = simulator.operating_point()
	V1 = float(analysis['2'])
	Pout = V1 * V1 / Rl
	Pin = Vin * (Vin - V1) / r1
	return Pout / Pin