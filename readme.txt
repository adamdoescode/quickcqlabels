*** quickcqlabels ***

What this does: 
This script will combine a formatted 384 well pcr plan with the Cq value output from a BioRad CFX run xlsx file.

What it does NOT do: 
It does no calculations or statistics on your Cq values. Nor does it tell you if those Cq values are real 
i.e. it doesn't look at the corresponding melt curves. Maybe sometime in the future it will do all of these things.

Installation:
Simply download the .py file to an appropiate directory. Make sure you have the dependencies, listed below, 
installed.

Dependencies:
Python 3.5
Pandas 0.23
xlrd (on linux, shouldn't be required on Windows)

How to Use:

First you need to format your 384 well PCR plan to match the format used in the sample plan. The sample plan is
provided on the github page along with the .py script.

Place the quickcqlabels.py script in the same folder as your cq.xlsx file from the CFX manager, and your PCR plan.
Run the script by typing the following, make sure to include the file extension:

>python quickcqlabels.py samplecq.xlsx sampleplan.xlsx

or you can type:

>python quickcqlabels.py samplecq.xlsx sampleplan.xlsx myoutput.csv

The first command will output your data to a file named "combined.csv" while the second includes an optional 
argument that changes the name of the output file to "myoutput.csv".

Whatever the name of the output file, it should contain the labels from your plan next to the Cq value for that 
label.
