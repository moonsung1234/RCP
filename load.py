
import sys

def init(path) :
    if not path in sys.path : 
        sys.path.append(path)