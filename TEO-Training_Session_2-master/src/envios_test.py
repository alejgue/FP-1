from pathlib import Path

from envios import (
    cliente_con_mas_incidencias,
    coste_total,
    destinos_top_por_peso,
    dias_medios_entre_envios,
    lee_envios,
    lee_incidencias,
    retraso_medio_por_mes,
    segmento_mas_rentable,
)


BASE = Path(__file__).resolve().parent.parent
ENV = BASE / "data" / "envios.csv"
INC = BASE / "data" / "incidencias.csv"


def main() -> None:
    envios = lee_envios(ENV)
    incidencias = lee_incidencias(INC)
    print(f"Total envíos: {len(envios)}")
    print(f"Total incidencias: {len(incidencias)}")

    print("\nCoste total TechNova prioridad alta o media:")
    print(coste_total(envios, cliente="TechNova", prioridades={"ALTA", "MEDIA"}))

    print("\nDestinos top por peso (top 3):")
    print(destinos_top_por_peso(envios))

    print("\nCliente con más incidencias de tipo Demora o Dano:")
    print(
        cliente_con_mas_incidencias(
            envios,
            incidencias,
            tipos={"Demora", "Dano"},
        )
    )

    print("\nRetraso medio por mes (solo prioridad ALTA):")
    print(retraso_medio_por_mes(envios, incidencias, prioridad="ALTA"))

    print("\nSegmento más rentable con mínimo 2 envíos:")
    print(segmento_mas_rentable(envios, minimo_envios=2))

    print("\nDías medios entre envíos de FrescoMarket:")
    print(dias_medios_entre_envios(envios, cliente="FrescoMarket"))


if __name__ == "__main__":
    main()
