import os

pathlist = ['./preprocessing',
	    './preprocessing/resources',
	    './preprocessing/resources/JS2',
	    './preprocessing/resources/ATK',
	    './preprocessing/resources/PIS',
	    './level',
	    './level/resources',
	    './level/resources/inputs',
	    './level/resources/inputs/JS2/L2',
	    './level/resources/inputs/ATK/L2',
	    './level/resources/inputs/PIS/L2',
	    './level/resources/outputs']

for path in pathlist
	if not os.path.exists(path):
		os.makedirs(path)
