# Informe Ejecutivo — Análisis de Planta de Flotación Minera

**Autor:** Rodolfo Gabriel Riveros Lobos  
**Fecha:** Junio 2026  
**Período analizado:** Marzo – Septiembre 2017  
**Herramienta:** Python (Pandas, Matplotlib, Seaborn)

---

## Resumen de Situación
Se completó un diagnóstico profundo de 183 días de operación de la planta utilizando datos del sistema SCADA. El objetivo fue determinar la salud de nuestro producto final y definir qué controles operativos garantizan que el concentrado cumpla con los estándares comerciales exigidos por el mercado.

###  Diagnóstico de Operación: ¿Qué encontramos?
* El Hierro es nuestra base sólida: La producción de hierro mantiene una estabilidad excepcional en torno al 65%. Es un indicador confiable que asegura que la planta tiene una base operativa robusta para la recuperación de mineral valioso.

* La Sílice es la amenaza a la rentabilidad: A diferencia del hierro, la sílice es altamente errática. Sus subidas repentinas por encima del 4% son el principal riesgo de rechazo de lotes comerciales. Mientras el hierro es estable, la sílice "salta", comprometiendo la calidad del producto final.

* Identificamos 6 fallas sistémicas: Detectamos 6 días específicos (agrupados en abril/mayo y agosto/septiembre) donde la planta perdió el control simultáneo de ambos indicadores. No fueron eventos aislados, sino períodos donde el proceso de separación falló por completo.

* El flujo de aire es nuestra palanca maestra: El análisis confirmó que el control de aire en las Columnas 01 y 03 es la herramienta más efectiva que tienen los operadores para "limpiar" el concentrado y reducir las impurezas de forma directa.

* Operamos de forma reactiva, no preventiva: Detectamos que el uso de químicos (Amina) funciona actualmente como un "termómetro de emergencia". Se aumenta la dosis solo cuando la sílice ya se disparó. Esto confirma que el sistema está reaccionando al problema en lugar de anticiparlo.
---

## ¿Qué recomendamos?

1. **Implementar Alarmas Inteligentes:**  Configurar alertas en el HMI que se disparen inmediatamente cuando el hierro baje de 64% y la sílice suba de 4% al mismo tiempo. Esto permitirá una intervención antes de que el lote sea irrecuperable.

2. **Estandarizar el Protocolo de Aireación:** Priorizar el ajuste de los caudales de aire en las primeras columnas como primera línea de defensa ante el aumento de impurezas, ya que es el control con impacto más rápido en la calidad.  

3. **Auditoría de los 6 Días Críticos:**  Realizar una revisión de los turnos y las condiciones del mineral alimentado en las fechas detectadas para entender qué causó el quiebre de la estabilidad en esos momentos específicos.

4. **Optimizar el Lazo de Control de Reactivos:** Evaluar la automatización de la dosificación de amina basándose en sensores de entrada, para que el sistema actúe antes de que la sílice llegue al producto final.

---

## Conclusión

La planta produce un hierro de excelente calidad, pero la volatilidad de la sílice drena nuestra eficiencia. Hoy tenemos la información exacta para saber qué válvulas (aire) y en qué momentos (días críticos) la operación pierde dinero. Aplicando un control proactivo en el flujo de aire y alarmas de calidad en tiempo real, podemos estabilizar el producto y eliminar los riesgos de rechazo comercial.