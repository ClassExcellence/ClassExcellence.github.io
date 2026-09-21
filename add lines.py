def add_lines(mmatrix,l,a,b):
	for i in range(len(mmatrix[a-1])):
		mmatrix[a-1][i],mmatrix[b-1][i]=mmatrix[a-1][i],l*mmatrix[a-1][i]+mmatrix[b-1][i]
	return mmatrix
