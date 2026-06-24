import matplotlib.pyplot as plt
import seaborn as sns


def plot_quality_distributions(df, vars_calidad):
    """
    Genera una grilla de gráficos (Histograma y Boxplot)
    para las variables de calidad del concentrado.
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Distribución de Variables de Calidad del Concentrado",
                 fontsize=14, fontweight="bold", y=1.01)

    for i, var in enumerate(vars_calidad):
        # Histograma
        ax1 = axes[i, 0]
        df[var].hist(bins=80, ax=ax1, color="steelblue",
                     edgecolor="white", alpha=0.8)
        ax1.axvline(df[var].mean(), color="red", linestyle="--",
                    linewidth=1.5, label=f"Media: {df[var].mean():.2f}")
        ax1.axvline(df[var].median(), color="orange", linestyle="--",
                    linewidth=1.5, label=f"Mediana: {df[var].median():.2f}")
        ax1.set_title(f"{var} — Distribución")
        ax1.set_xlabel(var)
        ax1.set_ylabel("Frecuencia")
        ax1.legend()

        # Boxplot
        ax2 = axes[i, 1]
        ax2.boxplot(df[var].dropna(), patch_artist=True,
                    boxprops=dict(facecolor="steelblue", alpha=0.6))
        ax2.set_title(f"{var} — Boxplot")
        ax2.set_ylabel(var)

    plt.tight_layout()
    plt.savefig("../images/distribucion_calidad.png",
                dpi=150, bbox_inches="tight")
    plt.show()


def plot_evolucion_temporal(df_diario):
    """
    Genera el gráfico de líneas de evolución temporal
    para Hierro y Sílice con promedios diarios.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True)
    fig.suptitle("Evolución Temporal de Calidad del Concentrado\n(Promedios Diarios)",
                 fontsize=14, fontweight="bold")

    ax1.plot(df_diario.index, df_diario["% Iron Concentrate"],
             color="steelblue", linewidth=1, label="% Iron Concentrate")
    ax1.axhline(df_diario["% Iron Concentrate"].mean(), color="red",
                linestyle="--", linewidth=1,
                label=f"Media: {df_diario['% Iron Concentrate'].mean():.2f}%")
    ax1.axhline(64.0, color="orange", linestyle=":", linewidth=1.5,
                label="Límite inferior referencia: 64%")
    ax1.set_ylabel("% Iron Concentrate")
    ax1.legend(loc="lower right")
    ax1.set_ylim(60, 70)

    ax2.plot(df_diario.index, df_diario["% Silica Concentrate"],
             color="tomato", linewidth=1, label="% Silica Concentrate")
    ax2.axhline(df_diario["% Silica Concentrate"].mean(), color="darkred",
                linestyle="--", linewidth=1,
                label=f"Media: {df_diario['% Silica Concentrate'].mean():.2f}%")
    ax2.axhline(4.0, color="orange", linestyle=":", linewidth=1.5,
                label="Límite superior referencia: 4%")
    ax2.set_ylabel("% Silica Concentrate")
    ax2.set_xlabel("Fecha")
    ax2.legend(loc="upper right")
    ax2.set_ylim(0, 7)

    plt.tight_layout()
    plt.savefig("../images/evolucion_temporal_calidad.png",
                dpi=150, bbox_inches="tight")
    plt.show()


def plot_heatmap_correlaciones(correlaciones):
    """Genera el mapa de calor de todas las variables de proceso."""
    plt.figure(figsize=(16, 12))
    sns.heatmap(correlaciones, annot=True, fmt=".2f", cmap="coolwarm",
                center=0, linewidths=0.5, linecolor="white",
                annot_kws={"size": 7})
    plt.title("Matriz de Correlación — Variables de Proceso y Calidad",
              fontsize=14, fontweight="bold", pad=15)
    plt.tight_layout()
    plt.savefig("../images/heatmap_correlaciones.png",
                dpi=150, bbox_inches="tight")
    plt.show()


def plot_barras_correlacion_silice(corr_calidad):
    """Genera el gráfico de barras de correlación con % Silica Concentrate."""
    plt.figure(figsize=(12, 7))
    colores = ["tomato" if x > 0 else "steelblue"
               for x in corr_calidad["% Silica Concentrate"]]

    corr_calidad["% Silica Concentrate"].plot(kind="barh", color=colores,
                                               edgecolor="white")
    plt.axvline(0, color="black", linewidth=0.8)
    plt.axvline(0.3, color="orange", linestyle="--",
                linewidth=1, label="Umbral referencia: ±0.3")
    plt.axvline(-0.3, color="orange", linestyle="--", linewidth=1)
    plt.title("Correlación de Variables de Proceso con % Silica Concentrate",
              fontsize=13, fontweight="bold")
    plt.xlabel("Coeficiente de Correlación de Pearson")
    plt.legend()
    plt.tight_layout()
    plt.savefig("../images/correlacion_silice.png",
                dpi=150, bbox_inches="tight")
    plt.show()