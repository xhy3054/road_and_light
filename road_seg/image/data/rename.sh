# !/bin/bash

for (( i = 1; i < 28; i++ )); do
	#statements
	
	mv tr_${i}.jpg ${i}.jpg
done

for (( i = 1; i < 32; i++ )); do
	#statements

	mv te${i}.jpg $[i+27].jpg
done