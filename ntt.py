import sys

if len(sys.argv) < 2:
	print 'YOU FAIL'
	sys.exit(0)

inname = sys.argv[1]
outname = inname + '.tex'

fin = open(inname,"r")
fout = open(outname,"w")

c = 0
lines = fin.read().split('\n')
fout.write("\\documentclass[12pt]{article}\n\\usepackage{fullpage}\n\\begin{document}\n\\begin{itemize}\n")
for line in lines:
	nc = 0
	while len(line) > 0 and line[0] == '\t':
		nc += 1
		line = line[1:]
	while c < nc:
		fout.write("\\begin{itemize}\n")
		c+=1
	while c > nc:
		fout.write("\\end{itemize}\n")
		c-=1
	if line != '':
		fout.write("\\item " + line + "\n")
fout.write("\\end{itemize}\n\\end{document}\n")
fin.close()
fout.close()
