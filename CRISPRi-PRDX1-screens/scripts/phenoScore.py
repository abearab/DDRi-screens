import numpy as np
import pandas as pd


def ann_score_df(df_in, up_hit='resistance_hit', down_hit='sensitivity_hit', threshold=10):
    df = df_in.copy()

    df.columns = ['gene', 'score', 'pvalue']
    df['score'] = df['score'].astype(float)
    df['pvalue'] = df['pvalue'].astype(float)

    pseudo_sd = df[df['gene']=='non-targeting']['score'].tolist()
    pseudo_sd = np.std(pseudo_sd)
    # print (pseudo_sd)
    
    df['label'] = '.'
    df.loc[df['gene']=='non-targeting', 'label'] = 'non-targeting'

    df.loc[(df['score']>0) & (df['label']!='non-targeting') & (df['score']/pseudo_sd * -np.log10(df['pvalue'])>=threshold), 'label'] = up_hit

    df.loc[(df['score']<0) & (df['label']!='non-targeting') & (df['score']/pseudo_sd * -np.log10(df['pvalue'])<=-threshold), 'label'] = down_hit

    df.loc[df['label']=='.', 'label'] = 'gene_non_hit'

    # reorder factors
    df['label'] = pd.Categorical(df['label'], categories=[down_hit, up_hit, 'gene_non_hit', 'non-targeting'])

    return df
