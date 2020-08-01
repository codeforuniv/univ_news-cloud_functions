import os, glob

# モジュールが追加されたときに自動でfrom university import *で全て持ってくる
__all__ = [
    os.path.split(os.path.splitext(file)[0])[1]
    for file in glob.glob(os.path.join(os.path.dirname(__file__), '[a-zA-Z0-9]*.py'))
]

# 国際教養大がバグが起きているのでいったん除外
__all__.remove('AkitaInternational')