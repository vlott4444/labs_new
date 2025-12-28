from classes import Conductor,Orchestra, ConductorOrchestra

orchestras = [
    Orchestra(1, 'Большой симфонический оркестр'),
    Orchestra(2, 'Камерный оркестр "Виртуозы"'),
    Orchestra(3, 'Симфонический оркестр филармонии'),
    Orchestra(4, 'Студийный оркестр'),
    Orchestra(5, 'Эстрадный оркестр'),
]

# Дирижеры
conductors = [
    Conductor(1, 'Светланов', 40, 1),
    Conductor(2, 'Плетнев', 35, 2),
    Conductor(3, 'Федосеев', 45, 3),
    Conductor(4, 'Гергиев', 38, 3),
    Conductor(5, 'Баршай', 30, 4),
    Conductor(6, 'Китаенко', 42, 1),
    Conductor(7, 'Синайский', 36, 5),
]

conductors_orchestras = [
    ConductorOrchestra(1, 1),
    ConductorOrchestra(1, 6),
    ConductorOrchestra(2, 2),
    ConductorOrchestra(3, 3),
    ConductorOrchestra(3, 4),
    ConductorOrchestra(4, 5),
    ConductorOrchestra(5, 7),

    # Дополнительные связи для многие-ко-многим
    ConductorOrchestra(1, 3),  # Светланов также дирижирует Симфоническим оркестром
    ConductorOrchestra(2, 7),  # Плетнев также дирижирует Эстрадным оркестром
    ConductorOrchestra(3, 1),  # Федосеев также дирижирует Большим симфоническим
    ConductorOrchestra(4, 2),  # Баршай также дирижирует Камерным оркестром
    ConductorOrchestra(5, 5),  # Синайский также дирижирует Студийным оркестром
]