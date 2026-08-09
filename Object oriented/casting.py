A = 12

B = float(A)
print(type(B))
print(B)

C = bool(A)
print(type(C))
print(C)

D = str(A)
print(type(D))
print(D)

print("-----------------------")

E = [1,2,3,4,5]

F = tuple(E)
print(type(F))
print(F)

G = str(E)
print(type(G))
print(G)

H = set(E)
print(type(H))  
print(H)

print("-----------------------")

I = (1,2,3,4,5)

J = list(I)
print(type(J))
print(J)

K = set(I)
print(type(K))
print(K)

L = str(I)
print(type(L))  
print(L)

print("-----------------------")

M = {1,2,3,4,5}

N = list(M)
print(type(N))
print(N)

O = str(M)
print(type(O))
print(O)

P = list(M)
print(type(P))  
print(P)

Q = tuple(M)
print(type(Q))
print(Q)

R = {
    "name": "Nimal",
    "age": 20,
    "city": "Colombo"
}

S = list(R)
print(type(S))
print(S)

T = str(R)
print(type(T))
print(T)

U = tuple(R)
print(type(U))
print(U)

V = set(R)
print(type(V))
print(V)