# Equations of 4-spin Ising model.

# 30/12/2017
from numpy import zeros, exp

def calc_observables(params):
	"""
	Give each set of parameters concatenated into one array.
	"""
	Cout = zeros((10))
	H = params[0:4]
	J = params[4:10]
	Z = +exp(+0)+exp(+H[3]+0)+exp(+H[2]+0)+exp(+H[2]+H[3]+J[5])+exp(+H[1]+0)+exp(+H[1]+H[3]+J[4])+exp(+H[1]+H[2]+J[3])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+0)+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5])
	Cout[0] = (+exp(+H[0]+0)+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[1] = (+exp(+H[1]+0)+exp(+H[1]+H[3]+J[4])+exp(+H[1]+H[2]+J[3])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[2] = (+exp(+H[2]+0)+exp(+H[2]+H[3]+J[5])+exp(+H[1]+H[2]+J[3])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[3] = (+exp(+H[3]+0)+exp(+H[2]+H[3]+J[5])+exp(+H[1]+H[3]+J[4])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[4] = (+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[5] = (+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[6] = (+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[7] = (+exp(+H[1]+H[2]+J[3])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[8] = (+exp(+H[1]+H[3]+J[4])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z
	Cout[9] = (+exp(+H[2]+H[3]+J[5])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]))/Z

	return(Cout)

def p(params):
	"""
	Give each set of parameters concatenated into one array.
	"""
	Cout = zeros((10))
	H = params[0:4]
	J = params[4:10]
	H = params[0:4]
	J = params[4:10]
	Pout = zeros((16))
	Z = +exp(+0)+exp(+H[3]+0)+exp(+H[2]+0)+exp(+H[2]+H[3]+J[5])+exp(+H[1]+0)+exp(+H[1]+H[3]+J[4])+exp(+H[1]+H[2]+J[3])+exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])+exp(+H[0]+0)+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5])
	Pout[0] = +exp(+0)/Z
	Pout[1] = +exp(+H[3]+0)/Z
	Pout[2] = +exp(+H[2]+0)/Z
	Pout[3] = +exp(+H[2]+H[3]+J[5])/Z
	Pout[4] = +exp(+H[1]+0)/Z
	Pout[5] = +exp(+H[1]+H[3]+J[4])/Z
	Pout[6] = +exp(+H[1]+H[2]+J[3])/Z
	Pout[7] = +exp(+H[1]+H[2]+H[3]+J[3]+J[4]+J[5])/Z
	Pout[8] = +exp(+H[0]+0)/Z
	Pout[9] = +exp(+H[0]+H[3]+J[2])/Z
	Pout[10] = +exp(+H[0]+H[2]+J[1])/Z
	Pout[11] = +exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[5])/Z
	Pout[12] = +exp(+H[0]+H[1]+J[0])/Z
	Pout[13] = +exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[4])/Z
	Pout[14] = +exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[3])/Z
	Pout[15] = +exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5])/Z

	return(Pout)
