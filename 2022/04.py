file = open("input.txt", 'r').read()
file = file.split("\n")
file.remove('')

fully_overlap = 0
contains=0
for i,row in enumerate(file):
    r1o,r2o = row.split(',')
    rs,rf = r1o.split('-')
    r1 = set([x for x in range(int(rs),int(rf)+1)])
    rs,rf = r2o.split('-')
    r2 = set([x for x in range(int(rs),int(rf)+1)])
    inters = r1.intersection(r2)
    if len(inters)==len(r1) or len(inters)==len(r2):
        print(r1o,r2o)
        print (inters)
        fully_overlap+=1
        print()
    if len(inters)>0:
        contains+=1

print(fully_overlap)
print(contains)
