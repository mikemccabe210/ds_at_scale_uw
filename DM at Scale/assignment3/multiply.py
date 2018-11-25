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


    a = [0,1,2,3,4]
    for i in a:
        if record[0]=='a':
            mr.emit_intermediate((record[1], i),record)
        else:
            mr.emit_intermediate((i,record[2]),record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total=0
    print key,list_of_values
    for aval in list_of_values:
        prod=0
        if aval[0]=='a':
            for bval in list_of_values:
                if bval[0]=='b' and aval[2]==bval[1]:
                    total +=aval[3]*bval[3]

    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
