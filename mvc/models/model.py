'''
Nota: Pyodbc permite utilizar ODBC para conectar a la gran mayoría de bases de datos.
Es gratuito tanto para uso personal como comercial.
'''

#  Importamos librerias.
import pyodbc

#  Creacion de una clase.
class Alumnos():
        def connect(self):
            try:
                #  Conexion con la base de datos.
                self.cnxn = pyodbc.connect('Driver={SQL Server}; Server=DESKTOP-RRVRH47; Database=saiiut; Integrated Security=SSPI;Persist Security Info=False;')
                self.cursor = self.cnxn.cursor()

            except Exception as e:
                print(e)

        #  Realizamos una consulta a la base de datos.
        def select(self):
            try:
                self.connect()

                #  Consulta
                query = ("SELECT * FROM [saiiut].[saiiut].[maestros] FULL JOIN [saiiut].[saiiut].[personas] ON [saiiut].[saiiut].[maestros].cve_maestro=[saiiut].[saiiut].[personas].cve_persona WHERE cve_tipo_persona='64' OR cve_tipo_persona = '4'")
                self.cursor.execute(query)

                #  Arreglo
                result = []
                for row in self.cursor:

                    #  Diccionario para almacenamiento
                    r = {
                        'cve_maestro':row[0],
                        'cve_universidad':row[1],
                        'cve_carrera':row[2],
                        'cve_division':row[3],
                        'cve_unidad_academica':row[4],
                        'tiempo_completo':row[5],
                        'activo':row[6],
                        'cve_persona':row[7],
                        'cve_universidad':row[8],
                        'nombre':row[9],
                        'apellido_pat':row[10],
                        'apellido_mat':row[11],
                        'cve_estado_civil':row[12],
                        'cve_tipo_persona':row[13],
                        'cve_pais':row[14],
                        'rfc':row[15],
                        'fecha_nacimiento':row[16],
                        'curp':row[17],
                        'sexo':row[18],
                        'cve_tipo_sangre':row[19],
                        'peso':row[20],            
                        'telefonoe':row[21],
                        'correo_alternativo':row[23],
                    }

                    result.append(r)
                self.cursor.close()
                self.cnxn.close()
                return result

            except Exception as e:
                print(e)
                result = []
                return result


        #  Realizamos una consulta a la base de datos.
        def horario(self):
            try:
                self.connect()

                #  Consulta
                query = ("SELECT * FROM [saiiut].[saiiut].[maestros] FULL JOIN [saiiut].[saiiut].[personas] ON [saiiut].[saiiut].[maestros].cve_maestro=[saiiut].[saiiut].[personas].cve_persona WHERE cve_tipo_persona='64' OR cve_tipo_persona = '4'")
                self.cursor.execute(query)

                #  Arreglo
                result = []
                for row in self.cursor:

                    #  Diccionario para almacenamiento
                    r = {
                        'cve_maestro':row[0],
                        'cve_universidad':row[1],
                        'cve_carrera':row[2],
                        'cve_division':row[3],
                        'cve_unidad_academica':row[4],
                        'tiempo_completo':row[5],
                        'activo':row[6],
                        'cve_persona':row[7],
                        'cve_universidad':row[8],
                        'nombre':row[9],
                        'apellido_pat':row[10],
                        'apellido_mat':row[11],
                        'cve_estado_civil':row[12],
                        'cve_tipo_persona':row[13],
                        'cve_pais':row[14],
                        'rfc':row[15],
                        'fecha_nacimiento':row[16],
                        'curp':row[17],
                        'sexo':row[18],
                        'cve_tipo_sangre':row[19],
                        'peso':row[20],            
                        'telefonoe':row[21],
                        'correo_alternativo':row[23],
                    }

                    result.append(r)
                self.cursor.close()
                self.cnxn.close()
                return result

            except Exception as e:
                print(e)
                result = []
                return result



    # Vista al perfil de profesor

        def view(self, cve_maestro):
            try:
                self.connect()
                query = ("SELECT * FROM [saiiut].[saiiut].[maestros] FULL JOIN [saiiut].[saiiut].[personas] ON [saiiut].[saiiut].[maestros].cve_maestro=[saiiut].[saiiut].[personas].cve_persona WHERE cve_maestro = ?")
                values = (cve_maestro)
                self.cursor.execute(query, values)
                result = []
                for row in self.cursor:
                    r = {
                        'cve_maestro':row[0],
                        'cve_universidad':row[1],
                        'cve_carrera':row[2],
                        'cve_division':row[3],
                        'cve_unidad_academica':row[4],
                        'tiempo_completo':row[5],
                        'activo':row[6],
                        'cve_persona':row[7],
                        'cve_universidad':row[8],
                        'nombre':row[9],
                        'apellido_pat':row[10],
                        'apellido_mat':row[11],
                        'cve_estado_civil':row[12],
                        'cve_tipo_persona':row[13],
                        'cve_pais':row[14],
                        'rfc':row[15],
                        'fecha_nacimiento':row[16],
                        'curp':row[17],
                        'sexo':row[18],
                        'cve_tipo_sangre':row[19],
                        'peso':row[20],            
                        'telefonoe':row[21],
                        'correo_alternativo':row[23],
                    }
                result.append(r)
                self.cursor.close()
                self.cnxn.close()
                return result
            except Exception as e:
                print(e)
                result = []
                return result
#  Objetos.
objeto = Alumnos()
objeto.connect()

#  Impresion de filas.
for row in objeto.select():
    print(row)