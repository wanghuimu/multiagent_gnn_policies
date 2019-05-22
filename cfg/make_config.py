import itertools

out_fname = 'vel2.cfg'

out_file = open(out_fname, "w")

with open("default.cfg") as f:
    for line in f:
        out_file.write(line) 

out_file.write('\n')	

params = {}
params['k'] = [1,2,3,4]
params['seed'] = range(10)
params['v_max'] = [0.5, 1.5, 2.5, 3.5]
#params['comm_radius'] = [3.0, 2.0, 1.5, 1.0]

param_names = params.keys()
param_values = params.values()

line = ''
for name in param_names:
	line = line + name + ', '
out_file.write('header = ' + line + 'reward' '\n\n')

for element in itertools.product(*param_values):
	line = '['
	for v in element:
		line = line + str(v) + ', '
	line = line[0:-2] + ']'
	out_file.write(line + '\n')

	for i in range(len(param_names)):
		line = param_names[i] + ' = ' + str(element[i])
		out_file.write(line+ '\n')

	out_file.write('\n')	 

out_file.close()

