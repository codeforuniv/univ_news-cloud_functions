import os
import glob
import pandas as pd
from datetime import datetime, date, timedelta

# collection_nameとscraping.pyの関数名が一致している必要がある
from university import *


if __name__ == '__main__':
    names = [os.path.split(os.path.splitext(file)[0])[1] for file in glob.glob(os.getcwd()+'/university/[a-zA-Z0-9]*.py')]
    # names.remove('AkitaInternational')  # 国際教養大がバグが起きているのでいったん除外
    instances = [eval(name + '.' + name + '()') for name in names]
