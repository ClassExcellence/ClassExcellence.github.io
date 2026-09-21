def swap_line(mmatrix,i,j):
		mmatrix[i-1],mmatrix[j-1]=mmatrix[j-1],mmatrix[i-1]
		return mmatrix