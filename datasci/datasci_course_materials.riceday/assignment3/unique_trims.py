import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    _, s = record
    mr.emit_intermediate(s[:-10], True)

def reducer(key, values):
    mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
