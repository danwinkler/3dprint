w=99
h=50
d=10
p=8

def q(f):
	return (
		f()(
			cube([w,h,d]),
			translate([w-p-2,h-p-2,1])(
				cube([p,p,d*2])
			)
		)
	)

def r(f):
	o = q(f) + mirror(Red)(q(f))
	return o + mirror(Green)(o)

a=r(union)
p=15
b=forward(h*3)(
	r(difference)
)
o=[a,b]
