import numpy as np
import pandas as pd
from resourse import *
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

def find_norm(name_rsrc, NORMS_GSP):
    df = pd.read_excel(NORMS_GSP)
    print(1)


def proc_exel(All_RESOURCES, GSP_2DKS, NORMS_GSP):
    df = pd.read_excel(All_RESOURCES)
    df = df.drop(0)
    unique_rsrc = df['name_rsrc'].unique() #all names af unique resourses
    for un_rsrc in range(len(unique_rsrc)):
        one_rsrc = df['name_rsrc'] == df['name_rsrc'][un_rsrc+1]
        all_rows_one_rsrc = one_rsrc.index[one_rsrc]
        for r in all_rows_one_rsrc:
            l = df.iloc[[r-1]]
            k = Resource(l)

            find_norm(str(k.name_rsrc.values[0]), NORMS_GSP)










