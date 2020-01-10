#JAN 10th 2020 T.I. fixed unwanted brackets issue
#JAN 10th 2020 T.I. GUI framework
#JAN 10th 2020 T.I. refactor
#JAN 10th 2020 T.I. modified output structure (RankedlineList1)
#JAN 9th  2020 T.I. created this file

import tkinter as tk

def generateAnsSheet():
    listget1=ansInput_entry.get("0.0", "end-1c").splitlines()
    lineList1 = [line.rstrip('\n') for line in listget1 if (line.startswith('Across') is False) and (line.startswith('Down') is False)]
    RankedlineList1=[None] * len(lineList1)
    for line in lineList1:
        ke=line[0]
        RankedlineList1[int(ke)-1]=line

    listget2=queInput_entry.get("0.0", "end-1c").splitlines()
    lineList2 = [line.rstrip('\n') for line in listget2]

    for lineidx in range(len(RankedlineList1)):
        line=RankedlineList1[lineidx]
        lineT=line[line.index(' '):]
        for line2 in lineList2:
            lineT2=line2[line2.index(' '):]
            if lineT2==lineT:
                lineListT=[line[:line.index('.')],line[line.index(' ')+1:],line2[:line2.index(' ')]]
                RankedlineList1[lineidx]=lineListT
    print (RankedlineList1)

    for [number,desc,title] in RankedlineList1:
        print(number,desc,title)
        listString=" ".join([number,desc,":",title,'\n'])
        ansSheetOutut_entry.insert(tk.END,listString)
    print([number,desc,title])
  

window = tk.Tk()

ansInput_entry = tk.Text(window)
ansInput_entry["width"] = 50
ansInput_entry["height"] = 10
ansInput_entry.pack(side=tk.LEFT)

queInput_entry = tk.Text(window)
queInput_entry["width"] = 50
queInput_entry["height"] = 10
queInput_entry.pack(side=tk.LEFT)

ansSheetOutut_entry = tk.Text(window)
ansSheetOutut_entry["width"] = 50
ansSheetOutut_entry["height"] = 10
ansSheetOutut_entry.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text='ANS Sheet', command=generateAnsSheet)
calculate_btn.pack()

window.mainloop()