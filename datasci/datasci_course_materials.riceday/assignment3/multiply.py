import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    matrix, i, j, value = record
    if matrix == 'a':
        # a(1, 2) will be needed by axb(1, 0), (1, 1), .. (1, 4)
        for _j in xrange(5):
            mr.emit_intermediate((i, _j), (matrix, i, j, value))
    else:
        # b(1, 2) will be needed by bxa(0, 2), (1, 2), .. (4, 2)
        for _i in xrange(5):
            mr.emit_intermediate((_i, j), (matrix, i, j, value))

def reducer(key, values):
    a_items = filter(lambda v: v[0] == 'a', values)
    b_items = filter(lambda v: v[0] == 'b', values)

    v = 0
    for _, a_i, a_j, a in a_items:
        for _, b_i, b_j, b in b_items:
            if a_j == b_i: v += a * b

    mr.emit(key + (v,))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
