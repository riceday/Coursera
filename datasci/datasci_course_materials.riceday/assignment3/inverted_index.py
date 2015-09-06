import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    docid, text = record
    for word in text.split():
        mr.emit_intermediate(word, docid)

def reducer(key, values):
    mr.emit((key, list(set(values))))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
