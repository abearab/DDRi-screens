library(ggplot2)
library(RColorBrewer)
library(tidyverse)
library(ggrepel)


# scale_color_manual(values = c('#3182bd', '#de2d26'),
#                    labels = c('Sensitizing Hits', 'Resistance Hits'))

plot_volcano <- function(df, score = 'rho',threshold = 100,
                         up_hit='resistance_hit',down_hit='sensitivity_hit',
                         xlim_l=-13,xlim_r=13,ylim=300){
    
    pseudo_sd <- df %>% dplyr::filter(gene=="non-targeting") %>% select(score) %>% as.list %>% unlist %>% sd
    draw_threshold <- function(x){threshold * pseudo_sd * sign(x)/(x)}

    p <- df %>% drop_na %>%
        ggplot(aes(x=score,y=-1*log10(pvalue)) ) + 
        geom_point(
            data = df %>% filter(label=='gene_non_hit'), 
            size = 1, color = 'gray90') +
        geom_point(
            data = df %>% filter(label==up_hit), 
            size = 2, color = '#fcae91') + 
        geom_point(
            data = df %>% filter(label==down_hit), 
            size = 2, color = '#bdd7e7') +
        geom_point(
            data = df %>% filter(label=="non-targeting"), 
            size = 1, color = 'gray70')
    
    p + xlab('log2FoldChange') -> p
    # if (score == 'gamma'){
    #     p + xlab(expression('CRISPRi phenotype (' * gamma * ')')) -> p
    # } 
    # if (score == 'rho'){
    #     p + xlab(expression('CRISPRi phenotype (' * rho * ')')) -> p #drug
    # }
    p +
        theme_classic() +
        xlim(xlim_l,xlim_r) +
        scale_y_continuous(limits = c(0.1,ylim)) +
        ylab(expression('-log'[10] * 'p-value')) +
        stat_function(fun = draw_threshold, linetype = 'dashed', color = 'black') -> p
    
    return(p)
}

label_as_black <- function(p,dd, size = 3, t_x = -0.2, t_y = -0.1){
    p + geom_point(
        data = dd, 
        size = size, shape=21,
        stroke=0.5, 
        colour = "black", fill = "black"
    ) + 
    geom_text_repel(data = dd,
                    aes(label=gene),
                    color = 'black', size = size, nudge_x = t_x, nudge_y = t_y)
}

label_sensitivity_hit <- function(p,dd, size = 3, t_x = -0.2, t_y = -0.1){
    p + geom_point(
        data = dd, 
        size = size, shape=21,
        # stroke=0.5, 
        # colour = "grey30", 
        fill = "#3182bd"
    ) + 
    geom_text_repel(data = dd,
                    aes(label=gene),
                    color = 'black', size = size, nudge_x = t_x, nudge_y = t_y)
}

label_resistance_hit <- function(p,dd, size = 3, t_x = 0.2, t_y = 0.1){
    p + geom_point(
        data = dd, 
        size = size, shape=21,
        stroke=0.5, 
        colour = "grey30", fill = "#de2d26"
    ) + 
    geom_text_repel(data = dd,
                    aes(label=gene),
                    color = 'black', size = size, nudge_x = t_x, nudge_y = t_y)
}