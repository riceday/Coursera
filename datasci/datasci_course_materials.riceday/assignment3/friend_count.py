import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    p, _ = record
    mr.emit_intermediate(p, True)

def reducer(key, values):
    mr.emit((key, len(values)))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
