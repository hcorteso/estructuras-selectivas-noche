# Estructura Simple
a = 33
b = 200

if b > a:
    print(b,"es mayor que ",a)

#Estructura Doble
if a > b:
    print(a,"es mayor que ",b)
else:
    print(a,"no es mayor que ",b)


# Codicion Multiple
if a > b:
    print(a,"es mayor que",b)
elif a < b:
    print(a,"es menor que",b)
else:
    print(a,"es igual que",b)

# Condicion enlazada
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("peo no por encima de 20.")



# Parametros end
print("Estudiar los sabados", end=" ")
print("es genial")

# Parametro sep
print("Daniela","Luis","Carlos","Camila")#agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")# quita el espacio
print("Daniela","Luis", "Carlos","Camila",sep=",")# agrega una coma

print("Daniela","Luis","Carlos","Camila",sep="_", end="_curso_python")# implementacion end y sep


