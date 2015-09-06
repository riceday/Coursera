import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    rec_id = record[1]
    mr.emit_intermediate(rec_id, record)

def reducer(key, values):
    orders = filter(lambda v: v[0] == 'order', values)
    items = filter(lambda v: v[0] == 'line_item', values)
    for o in orders:
        for i in items:
            mr.emit(o + i)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
