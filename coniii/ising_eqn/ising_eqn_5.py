# Equations of 5-spin Ising model.

# 30/12/2017
from numpy import zeros, exp

def calc_observables(params):
	"""
	Give each set of parameters concatenated into one array.
	"""
	Cout = zeros((15))
	H = params[0:5]
	J = params[5:15]
	Z = +exp(+0)+exp(+H[4]+0)+exp(+H[3]+0)+exp(+H[3]+H[4]+J[9])+exp(+H[2]+0)+exp(+H[2]+H[4]+J[8])+exp(+H[2]+H[3]+J[7])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+0)+exp(+H[1]+H[4]+J[6])+exp(+H[1]+H[3]+J[5])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+J[4])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+0)+exp(+H[0]+H[4]+J[3])+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])
	Cout[0] = (+exp(+H[0]+0)+exp(+H[0]+H[4]+J[3])+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[1] = (+exp(+H[1]+0)+exp(+H[1]+H[4]+J[6])+exp(+H[1]+H[3]+J[5])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+J[4])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[2] = (+exp(+H[2]+0)+exp(+H[2]+H[4]+J[8])+exp(+H[2]+H[3]+J[7])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[2]+J[4])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[3] = (+exp(+H[3]+0)+exp(+H[3]+H[4]+J[9])+exp(+H[2]+H[3]+J[7])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[3]+J[5])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[4] = (+exp(+H[4]+0)+exp(+H[3]+H[4]+J[9])+exp(+H[2]+H[4]+J[8])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[4]+J[6])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[4]+J[3])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[5] = (+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[6] = (+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[7] = (+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[8] = (+exp(+H[0]+H[4]+J[3])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[9] = (+exp(+H[1]+H[2]+J[4])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[10] = (+exp(+H[1]+H[3]+J[5])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[11] = (+exp(+H[1]+H[4]+J[6])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[12] = (+exp(+H[2]+H[3]+J[7])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[13] = (+exp(+H[2]+H[4]+J[8])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z
	Cout[14] = (+exp(+H[3]+H[4]+J[9])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9]))/Z

	return(Cout)

def p(params):
	"""
	Give each set of parameters concatenated into one array.
	"""
	Cout = zeros((15))
	H = params[0:5]
	J = params[5:15]
	H = params[0:5]
	J = params[5:15]
	Pout = zeros((32))
	Z = +exp(+0)+exp(+H[4]+0)+exp(+H[3]+0)+exp(+H[3]+H[4]+J[9])+exp(+H[2]+0)+exp(+H[2]+H[4]+J[8])+exp(+H[2]+H[3]+J[7])+exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])+exp(+H[1]+0)+exp(+H[1]+H[4]+J[6])+exp(+H[1]+H[3]+J[5])+exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])+exp(+H[1]+H[2]+J[4])+exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])+exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])+exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])+exp(+H[0]+0)+exp(+H[0]+H[4]+J[3])+exp(+H[0]+H[3]+J[2])+exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])+exp(+H[0]+H[2]+J[1])+exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])+exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])+exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])+exp(+H[0]+H[1]+J[0])+exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])+exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])+exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])+exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])+exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])+exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])+exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])
	Pout[0] = +exp(+0)/Z
	Pout[1] = +exp(+H[4]+0)/Z
	Pout[2] = +exp(+H[3]+0)/Z
	Pout[3] = +exp(+H[3]+H[4]+J[9])/Z
	Pout[4] = +exp(+H[2]+0)/Z
	Pout[5] = +exp(+H[2]+H[4]+J[8])/Z
	Pout[6] = +exp(+H[2]+H[3]+J[7])/Z
	Pout[7] = +exp(+H[2]+H[3]+H[4]+J[7]+J[8]+J[9])/Z
	Pout[8] = +exp(+H[1]+0)/Z
	Pout[9] = +exp(+H[1]+H[4]+J[6])/Z
	Pout[10] = +exp(+H[1]+H[3]+J[5])/Z
	Pout[11] = +exp(+H[1]+H[3]+H[4]+J[5]+J[6]+J[9])/Z
	Pout[12] = +exp(+H[1]+H[2]+J[4])/Z
	Pout[13] = +exp(+H[1]+H[2]+H[4]+J[4]+J[6]+J[8])/Z
	Pout[14] = +exp(+H[1]+H[2]+H[3]+J[4]+J[5]+J[7])/Z
	Pout[15] = +exp(+H[1]+H[2]+H[3]+H[4]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])/Z
	Pout[16] = +exp(+H[0]+0)/Z
	Pout[17] = +exp(+H[0]+H[4]+J[3])/Z
	Pout[18] = +exp(+H[0]+H[3]+J[2])/Z
	Pout[19] = +exp(+H[0]+H[3]+H[4]+J[2]+J[3]+J[9])/Z
	Pout[20] = +exp(+H[0]+H[2]+J[1])/Z
	Pout[21] = +exp(+H[0]+H[2]+H[4]+J[1]+J[3]+J[8])/Z
	Pout[22] = +exp(+H[0]+H[2]+H[3]+J[1]+J[2]+J[7])/Z
	Pout[23] = +exp(+H[0]+H[2]+H[3]+H[4]+J[1]+J[2]+J[3]+J[7]+J[8]+J[9])/Z
	Pout[24] = +exp(+H[0]+H[1]+J[0])/Z
	Pout[25] = +exp(+H[0]+H[1]+H[4]+J[0]+J[3]+J[6])/Z
	Pout[26] = +exp(+H[0]+H[1]+H[3]+J[0]+J[2]+J[5])/Z
	Pout[27] = +exp(+H[0]+H[1]+H[3]+H[4]+J[0]+J[2]+J[3]+J[5]+J[6]+J[9])/Z
	Pout[28] = +exp(+H[0]+H[1]+H[2]+J[0]+J[1]+J[4])/Z
	Pout[29] = +exp(+H[0]+H[1]+H[2]+H[4]+J[0]+J[1]+J[3]+J[4]+J[6]+J[8])/Z
	Pout[30] = +exp(+H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[4]+J[5]+J[7])/Z
	Pout[31] = +exp(+H[0]+H[1]+H[2]+H[3]+H[4]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5]+J[6]+J[7]+J[8]+J[9])/Z

	return(Pout)
