from models import Comedor, Alimentos, Beneficiario, ComedorComunitario
from views import ComedorView

class ComedorController:
    """Controlador principal del sistema de comedores comunitarios"""
    
    def __init__(self):
        self.view = ComedorView()
        self.comedores_comunitarios = self._inicializar_comedores()
        
    def _inicializar_comedores(self):
        """Inicializar los datos de los comedores comunitarios"""
        comedores_data = [
            ("Los luceros", "Cra 17F No. 69A-32 Sur (Lucero Sur)", 250, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("Potosí", "Calle 81 Sur No. 42-09", 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Caracolí", "Calle 76A Sur No. 74B-05", 220, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("La Estrella", "Cra 18 No. 74A Sur-87", 240, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("Bella Flor - La Torre", "Cra 27 No. 75A-50 Sur", 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Altos de la Cruz", "Transv 22 No. 69K-19 Sur", 225, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Juan Pablo II", "Diag 68B Sur No. 18P-40", 220, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("Naciones Unidas", "Cra 18R No. 77A Sur-27", 235, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("Jerusalén Canteras", "Cra 47D No. 68G-08 Sur", 250, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Estrella del Sur", "Calle 74 No. 18 Bis-18", 230, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("Santa Viviana", "Calle 75D Sur No. 75C-03 Sur", 220, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Arborizadora", "Cra 40 No. 63I-25 Sur", 230, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Perdomo", "Av. Villavicencio No. 60B-05 Sur", 240, "Lun a sáb, 10:30 a.m. - 3:00 p.m."),
            ("El Tesoro", "Cra 18F No. 76 Sur", 225, "Lun a sáb, 11:00 a.m. - 2:30 p.m."),
            ("Vista Hermosa", "Calle 80B Sur No. 44-10", 230, "Lun a sáb, 10:30 a.m. - 3:00 p.m.")
        ]
        
        comedores = []
        for nombre, direccion, capacidad, horario in comedores_data:
            comedor = Comedor(nombre, direccion, capacidad, horario)
            alimentos = Alimentos()
            comedor_comunitario = ComedorComunitario(comedor, alimentos)
            comedores.append(comedor_comunitario)
            
        return comedores
        
    def ejecutar(self):
        """Método principal para ejecutar la aplicación"""
        while True:
            self.view.mostrar_menu_principal(self.comedores_comunitarios)
            opcion = self.view.leer_entero("Escriba el número perteneciente al comedor: ", 1, len(self.comedores_comunitarios) + 1)
            
            if opcion == len(self.comedores_comunitarios) + 1:
                self.view.mostrar_mensaje("Saliendo...")
                break
                
            comedor_seleccionado = self.comedores_comunitarios[opcion - 1]
            self._gestionar_comedor(comedor_seleccionado)
            
    def _gestionar_comedor(self, comedor_comunitario):
        """Gestionar las operaciones de un comedor específico"""
        while True:
            self.view.mostrar_menu_comedor(comedor_comunitario.comedor.nombre_comedor)
            opcion = self.view.leer_entero("Escoja una opción: ", 1, 7)
            
            if opcion == 1:
                self._mostrar_inventario(comedor_comunitario)
            elif opcion == 2:
                self._entregar_alimentos(comedor_comunitario)
            elif opcion == 3:
                self._repartir_comida(comedor_comunitario)
            elif opcion == 4:
                self._mostrar_beneficiarios(comedor_comunitario)
            elif opcion == 5:
                self._agregar_beneficiario(comedor_comunitario)
            elif opcion == 6:
                self._retirar_beneficiario(comedor_comunitario)
            elif opcion == 7:
                self.view.mostrar_mensaje("Saliendo...")
                break
                
    def _mostrar_inventario(self, comedor_comunitario):
        """Mostrar el inventario actual del comedor"""
        self.view.mostrar_inventario(comedor_comunitario.alimentos)
        
    def _entregar_alimentos(self, comedor_comunitario):
        """Simular la entrega de alimentos al comedor"""
        # Cantidades fijas como en el código original
        cereales = 552
        proteinas = 558
        verduras = 765
        frutas = 240
        bebidas = 865
        
        comedor_comunitario.alimentos.entrega_alimentos(cereales, proteinas, verduras, frutas, bebidas)
        self.view.mostrar_mensaje("Al restaurante le acaba de llegar una carga de comida")
        
    def _repartir_comida(self, comedor_comunitario):
        """Repartir comida a los beneficiarios"""
        cantidad_beneficiarios = len(comedor_comunitario.beneficiarios)
        
        if cantidad_beneficiarios == 0:
            self.view.mostrar_mensaje("Este comedor aún no tiene beneficiarios.")
            return
            
        exito, mensaje = comedor_comunitario.alimentos.repartir_alimentos(cantidad_beneficiarios)
        self.view.mostrar_mensaje(mensaje)
        
    def _mostrar_beneficiarios(self, comedor_comunitario):
        """Mostrar y consultar beneficiarios"""
        tiene_beneficiarios = self.view.mostrar_beneficiarios(
            comedor_comunitario.beneficiarios, 
            comedor_comunitario.comedor.nombre_comedor
        )
        
        if tiene_beneficiarios:
            indice = self.view.leer_entero(
                "Digite el número correspondiente al beneficiario a consultar: ", 
                1, len(comedor_comunitario.beneficiarios)
            ) - 1
            
            beneficiario = comedor_comunitario.obtener_beneficiario(indice)
            if beneficiario:
                self.view.mostrar_detalle_beneficiario(beneficiario)
            else:
                self.view.mostrar_error("Número de beneficiario no válido")
                
    def _agregar_beneficiario(self, comedor_comunitario):
        """Agregar un nuevo beneficiario al comedor"""
        nombre, num_cedula, edad, sexo, estrato = self.view.solicitar_datos_beneficiario()
        
        # Crear beneficiario temporal
        beneficiario = Beneficiario(nombre, num_cedula, edad, sexo, estrato)
        
        # Obtener datos para calcular vulnerabilidad
        comidas, sueldo, personas_cargo, discapacidad, vivienda = self.view.solicitar_datos_vulnerabilidad(edad)
        
        # Calcular puntaje inicial
        puntaje = beneficiario.calcular_puntaje_vulnerabilidad(
            comidas, sueldo, personas_cargo, discapacidad, vivienda
        )
        
        # Verificar si necesita datos adicionales
        if 10 <= puntaje < 15:
            desplazamiento, menores_cargo = self.view.solicitar_datos_adicionales()
            puntaje = beneficiario.calcular_puntaje_vulnerabilidad(
                comidas, sueldo, personas_cargo, discapacidad, vivienda, 
                desplazamiento, menores_cargo
            )
        
        # Determinar si es apto
        if beneficiario.es_apto():
            comedor_comunitario.agregar_beneficiario(beneficiario)
            self.view.mostrar_mensaje(f"Beneficiario {nombre} inscrito con éxito")
        else:
            self.view.mostrar_mensaje(f"El beneficiario {nombre} NO es apto para recibir comida en este comedor comunitario")
            
    def _retirar_beneficiario(self, comedor_comunitario):
        """Retirar un beneficiario del comedor"""
        tiene_beneficiarios = self.view.mostrar_beneficiarios(
            comedor_comunitario.beneficiarios, 
            comedor_comunitario.comedor.nombre_comedor
        )
        
        if tiene_beneficiarios:
            indice = self.view.leer_entero(
                "Digite el número correspondiente al beneficiario que desea retirar: ", 
                1, len(comedor_comunitario.beneficiarios)
            ) - 1
            
            exito, beneficiario_retirado = comedor_comunitario.retirar_beneficiario(indice)
            if exito:
                self.view.mostrar_mensaje("Beneficiario retirado con éxito")
            else:
                self.view.mostrar_error("No se pudo retirar el beneficiario")