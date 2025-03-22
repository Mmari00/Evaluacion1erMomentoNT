import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crear diccionario vacío
estudiantes = {}
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
for i in range(3):
    nombre = input("Ingresa el nombre del estudiante (4 letras o menos): ")
    nota = float(input(f"Ingresa la nota de {nombre}: "))
    # Guarda cada par nombre-nota en el diccionario
    estudiantes[nombre] = nota


# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active


# PARTE 3: Escribir encabezado
# Escribe "Nombres cortos (<=4 letras)" en A1
hoja['A1'] = "Nombres cortos, con 4 letras o menos (<=4 letras)."


# PARTE 4: Escribir nombres cortos con ciclo y condicional
fila = 2
# Usa un ciclo for para recorrer el diccionario
for nombre, nota in estudiantes.items():
    # Si el nombre tiene 4 letras o menos
    if len(nombre) <= 4:
        hoja[f'A{fila}'] = nombre
        fila += 1



# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio4.xlsx"
libro.save("ejercicio4.xlsx")
print("¡Ejercicio 4 guardado en ejercicio4.xlsx!")