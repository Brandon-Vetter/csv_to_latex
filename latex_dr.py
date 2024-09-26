import argparse


def main():
    mk_latex_table(input("input file name: "), input("input output file: "))

def mk_latex_table(tb_nm, doc):
    #
    sheet = open(tb_nm, "r")
    tex_file = open(doc, "w")
    com_del_fil = []
    for line in sheet.readlines():
        com_del_fil.append(line.split(','))
    tex_file.write("\\begin{tabular}{" + "c|"*len(com_del_fil[0]) + "}\n")
    for row in com_del_fil:
        for col in row:
            if col.endswith('\n'):
                tex_file.write(col[0:len(col)-1] + " \\\\ \n")
                continue
            tex_file.write(col + " & ")
    tex_file.write("\\end{tabular}")
    sheet.close()
    tex_file.close()

main()