a="hello";#string
b=20;#int
c=10.45;#float


d=3+7j;#complex
#here 7 is real part and 7 is imaginary
# print(d.real);
# print(d.imag);


e=["a","b",7];# list 
# print(e[0]);
# print(e);


f=(1,3,5);#tuple
# print(f);
# print(f[0]);


g=range(1,10,2);#range(start(optional),end(required),diff(optional))
# print(range);



# 1) Only stop
print(list(range(5)))   # [0, 1, 2, 3, 4]

# 2) Start and stop
print(list(range(2, 8)))  # [2, 3, 4, 5, 6, 7]

# 3) With step
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]

# 4) Negative step (reverse)
print(list(range(10, 2, -2)))  # [10, 8, 6, 4]
