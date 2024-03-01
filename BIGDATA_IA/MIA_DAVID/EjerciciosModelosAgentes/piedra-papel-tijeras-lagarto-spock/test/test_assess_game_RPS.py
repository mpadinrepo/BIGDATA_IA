import pytest
from src.RPS_dict import GameResult, GameAction, assess_game

@pytest.mark.empate
def test_empate():
    '''
    Partidas con empate
    '''

    assert GameResult.Empate == assess_game(
        accion_usuario=GameAction.Piedra,
        accion_computadora=GameAction.Piedra)

    assert GameResult.Empate == assess_game(
        accion_usuario=GameAction.Tijeras, 
        accion_computadora=GameAction.Tijeras)

    assert GameResult.Empate == assess_game(
        accion_usuario=GameAction.Papel,
        accion_computadora=GameAction.Papel)

@pytest.mark.piedra
def test_piedra_pierde():
    '''
    Piedra pierde con Papel 
    '''
    assert GameResult.Victoria == assess_game(
        accion_usuario=GameAction.Papel,
        accion_computadora=GameAction.Piedra)

@pytest.mark.piedra
def test_piedra_gana():
    '''
    Piedra gana a Tijeras
    '''
    assert GameResult.Derrota == assess_game(
        accion_usuario=GameAction.Tijeras,
        accion_computadora=GameAction.Piedra)

@pytest.mark.papel
def test_papel_pierde():
    '''
    Papel pierde con Tijeras
    '''
    assert GameResult.Victoria == assess_game(
        accion_usuario=GameAction.Tijeras,
        accion_computadora=GameAction.Papel)

@pytest.mark.papel
def test_papel_gana():
    '''
    Papel gana a Piedra
    '''
    assert GameResult.Derrota == assess_game(
        accion_usuario=GameAction.Piedra,
        accion_computadora=GameAction.Papel)

@pytest.mark.tijeras
def test_tijeras_pierde():
    '''
    Tijeras pierde con Piedra 
    '''
    assert GameResult.Victoria == assess_game(
        accion_usuario=GameAction.Piedra,
        accion_computadora=GameAction.Tijeras)

@pytest.mark.tijeras
def test_tijeras_gana():
    '''
    Tijeras gana a Papel 
    '''
    assert GameResult.Derrota == assess_game(
        accion_usuario=GameAction.Papel,
        accion_computadora=GameAction.Tijeras)
