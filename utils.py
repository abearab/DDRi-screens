import os
import pandas as pd
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import squareform


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


def get_score(screen,score,rename=None,rep='ave_rep1_rep2'):
    df = screen['gene scores'].xs(score, level=0, axis=1).xs(rep, level=0, axis=1)
    del df['transcripts']
    if rename: score = rename
    df = df.loc[:,['average phenotype of strongest 3','Mann-Whitney p-value']].rename({
        'average phenotype of strongest 3': score + '.rho', 
        'Mann-Whitney p-value': score+'.pvalue'
    }, axis='columns')
    
    ### Normalization based on Negative Control gRNAs ### 
    ## step 1: select neg ctrl gRNAs scores
    ctrl_gRNA = np.array(['pseudo' in g for g in df.index])     
    ## step 2: measure mean neg ctrl gRNAs scores
    mean_ctrl_gRNA  = np.median(df.loc[ctrl_gRNA,score + '.rho'])
    ## step 3: subtract mean of neg ctrl gRNAs scores
    df.loc[:,score + '.rho.norm'] = df.loc[:,score + '.rho'] - mean_ctrl_gRNA
    ## step 4: measure std of neg ctrl gRNAs scores
    sigma = np.std(df.loc[ctrl_gRNA,score + '.rho'])
    ## step 5: divide by std of neg ctrl gRNAs scores
    df.loc[:,score + '.rho.norm'] = df.loc[:,score + '.rho.norm'] / sigma
    ## step 6: remove rows with pseudo index, neg control gRNAs 
    df = df.loc[ctrl_gRNA == False,:]
    
    print (f'{score} ->\n\tmean(neg control gRNAs rho score): {mean_ctrl_gRNA}')
    print (f'\tstd(neg control gRNAs rho score): {sigma}')
    
    return df


#     def plot_corr(df,title,vmin=None,vmax=None,sub=111):
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



def corr_clust(data,dendrogram=False, threshold = 0.8):
    '''Correlation Heatmaps with Hierarchical Clustering
    '''
    # https://www.kaggle.com/sgalella/correlation-heatmaps-with-hierarchical-clustering
    dissimilarity = 1 - abs(data.corr())
    Z = linkage(squareform(dissimilarity), 'complete')
    
    if dendrogram:
        return Z
        
    else:
        # the cluster
        labels = fcluster(Z, threshold, criterion='distance')

        # Keep the indices to sort labels
        labels_order = np.argsort(labels)

        # Build a new dataframe with the sorted columns
        for idx, i in enumerate(data.columns[labels_order]):
            if idx == 0:
                clustered = pd.DataFrame(data[i])
            else:
                df_to_append = pd.DataFrame(data[i])
                clustered = pd.concat([clustered, df_to_append], axis=1)

        correlations = clustered.corr()

        return correlations
        

def plot_corr(data,ax,vmin=None,vmax=None):
    # Compute the correlation matrix
    corr = corr_clust(data)
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(
        round(corr,2), mask=mask, cmap=cmap, vmin=vmin,vmax=vmax, center=0,
        square=True, linewidths=.5, cbar_kws={"shrink": .5},ax=ax
    )