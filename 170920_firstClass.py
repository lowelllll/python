line = "Good,100,490,10"
field_types = [str,int,float]
raw_fields = line.split(",")
field = [ty(val) for ty,val in zip(field_types,raw_fields)]
print field