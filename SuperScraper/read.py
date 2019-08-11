import jsonlines

comset=set()
with jsonlines.open('output/comics1.jl') as reader:
	for obj in reader:
		comset.update(obj['comics'])

print(comset)
print(len(comset))