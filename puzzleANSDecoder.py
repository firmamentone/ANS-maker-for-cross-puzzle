
#JAN 10th 2020 T.I. modified output structure (RankedlineList1)
#JAN 9th  2020 T.I. created this file

fileName="inputSample1.txt"
lineList1 = [line.rstrip('\n') for line in open(fileName) if (line.startswith('Across') is False) and (line.startswith('Down') is False)]
RankedlineList1=[None] * len(lineList1)

for line in lineList1:
    ke=line[0]
    RankedlineList1[int(ke)-1]=line
 
fileName="inputANS1.txt"
lineList2 = [line.rstrip('\n') for line in open(fileName)]

idx=0
for line in RankedlineList1:
    lineT=line[line.index(' '):]
    for line2 in lineList2:
        lineT2=line2[line2.index(' '):]
        if lineT2==lineT:
            lineListT=[line[:line.index('.')],line[line.index(' ')+1:],line2[:line2.index(' ')]]
            RankedlineList1[idx]=lineListT
    idx=idx+1
print (RankedlineList1)
