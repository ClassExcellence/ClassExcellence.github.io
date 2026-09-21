def scal_line(mmatrix,scal,line):
	for i in range(len(mmatrix[line-1])):
		mmatrix[line-1][i]=scal*mmatrix[line-1][i]
	return mmatrix
