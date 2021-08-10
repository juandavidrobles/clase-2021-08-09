from persistencia import Persistencia

db = Persistencia()


# db.add('Gabriela')
db.add('juan')
print(db.estudiantes)

db.remove('juan')
print(db.estudiantes)