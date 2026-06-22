# Simulación híbrida ABM–LLM de la segunda vuelta presidencial de Colombia 2026

> **Advertencia:** este repositorio contiene un experimento computacional con agentes sintéticos. No es una encuesta, un pronóstico electoral, una estimación representativa, un estudio causal de efectos mediáticos ni una medición de cognición humana real.

## Descripción

El proyecto simula veinte días de campaña mediante dos capas conectadas:

1. un modelo basado en agentes con 1.000 agentes sintéticos heterogéneos; y
2. una deliberación cognitiva posterior mediante Claude, condicionada por el dossier informativo acumulado de cada agente.

La cadena analítica es:

**ingestión de información → interpretación y memoria → reencuadre semántico → transmisión social → emergencia → estado electoral sintético → deliberación LLM**

## Contrato experimental

- Ventana: 1–20 de junio de 2026.
- Frontera electoral: 21 de junio de 2026.
- Agentes: 1.000.
- Observaciones maestras: 207.
- Señales canónicas: 201.
- Observaciones de soporte: 6.
- Categorías de fuentes: 9.
- Semilla del ABM: 42.
- Modelo LLM registrado en la ejecución: `claude-sonnet-4-6`.
- Temperatura LLM: 0.35.

## Contenido principal

- `data/`: paquete auditado v5.1 y copia extraída.
- `notebooks/`: notebook publicable sin outputs.
- `methodology/`: especificación ODD+D, tarjetas del modelo y datos, validación, ética y reproducibilidad.
- `results/`: tablas que respaldan el dashboard.
- `docs/`: dashboard listo para GitHub Pages.
- `release-assets-v1.0.0/`: archivos grandes que deben adjuntarse a un GitHub Release, no al historial normal del repositorio.

## Ejecución básica

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate_data_package.py
python scripts/validate_results.py
pytest
```

Para ejecutar localmente el notebook:

```bash
export COLOMBIA_ABM_PACKAGE_PATH="$PWD/data/raw/colombia_2026_source_balanced_v5_1_methodological_audit.zip"
export COLOMBIA_HYBRID_PROFILE="FULL"
export ANTHROPIC_API_KEY="your-key"
jupyter lab notebooks/Colombia_2026_Presidential_Runoff_The_20_Day_Simulation.ipynb
```

Los resultados publicados describen comportamiento interno del modelo. No deben convertirse en porcentajes de intención de voto real ni en inferencias sobre personas, regiones o grupos demográficos.
