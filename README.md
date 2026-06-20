# 🏔️ EDA — Planta de Flotación Minera

**Autor:** Rodolfo Gabriel Riveros Lobos  
**Fecha:** Junio 2026  
**Stack:** Python · Pandas · Matplotlib · Seaborn · Jupyter Notebook

---

## 📋 Descripción del Caso

Análisis exploratorio de datos sobre un proceso industrial de flotación minera.

El objetivo es identificar el comportamiento de las variables de calidad 
del concentrado (% hierro, % sílice) y detectar qué variables operativas 
presentan mayor correlación con la calidad del producto final.

Este análisis simula un escenario real de Data Analyst Junior 
en operaciones mineras.

---

## 📦 Dataset

**Fuente:** Kaggle — Quality Prediction in a Mining Process  
**Link:** https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process  
**Registros:** ~737.000 registros horarios  
**Variables:** 24 variables de proceso e instrumentación

> El dataset no está incluido en este repositorio.  
> Descargarlo desde el link y ubicarlo en `data/raw/`.

---

## 🗂️ Estructura del Proyecto

mining-eda-flotation-plant/

├── data/

│   ├── raw/              ← Dataset original (no versionado)

│   └── processed/        ← Datos procesados

├── notebooks/

│   └── EDA_Flotation_Plant_RRiveros.ipynb

├── reports/

│   └── INFORME_EJECUTIVO.md

├── images/               ← Gráficos exportados

├── requirements.txt

└── environment.yml

---

## ⚙️ Reproducir el Entorno

```bash
conda create -n mining-eda python=3.11 -y
conda activate mining-eda
pip install -r requirements.txt
```

---

## 🔍 Hallazgos Principales

> *(Se completan al finalizar el análisis)*

- 🔹 Hallazgo 1:
- 🔹 Hallazgo 2:
- 🔹 Hallazgo 3:

---

## 📊 Visualizaciones

> *(Se agregan capturas al finalizar el análisis)*

---

## 📁 Informe Ejecutivo

Ver [`reports/INFORME_EJECUTIVO.md`](reports/INFORME_EJECUTIVO.md)

---

## 🛠️ Stack Técnico

| Herramienta | Uso |
|---|---|
| Python 3.11 | Lenguaje principal |
| Pandas | Manipulación de datos |
| Matplotlib / Seaborn | Visualización |
| Jupyter Notebook | Desarrollo y documentación |
| GitHub | Control de versiones y portfolio |