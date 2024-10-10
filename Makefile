gentests:
	gcc -o tests/generate_rand48_conformance_data tests/generate_rand48_conformance_data.c
	tests/generate_rand48_conformance_data > tests/data/rand48_conformance_data.json
