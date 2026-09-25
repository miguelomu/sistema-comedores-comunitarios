class Comedor:
    """Modelo para representar un comedor comunitario"""
    
    def __init__(self, nombre_comedor="", direccion="", capacidad=0, horario=""):
        self.nombre_comedor = nombre_comedor
        self.direccion = direccion
        self.capacidad = capacidad
        self.horario = horario  # Corregido el typo "horaio"
        
    def __str__(self):
        return f"{self.nombre_comedor} - {self.direccion}"


class Alimentos:
    """Modelo para manejar el inventario de alimentos"""
    
    def __init__(self, cereales_harinas=0, proteinas=0, verduras=0, frutas=0, bebidas_nutritivas=0):
        self.cereales_harinas = cereales_harinas
        self.proteinas = proteinas
        self.verduras = verduras
        self.frutas = frutas
        self.bebidas_nutritivas = bebidas_nutritivas
        self.platos_comida = 0
        self._actualizar_platos()
        
    def entrega_alimentos(self, cereales_harinas, proteinas, verduras, frutas, bebidas_nutritivas):
        """Agregar alimentos al inventario"""
        self.cereales_harinas += cereales_harinas
        self.proteinas += proteinas
        self.verduras += verduras
        self.frutas += frutas
        self.bebidas_nutritivas += bebidas_nutritivas
        self._actualizar_platos()
        
    def repartir_alimentos(self, cantidad_beneficiarios):
        """Repartir alimentos a beneficiarios"""
        if cantidad_beneficiarios <= 0:
            return False, "No hay beneficiarios para repartir"
            
        if cantidad_beneficiarios > self.platos_comida:
            return False, f"Hacen falta {cantidad_beneficiarios - self.platos_comida} platos de comida"
            
        # Cantidades por plato
        cereales_por_plato = 110
        proteinas_por_plato = 80
        verduras_por_plato = 70
        frutas_por_plato = 110
        bebidas_por_plato = 225
        
        # Descontar del inventario
        self.cereales_harinas -= cereales_por_plato * cantidad_beneficiarios
        self.proteinas -= proteinas_por_plato * cantidad_beneficiarios
        self.verduras -= verduras_por_plato * cantidad_beneficiarios
        self.frutas -= frutas_por_plato * cantidad_beneficiarios
        self.bebidas_nutritivas -= bebidas_por_plato * cantidad_beneficiarios
        
        self._actualizar_platos()
        return True, f"Se entregaron {cantidad_beneficiarios} platos de comida"
        
    def _actualizar_platos(self):
        """Calcular cuántos platos completos se pueden hacer"""
        porciones_cereal = self.cereales_harinas // 110
        porciones_proteinas = self.proteinas // 80
        porciones_verduras = self.verduras // 70
        porciones_frutas = self.frutas // 110
        porciones_bebidas = self.bebidas_nutritivas // 225
        
        self.platos_comida = min(porciones_cereal, porciones_proteinas, 
                                porciones_verduras, porciones_frutas, porciones_bebidas)


class Beneficiario:
    """Modelo para representar un beneficiario del comedor"""
    
    def __init__(self, nombre="", num_cedula="", edad=0, sexo="", estrato=0, 
                 discapacidad=False, puntaje_vulnerabilidad=0):
        self.nombre = nombre
        self.num_cedula = num_cedula
        self.edad = edad
        self.sexo = sexo
        self.estrato = estrato
        self.discapacidad = discapacidad
        self.puntaje_vulnerabilidad = puntaje_vulnerabilidad
        
    def calcular_puntaje_vulnerabilidad(self, comidas_diarias, sueldo_mensual, 
                                      personas_a_cargo, tiene_discapacidad, 
                                      tipo_vivienda, desplazamiento=False, 
                                      menores_a_cargo=False):
        """Calcular el puntaje de vulnerabilidad del beneficiario"""
        self.puntaje_vulnerabilidad = 0
        
        # Puntaje por comidas diarias
        if comidas_diarias == 1:
            self.puntaje_vulnerabilidad += 5
        elif comidas_diarias == 2:
            self.puntaje_vulnerabilidad += 3
        elif comidas_diarias == 3:
            self.puntaje_vulnerabilidad += 0
            
        # Puntaje por ingresos
        if personas_a_cargo > 0:
            ingreso_por_persona = sueldo_mensual / personas_a_cargo
        else:
            ingreso_por_persona = sueldo_mensual
            
        if ingreso_por_persona < 200000:
            self.puntaje_vulnerabilidad += 5
        elif ingreso_por_persona <= 300000:
            self.puntaje_vulnerabilidad += 3
        else:
            self.puntaje_vulnerabilidad += 0
            
        # Puntaje por discapacidad
        if tiene_discapacidad:
            self.puntaje_vulnerabilidad += 5
            
        # Puntaje por tipo de vivienda
        if tipo_vivienda == "calle":
            self.puntaje_vulnerabilidad += 5
        elif tipo_vivienda == "arriendo":
            self.puntaje_vulnerabilidad += 3
        elif tipo_vivienda == "propia":
            self.puntaje_vulnerabilidad += 0
            
        # Puntajes adicionales
        if desplazamiento:
            self.puntaje_vulnerabilidad += 5
        if menores_a_cargo:
            self.puntaje_vulnerabilidad += 5
            
        self.discapacidad = tiene_discapacidad
        return self.puntaje_vulnerabilidad
        
    def es_apto(self):
        """Determinar si el beneficiario es apto para recibir comida"""
        return self.puntaje_vulnerabilidad >= 15


class ComedorComunitario:
    """Modelo principal que combina comedor, alimentos y beneficiarios"""
    
    def __init__(self, comedor, alimentos=None):
        self.comedor = comedor
        self.alimentos = alimentos or Alimentos()
        self.beneficiarios = []
        
    def agregar_beneficiario(self, beneficiario):
        """Agregar un nuevo beneficiario"""
        if beneficiario not in self.beneficiarios:
            self.beneficiarios.append(beneficiario)
            return True
        return False
        
    def retirar_beneficiario(self, indice):
        """Retirar un beneficiario por índice"""
        if 0 <= indice < len(self.beneficiarios):
            beneficiario_retirado = self.beneficiarios.pop(indice)
            return True, beneficiario_retirado
        return False, None
        
    def obtener_beneficiario(self, indice):
        """Obtener un beneficiario por índice"""
        if 0 <= indice < len(self.beneficiarios):
            return self.beneficiarios[indice]
        return None