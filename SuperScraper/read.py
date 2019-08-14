import jsonlines

comset=set()
ordset=set()
with jsonlines.open('output/comics1.jl') as reader:
	for obj in reader:
		comset.update(obj['comics'])

with jsonlines.open('output/orders.jl') as reader:
	for obj in reader:
		ordset.update(obj['order'])

print("Available :" + str(comset))
print("Total Avilable: " + str(len(comset)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Bought: " + str(ordset))
print("Total Bought: " + str(len(ordset)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Available Unbought: " + str(comset.difference(ordset)))
print("Total: " + str(len(comset.difference(ordset))))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("UnAvailable Bought: " + str(ordset.difference(comset)))
print("Total: " + str(len(ordset.difference(comset))))