import os
import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import seaborn as sns


def find_top(df,value, value_thr, stat, stat_thr, drop_dup=False,silent=False):
    # Select rows (genes) which has value >= value_thr & stat < stat_thr
    #     if n_line==None:
    up = df.iloc[
         [i for i,l in enumerate(
             np.array([
                 np.array(df.loc[:,value] >= value_thr),
                 np.array(df.loc[:,stat] < stat_thr)]).all(axis=0)) if l == 1]
    ,:]
    dn = df.iloc[
         [i for i,l in enumerate(
             np.array([
                 np.array(df.loc[:,value] <= -1*(value_thr)),
                 np.array(df.loc[:,stat] < stat_thr)]).all(axis=0)) if l == 1]
    ,:]

    if drop_dup==True:
        up = up.sort_values(stat).drop_duplicates(subset='gene_id', keep="last")
        dn = dn.sort_values(stat).drop_duplicates(subset='gene_id', keep="last")

    if not silent:
        print ('up: ', up.shape[0])
        print ('down:', dn.shape[0])

    return up, dn


def get_score(screen,score,rename=None,pseudo=False):
    out = screen['gene scores'].xs(score, level=0, axis=1).xs('ave_rep1_rep2', level=0, axis=1)
    del out['transcripts']
    
    if rename:
        score = rename
    
    out = out.loc[:,['average phenotype of strongest 3','Mann-Whitney p-value']].rename({
        'average phenotype of strongest 3': score + '.rho', 
        'Mann-Whitney p-value': score+'.pvalue'
    }, axis='columns')
    
    if not pseudo: 
        out = out.loc[['pseudo' not in g for g in out.index],:]
    
    return out


# def plot_corr(df,title,vmin=None,vmax=None,sub=111):
#     fig = plt.figure()
#     ax = fig.add_subplot(sub)

#     alpha = df.columns.values
#     cax = ax.matshow(df.corr()) #, interpolation='nearest')
#     fig.colorbar(cax)
#     cax.set_clim(vmin,vmax)

#     xaxis = np.arange(len(alpha))
#     ax.set_xticks(xaxis)
#     ax.set_yticks(xaxis)
#     ax.set_xticklabels(alpha, rotation=45)
#     ax.set_yticklabels(alpha, rotation=45)
#     ax.set_title(title, fontsize=15)


#     plt.show()
def plot_corr(df,ax,vmin=None,vmax=None):
    # Compute the correlation matrix
    corr = df.corr('spearman')
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(
        corr, mask=mask, cmap=cmap, vmin=vmin,vmax=vmax, center=0,
        square=True, linewidths=.5, cbar_kws={"shrink": .5},ax=ax
    )