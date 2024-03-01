import pytest
from src.RPS_spock_lizard import Juego, ResultadoJuego, AccionJuego


@pytest.fixture
def juego():
    '''
    Configuración del objeto juego
    '''
    juego_configurado = Juego()
    return juego_configurado


@pytest.mark.empate
def test_empate(juego):

    assert ResultadoJuego.Empate == juego.evaluar_juego(
        accion_usuario=AccionJuego.Spock,
        accion_computadora=AccionJuego.Spock)

    assert ResultadoJuego.Empate == juego.evaluar_juego(
        accion_usuario=AccionJuego.Lagarto,
        accion_computadora=AccionJuego.Lagarto)

    assert ResultadoJuego.Empate == juego.evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Piedra)

    assert ResultadoJuego.Empate == juego.evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Tijeras)

    assert ResultadoJuego.Empate == juego.evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Papel)


@pytest.mark.spock
def test_spock_pierde(juego):
    '''
    Spock pierde contra Lagarto y Papel 
    '''
    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Spock)

    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Lagarto,
        accion_computadora=AccionJuego.Spock)


@pytest.mark.spock
def test_spock_gana(juego):
    '''
    Spock gana a Piedra y Tijeras 
    '''
    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Spock)

    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Spock)


@pytest.mark.lagarto
def test_lagarto_pierde(juego):
    '''
    Lagarto pierde contra Piedra y Tijeras 
    '''
    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Lagarto)

    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Lagarto)


@pytest.mark.lagarto
def test_lagarto_gana(juego):
    '''
    Lagarto gana a Spock y Papel 
    '''
    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Spock,
        accion_computadora=AccionJuego.Lagarto)

    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Lagarto)


@pytest.mark.piedra
def test_piedra_pierde(juego):
    '''
    Piedra pierde contra Spock y Papel 
    '''
    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Spock,
        accion_computadora=AccionJuego.Piedra)

    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Piedra)


@pytest.mark.piedra
def test_piedra_gana(juego):
    '''
    Piedra gana a Tijeras y Lagarto 
    '''
    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Piedra)

    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Lagarto,
        accion_computadora=AccionJuego.Piedra)


@pytest.mark.papel
def test_papel_pierde(juego):
    '''
    Papel pierde contra Tijeras y Lagarto 
    '''
    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Tijeras,
        accion_computadora=AccionJuego.Papel)

    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Lagarto,
        accion_computadora=AccionJuego.Papel)


@pytest.mark.papel
def test_papel_gana(juego):
    '''
    Papel gana a Piedra y Spock 
    '''
    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Papel)

    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Spock,
        accion_computadora=AccionJuego.Papel)


@pytest.mark.tijeras
def test_tijeras_pierde(juego):
    '''
    Tijeras pierde contra Spock y Piedra 
    '''
    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Spock,
        accion_computadora=AccionJuego.Tijeras)

    assert ResultadoJuego.Victoria == juego.evaluar_juego(
        accion_usuario=AccionJuego.Piedra,
        accion_computadora=AccionJuego.Tijeras)


@pytest.mark.tijeras
def test_tijeras_gana(juego):
    '''
    Tijeras gana a Lagarto y Papel 
    '''
    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Lagarto,
        accion_computadora=AccionJuego.Tijeras)

    assert ResultadoJuego.Derrota == juego.evaluar_juego(
        accion_usuario=AccionJuego.Papel,
        accion_computadora=AccionJuego.Tijeras)


@pytest.mark.acciones
def test_accion_menos():
    '''
    Comportamiento del tipo Enum AccionJuego
    '''
    assert 1 == len(AccionJuego.menos(
        AccionJuego.Tijeras,
        AccionJuego.Lagarto,
        AccionJuego.Papel,
        AccionJuego.Piedra))

    assert 4 == len(AccionJuego.menos(AccionJuego.Lagarto))

    assert AccionJuego.Lagarto not in AccionJuego.menos(AccionJuego.Lagarto)

    assert AccionJuego.Lagarto in AccionJuego.menos(AccionJuego.Spock, AccionJuego.Piedra)
