class ComedorView:
    """Vista para mostrar información y solicitar datos del usuario"""
    
    def mostrar_menu_principal(self, comedores):
        """Mostrar el menú principal de selección de comedores"""
        print("\nEN CUAL COMEDOR DESEA TRABAJAR")
        print("-------------------------")
        for i, comedor in enumerate(comedores, 1):
            print(f"{i}. {comedor.comedor}")
        print(f"{len(comedores) + 1}. Salir del programa")
        print("-------------------------")
        
    def mostrar_menu_comedor(self, nombre_comedor):
        """Mostrar el menú de opciones para un comedor específico"""
        print(f"\nOPCIONES COMEDOR COMUNITARIO ({nombre_comedor})")
        print("-------------------------")
        print("1. Inventario de Comida")
        print("2. Entrega de Comida")
        print("3. Repartir comida")
        print("4. Beneficiarios inscritos")
        print("5. Añadir beneficiario")
        print("6. Retirar Beneficiario")
        print("7. Salir, escoger otro comedor")
        print("-------------------------")
        
    def mostrar_inventario(self, alimentos):
        """Mostrar el inventario actual de alimentos"""
        print("\nCOMIDA ACTUAL:")
        print("-----------------")
        print(f"{alimentos.cereales_harinas}g en cereales y harinas")
        print(f"{alimentos.proteinas}g en proteínas")
        print(f"{alimentos.verduras}g en verduras")
        print(f"{alimentos.frutas}g en frutas")
        print(f"{alimentos.bebidas_nutritivas}g en bebidas nutritivas")
        print(f"Este comedor cuenta con {alimentos.platos_comida} platos de comida disponibles")
        print("-----------------")
        
    def mostrar_beneficiarios(self, beneficiarios, nombre_comedor):
        """Mostrar lista de beneficiarios"""
        print(f"\nBeneficiarios inscritos en el comedor {nombre_comedor}")
        print("-----------------")
        if not beneficiarios:
            print("Este comedor aún no tiene beneficiarios.")
            return False
            
        for i, beneficiario in enumerate(beneficiarios, 1):
            print(f"{i}. Nombre: {beneficiario.nombre}")
            print(f"   Número de identificación: {beneficiario.num_cedula}")
            print("-----------------")
        return True
        
    def mostrar_detalle_beneficiario(self, beneficiario):
        """Mostrar detalles completos de un beneficiario"""
        print("-----------------")
        print(f"Nombre: {beneficiario.nombre}")
        print(f"Número de identificación: {beneficiario.num_cedula}")
        print(f"Edad: {beneficiario.edad}")
        print(f"Sexo: {beneficiario.sexo}")
        print(f"Sufre discapacidad: {'Sí' if beneficiario.discapacidad else 'No'}")
        print(f"Estrato: {beneficiario.estrato}")
        print(f"Puntaje de vulnerabilidad: {beneficiario.puntaje_vulnerabilidad}")
        print("-----------------")
        
    def solicitar_datos_beneficiario(self):
        """Solicitar datos para un nuevo beneficiario"""
        print("\nIngrese los siguientes datos sobre el nuevo beneficiario")
        print("-----------------")
        nombre = input("Nombre: ").strip()
        num_cedula = input("Número de Cédula: ").strip()
        edad = self.leer_entero("Edad: ", 0, 150)
        sexo = input("Sexo (M/F): ").strip().upper()
        estrato = input("Estrato: ").strip()
        
        return nombre, num_cedula, edad, sexo, estrato
        
    def solicitar_datos_vulnerabilidad(self, edad):
        """Solicitar datos para calcular vulnerabilidad"""
        if edad >= 18:
            print("\nLlene los siguientes datos para determinar si el beneficiario es apto o no")
        else:
            print("\nEn caso de ser menor de edad, debe llenar los siguientes datos de su representante legal")
        print("-------------------------")
        
        comidas_diarias = self.leer_entero("¿Cuántas veces al día come?: ", 1, 3)
        sueldo_mensual = self.leer_entero("Ingrese su sueldo mensual: ", 0, 999999999)
        personas_a_cargo = self.leer_entero("¿Cuántas personas dependen de usted económicamente?: ", 0, 50)
        
        while True:
            discapacidad_input = input("¿Tiene alguna discapacidad? (si/no): ").lower().strip()
            if discapacidad_input in ['si', 'sí', 's']:
                tiene_discapacidad = True
                break
            elif discapacidad_input in ['no', 'n']:
                tiene_discapacidad = False
                break
            else:
                print("Por favor responda 'si' o 'no'")
                
        while True:
            tipo_vivienda = input("Tipo de vivienda (propia/arriendo/calle): ").lower().strip()
            if tipo_vivienda in ['propia', 'arriendo', 'calle']:
                break
            else:
                print("Por favor ingrese: propia, arriendo o calle")
                
        return comidas_diarias, sueldo_mensual, personas_a_cargo, tiene_discapacidad, tipo_vivienda
        
    def solicitar_datos_adicionales(self):
        """Solicitar datos adicionales para casos límite"""
        print("Es necesario hacer una verificación adicional para determinar si el beneficiario es apto o no")
        print("-----------------")
        
        while True:
            desplazamiento_input = input("¿El beneficiario ha sufrido de desplazamiento? (si/no): ").lower().strip()
            if desplazamiento_input in ['si', 'sí', 's']:
                desplazamiento = True
                break
            elif desplazamiento_input in ['no', 'n']:
                desplazamiento = False
                break
            else:
                print("Por favor responda 'si' o 'no'")
                
        menores_a_cargo = False
        if not desplazamiento:
            while True:
                menores_input = input("¿Tiene menores de 5 años a su cargo? (si/no): ").lower().strip()
                if menores_input in ['si', 'sí', 's']:
                    menores_a_cargo = True
                    break
                elif menores_input in ['no', 'n']:
                    menores_a_cargo = False
                    break
                else:
                    print("Por favor responda 'si' o 'no'")
                    
        return desplazamiento, menores_a_cargo
        
    def mostrar_mensaje(self, mensaje):
        """Mostrar un mensaje al usuario"""
        print(f"\n{mensaje}")
        
    def mostrar_error(self, error):
        """Mostrar un mensaje de error"""
        print(f"\nError: {error}")
        
    def leer_entero(self, mensaje, minimo=None, maximo=None):
        """Leer un número entero con validación"""
        while True:
            try:
                valor = int(input(mensaje))
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"Por favor, ingrese un número entre {minimo} y {maximo}.")
                else:
                    return valor
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")