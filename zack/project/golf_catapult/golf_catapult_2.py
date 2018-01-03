c=cube
a=lambda x: distribute_in_grid([c(x)]*4, (6))
o=[
	translate([-1,-1,-2])(c([9,9,2])) + a(1),
	right(10)(translate([-1,-1,-2])(c([9,9,2])) - a(2)),
]
# o=scale([2,0.5,1])(o)