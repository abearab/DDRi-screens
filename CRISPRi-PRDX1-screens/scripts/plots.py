almost_black = '#111111'

yellow_blue = matplotlib.colors.LinearSegmentedColormap.from_list('YlBu',[(0,'#0000ff'),(.49,'#000000'),(.51,'#000000'),(1,'#ffff00')])
yellow_blue.set_bad('#999999',1)


def cleanAxes(ax, top=False, right=False, bottom=True, left=True):
    ax.grid('off')
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

    #turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    #now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()


def generate_scatterplot(adata, x_col, y_col, name = '', layer = None, ax_range = None, figureScale = 1):
    
    targeting = adata[:,adata.var['design'].str.contains('gene')].to_df(layer).T
    nontargeting = adata[:,~adata.var['design'].str.contains('gene')].to_df(layer).T
    
    fig, ax = plt.subplots(figsize=(2 * figureScale, 2 * figureScale))
    

    ax.scatter(
        targeting.loc[:,x_col],
        targeting.loc[:,y_col],
        s=5, c=almost_black, label='all sgRNAs',
        rasterized=True)

    ax.scatter(
        nontargeting.loc[:,x_col],
        nontargeting.loc[:,y_col],
        s=5, c='#BFBFBF', label='non-targeting',
        rasterized=True)
    
    ax.set_xlabel(x_col,fontsize=8)
    ax.set_ylabel(y_col,fontsize=8)
    
    if ax_range:
        ax_min, ax_max = ax_range
        ax.set_xticks(list(range(ax_min,ax_max+1, 2)))
        ax.set_yticks(list(range(ax_min,ax_max+1, 2)))

    ax.tick_params(axis='both', which='major', labelsize=8)
    ax.tick_params(axis='both', which='minor', labelsize=6)

    plt.title(f"Scatter Plot of {name}", fontsize=10)
    cleanAxes(ax)
    plt.grid(None)
    plt.tight_layout()
    plt.show()