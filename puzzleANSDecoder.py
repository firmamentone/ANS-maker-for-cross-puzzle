#JAN 11th 2020 T.I. refactor
#JAN 11th 2020 T.I. fixed "string ends with empty" problem
#JAN 10th 2020 T.I. fixed unwanted brackets problem
#JAN 10th 2020 T.I. GUI framework
#JAN 10th 2020 T.I. refactor
#JAN 10th 2020 T.I. modified output structure (RankedlineList1)
#JAN 9th  2020 T.I. created this file

import tkinter as tk

def generateAnsSheet():
    listget1=quesInput_text.get("1.0", "end-1c").splitlines()
   
    lineList1 = [line.rstrip(' \n') for line in listget1 if (line.startswith('Across') is False) and (line.startswith('Down') is False)]
    RankedlineList1=[None] * len(lineList1)
    for line in lineList1:
        ke=line[:line.index('.')]
        RankedlineList1[int(ke)-1]=line

    listget2=descripInput_text.get("1.0", "end-1c").splitlines()
    lineList2 = [line.rstrip(' \n') for line in listget2]

    for lineidx in range(len(RankedlineList1)):
        line=RankedlineList1[lineidx]
        lineT=line[line.index(' '):]
        for line2 in lineList2:
            lineT2=line2[line2.index(' '):]
            if lineT2==lineT:
                lineListT=[line[:line.index('.')],line[line.index(' ')+1:],line2[:line2.index(' ')]]
                RankedlineList1[lineidx]=lineListT

    for [number,desc,title] in RankedlineList1:
        listString=" ".join([number,desc,":",title,'\n'])
        ansSheetOutput_text.insert("end",listString)
  

window = tk.Tk()

quesInput_text = tk.Text(window)
quesInput_text["width"] = 100
quesInput_text["height"] = 10
quesInput_text.pack()

descripInput_text = tk.Text(window)
descripInput_text["width"] = 100
descripInput_text["height"] = 10
descripInput_text.pack()

ansSheetOutput_text = tk.Text(window)
ansSheetOutput_text["width"] = 100
ansSheetOutput_text["height"] = 10
ansSheetOutput_text.pack()

anssheetGEN_btn = tk.Button(window, text='ANS Sheet', command=generateAnsSheet)
anssheetGEN_btn.pack()

window.mainloop()