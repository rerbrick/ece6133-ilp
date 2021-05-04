# ece6133-ilp
ILP floor planning

Note: Must be run on a Windows machine.

1. Navigate to the ece6133-ilp directory in a terminal.
2. Run command "pip install lpsolve55-5.5.2.5-cp39-cp39-win_amd64.whl"
3. Verify that lpsolve55 has installed successfully.
4. To run the program, call "py main.py <benchmark_file>"
	Ex: py main.py 5_block
	Note: The benchmark file must be located in the "benchmarks" directory.
5. The program will ask if you want to solve for overestimation or
	underestimation. Type 'o' for overestimation and 'u' for underestimation
	and hit Enter.
6. The program will run and print areas of each floorplan, print the total 
	runtime to produce the solution, and plot the final floorplan.