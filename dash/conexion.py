import psycopg2
class conexion:
    def __init__(self):
        self.connection = None
    def openConnection(self):
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="123456789",
                                               database="BD Amazon Books",
                                               host="localhost", 
                                               port="5432")
        except Exception as e:
            print (e)
    def closeConnection(self):
        self.connection.close()
