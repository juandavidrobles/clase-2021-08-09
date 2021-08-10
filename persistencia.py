import json

class Persistencia:

  def __init__(self, estudiantes_iniciales = None):
    if (estudiantes_iniciales):
      self.estudiantes = estudiantes_iniciales
    else:
      try:
        file = open('./data.json', 'r')
        estudiantes = json.loads(file.read())
        # json.load
        self.estudiantes = estudiantes
        file.close()
      except:
        self.estudiantes = []

  def count(self):
    return len(self.estudiantes)
    
  def add(self, estudiante):
    self.estudiantes.append(estudiante)
    self.update_file()
    
  def remove(self, estudiante):
    self.estudiantes.remove(estudiante)
    self.update_file()

  def update_file(self):
    file = open('./data.json', 'w')
    file.write(json.dumps(self.estudiantes))
    file.close()
      