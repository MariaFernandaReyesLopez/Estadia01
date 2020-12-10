import web # IMPORTACCION DE WEB.

import mvc.models.model as model

model_alumnos = model.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class CargaAcademica():
    
    def GET(self):
        try:
            result = model_alumnos.select()
            return render.cargaacademica(result) # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.