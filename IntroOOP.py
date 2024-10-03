class Persona:
    def __init__(self, nombre, edad, genero, ciudad, ocupacion):
        self.nombre = nombre      # Nombre de la persona
        self.edad = edad          # Edad de la persona
        self.genero = genero      # Género de la persona
        self.ciudad = ciudad      # Ciudad de residencia
        self.ocupacion = ocupacion # Ocupación de la persona

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, "
                f"Ciudad: {self.ciudad}, Ocupación: {self.ocupacion}")

    #Pasar saludo
    def saludarA(self, nombreOtraPersona):
        return f"Hola", {self.nombre}, f"te manda a saludar {nombreOtraPersona}"

# Crear una instancia de la clase Persona
persona1 = Persona("Brenda", 21, "Femenino", "Madrid", "Ingeniera")
persona2 = Persona(nombre="Juan", edad=19, genero="Masculino", ciudad="Pachuca", ocupacion="Estudiante")
persona3 = Persona(nombre="Victor", edad=10, genero="Masculino", ciudad="Pachuca", ocupacion="Docente")

print(persona1.saludarA(persona2.nombre))

# Imprimir la información de la persona
print(persona1)
print(persona2)
print(persona3)
