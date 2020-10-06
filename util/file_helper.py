from dataclasses import dataclass
import os
import pandas as pd
import xlrd
import googlemaps
'''
pandas version 1.x 이상 encoding='UTF-8' 불필요
ImportError: Missing optional dependency
'''

@dataclass
class FileReader:

    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''

    def new_file(self) -> str:
        return os.path.join(self.context,self.fname)

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        print(f'PANDAS VERSION: {pd.__version__}')
        return pd.read_excel(self.new_file(), header = header, usecols = usecols)

    def create_gmpas(self):
        return googlemaps.Client(key='') # 구글에서 발급받은 키 넣으면 됨