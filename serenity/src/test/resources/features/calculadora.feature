Feature: Operaciones de la calculadora
  Como usuario de la calculadora
  Quiero realizar operaciones matemáticas básicas
  Para obtener resultados correctos con números positivos y negativos

  Scenario: Sumar dos números positivos
    Given que tengo los números 5 y 3
    When sumo ambos números
    Then el resultado debe ser 8

  Scenario: Sumar dos números negativos
    Given que tengo los números -5 y -3
    When sumo ambos números
    Then el resultado debe ser -8

  Scenario: Restar dos números positivos
    Given que tengo los números 10 y 4
    When resto el segundo del primero
    Then el resultado debe ser 6

  Scenario: Restar dos números negativos
    Given que tengo los números -10 y -4
    When resto el segundo del primero
    Then el resultado debe ser -6

  Scenario: Multiplicar dos números positivos
    Given que tengo los números 6 y 7
    When multiplico ambos números
    Then el resultado debe ser 42

  Scenario: Multiplicar dos números negativos
    Given que tengo los números -6 y -7
    When multiplico ambos números
    Then el resultado debe ser 42

  Scenario: Dividir dos números positivos
    Given que tengo los números 20 y 5
    When divido el primero entre el segundo
    Then el resultado debe ser 4

  Scenario: Dividir dos números negativos
    Given que tengo los números -20 y -5
    When divido el primero entre el segundo
    Then el resultado debe ser 4

  Scenario: Dividir entre cero
    Given que tengo los números 10 y 0
    When divido el primero entre el segundo
    Then debo recibir un error indicando que no se puede dividir entre cero
