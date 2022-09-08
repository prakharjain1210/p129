import csv
d1=[]
d2=[]
with open("bright_stars.csv","r",encoding='utf8') as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d1.append(i)
with open("unit_converted_stars.csv","r",encoding='utf8') as f:
    csv_reader=csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1=d1[0]
h2=d2[0]
h=h1+h2

p1=d1[1:]
p2=d2[1:]

p=[]
for i in p1:
    p.append(i)

for i in p2:
    p.append(i)

with open("new.csv","w",encoding='utf8') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p)