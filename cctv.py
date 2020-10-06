import numpy as np
import os
import pandas as pd
basedir =os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

class Cctv:
    def __init__(self):
        self.cctv = pd.read_csv(os.path.join(basedir,'model','data','cctv_in_seoul','cctv_in_seoul.csv'))
        print(self.cctv.head())
        print('----------------------')
        print(self.cctv.tail)
        print('----------------------')
        print(self.cctv.columns)

if __name__ == '__main__':
    t = Cctv()
    t.read_file()
    