from mayday import lee_desastres, parsea_hora, desastres_con_fallecidos_en_tierra

def test_lee_desastres():
    desastres = lee_desastres("data/mayday.csv")
    print(f"Número de desastres leídos: {len(desastres)}")
    print("Los dos primeros desastres son:")
    print(desastres[0])
    print(desastres[1])
    print("Los dos últimos desastres son:")
    print(desastres[-2])
    print(desastres[-1])

def test_desastres_con_fallecidos_en_tierra():
    desastres = lee_desastres("data/mayday.csv")
    print("Los 5 desastres con más fallecidos en tierra son:")
    desastres_con_tierra = desastres_con_fallecidos_en_tierra(desastres,5)
    print( desastres_con_tierra)

if __name__ == "__main__":
    #test_lee_desastres()
    test_desastres_con_fallecidos_en_tierra()
