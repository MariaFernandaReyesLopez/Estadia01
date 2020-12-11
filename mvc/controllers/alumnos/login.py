''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''
import web # IMPORTACCION DE WEB.
#import hashlib


render = web.template.render("mvc/views/alumnos/")

class Login():

    def GET(self):
        try:
            return render.login() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.

    def POST(self):
        try:
            i = web.input()
            
"""
    def POST(self):
           #Comprueba si el usuario se puede logear
            #y crea atributos para la sesión.
        import sys
        inputData = web.input()
 
        check = db.query("SELECT * FROM users WHERE username=$user and password=$pass", vars=inputData)

        if check:
            session.loggedin = True
            session.username = inputData.username
            print >> sys.stderr, "Login Successful"
            raise web.seeother("/dashboard")
         else:
            print >> sys.stderr, "Login Failed"
            return render.login("usuariontraseña inválida")


    def POST(self):
        # C O N E X I O N    A     B D 
        self.cnxn = pyodbc.connect('Driver={SQL Server}; Server=LAPTOP-SH2I8EFC; Database=horarios; Integrated Security=SSPI;Persist Security Info=False;')
        self.cursor = self.cnxn.cursor()

        i = web.input()

        authdb = sqlite3.connect('users.db')
        pwdhash = hashlib.md5(i.password).hexdigest()
        check = authdb.execute('select * from users where username=? and password=?', (i.username, pwdhash))
        if check:
            session.loggedin = True
            session.username = i.username
            raise web.seeother('/results')
        else:
            return render.base("Those login details don't work.")
"""