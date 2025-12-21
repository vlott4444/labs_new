class Conductor:
    """Дирижер"""
    def __init__(self, id, name, experience, orchestra_id):
        self.id = id
        self.name = name
        self.experience = experience  # стаж работы в годах (количественный признак)
        self.orchestra_id = orchestra_id

class Orchestra:
    """Оркестр"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ConductorOrchestra:
    """
    'Дирижеры оркестра' для реализации
    связи многие-ко-многим
    """
    def __init__(self, orchestra_id, conductor_id):
        self.orchestra_id = orchestra_id
        self.conductor_id = conductor_id
