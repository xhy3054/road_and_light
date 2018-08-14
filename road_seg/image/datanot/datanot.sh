# !/bin/bash



for (( i = 1; i < 33; i++ )); do
	#statements

	cp ~/Pictures/image/testnot/${i}.png ~/Pictures/image/datanot/$[i+27].png
done