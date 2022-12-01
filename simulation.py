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
	R1.resistance = rs[0]
	R2.resistance = rs[1]
	analysis = simulator.operating_point()
	V2 = float(analysis['2'])
	PRl = V2 * V2 / Rl
	return PRl