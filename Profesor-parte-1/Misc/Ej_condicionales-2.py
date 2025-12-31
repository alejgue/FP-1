def categorizar(token):
    match token:
        case "+" | "-" | "*" | "/":
            return "Operador"
        case int() as n if n < 0:
            return "Entero negativo"
        case int():
            return "Entero"
        case str():
            return "Cadena"
        case _:
            return "Otro"

[categorizar(t) for t in ["+", -2, 5, "hola", 2.3]]