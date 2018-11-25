import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    record.sort()
    key = record[0]+record[1]
    value = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    print key
    if len(list_of_values)<2:
        tup = tuple(list_of_values[0])
        tupp = (list_of_values[0][1],list_of_values[0][0])
        mr.emit(tup)
        mr.emit(tupp)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
