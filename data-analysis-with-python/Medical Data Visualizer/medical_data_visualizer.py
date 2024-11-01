import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where(
    df["weight"] / (df["height"] * df["height"]) * 10000 > 25, 1, 0)

# 3
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)

# 4


def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke",
                    "alco", "active", "overweight"],
    )

    # 6
    df_cat = df_cat.reset_index() \
        .groupby(['variable', 'cardio', 'value']) \
        .agg('count') \
        .rename(columns={'index': 'total'}) \
        .reset_index()

    # 7

    # 8
    fig = sns.catplot(
        x="variable",
        y="total",
        col="cardio",
        hue="value",
        data=df_cat,
        kind="bar").fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(12, 6))

    # 15
    sns.heatmap(corr, mask=mask,
                annot=True, fmt='.1f',
                center=0, vmin=-0.5, vmax=0.5)

    # 16
    fig.savefig('heatmap.png')
    return fig