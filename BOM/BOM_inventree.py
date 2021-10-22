import kicad_netlist_reader
import csv
import sys

net = kicad_netlist_reader.netlist(sys.argv[1])

try:
    f = open(sys.argv[2]+".csv", 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, sys.stderr)
    f = sys.stdout
    
out = csv.writer(f, lineterminator='\n', delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

out.writerow([
	'part_id',
	'part_ipn',
	'part_name',
	'quantity',
	'optional',
	'overage',
	'Reference',
	'note',
	'inherited',
	'allow_varients',
	'Value',
	'ref',
	])
	
grouped = net.groupComponents()

# Output all of the component information
row = []
for group in grouped:#
    del row[:]
    refs = ""

    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    for component in group:
        if len(refs) > 0:
            refs += ", "
        refs += component.getRef()
        c = component
        
    row.append(c.getField("part_id"))
    row.append(c.getField("part_ipn"))
    row.append(c.getField("MFG ID"))
    row.append(c.getField("quantity"))
    row.append(c.getField("optional"))
    row.append(c.getField("overage"))
    row.append(refs)
    row.append(c.getField("note"))
    row.append(c.getField("inherited"))
    row.append(c.getField("allow_varients"))
    row.append(c.getField("Value"))
    
    out.writerow(row)

f.close()
		


