m=mirror;t=translate;s=scale;c=cube;h=-0.5
l=lambda x: s(x)(t([h,h])(c()))
def q(f,a):
	o=f()(c([9,9,2]), t([8,8,h])(l(a)))
	o+=m(Red)(o)
	o+=m(Green)(o)
	return s([-h,1.5,1])(o)

o=[
	q(union,1),
	t([20,0])(q(difference,1.2))
]
