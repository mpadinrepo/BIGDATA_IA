# test_nombre_apellido.py

def test_uppercase():
    nombre = "Juan"
    apellido1 = "Perez"
    apellido2 = "Gomez"

    nombreupper = nombre.upper()
    apellido1upper = apellido1.upper()
    apellido2upper = apellido2.upper()

    assert nombreupper == "MANUEL"
    assert apellido1upper == "PADIN"
    assert apellido2upper == "PRESA"

def test_lowercase():
    nombre = "Manuel"
    apellido1 = "Padin"
    apellido2 = "Presa"

    nombrelower = nombre.lower()
    apellido1lower = apellido1.lower()
    apellido2lower = apellido2.lower()

    assert nombrelower == "manuel"
    assert apellido1lower == "padin"
    assert apellido2lower == "presa"

def test_capitalize():
    nombre = "manuel"
    apellido1 = "padin"
    apellido2 = "presa"

    nombrecapitalize = nombre.capitalize()
    apellido1capitalize = apellido1.capitalize()
    apellido2capitalize = apellido2.capitalize()

    assert nombrecapitalize == "Manuel"
    assert apellido1capitalize == "Padin"
    assert apellido2capitalize == "Presa"
