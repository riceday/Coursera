import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    p, f = record
    key = (p, f) if p < f else (f, p)
    mr.emit_intermediate((key), True)

def reducer(key, values):
    if len(values) == 1:
        p, f = key
        mr.emit((p, f))
        mr.emit((f, p))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
