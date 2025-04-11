def config(): 
    from cycler import cycler
    import matplotlib.pyplot as plt
    marker_color = [
    ['o',"#1f77b4"],  
    ['D',"#ff7f0e"],  
    ['d',"#2ca02c"],  
    ['p',"#d62728"],  
    ['P',"#9467bd"],  
    ['*',"#8c564b"],  
    ['h',"#e377c2"],  
    ['+',"#7f7f7f"],  
    ['x',"#bcbd22"],  
    ['X',"#17becf"],  
    ]
    plt.rcParams.update({
          'axes.autolimit_mode'     : 'round_numbers',
          'axes.labelsize'          : 'medium',
          'axes.labelweight'        : 'bold',
          'axes.linewidth'          : 0.8,
          'axes.prop_cycle'         :     cycler('marker', [marker[0] for marker in marker_color]
                                      ) + cycler('color', [color[1] for color in marker_color]),
          'axes.spines.right'       : False,
          'axes.spines.top'         : False,
          'axes.titlelocation'      : 'left',
          'axes.titlesize'          : 'medium',
          'axes.titleweight'        : 'bold',
          'axes.xmargin'            : 0,
          'axes.ymargin'            : 0,
          'figure.dpi'              : 300.0,
          'figure.figsize'          :[15/2.54,9*15/16/2.54],
          'figure.subplot.bottom'   :   16/15*1/6,
          'figure.subplot.left'     :   16/15*3/24,
          'figure.subplot.right'    : 1-16/15*1/3,
          'figure.subplot.top'      : 1-16/15*1/12,
          'figure.titlesize'        : 'medium',
          'figure.titleweight'      : 'bold',
          'font.family'             : 'monospace',
          'font.size'               : 11.0,
          'font.stretch'            : 'normal',
          'font.style'              : 'normal',
          'font.variant'            : 'normal',
          'font.weight'             : 'bold',
          'grid.color'              : '#000000',
          'grid.linewidth'          : 0.8,
          'hatch.color'             : 'black',
          'legend.borderaxespad'    : 0,
          'legend.borderpad'        : 0,
          'legend.edgecolor'        : '1',
          'legend.facecolor'        : 'white',
          'legend.fancybox'         : False,
          'legend.fontsize'         : 'medium',
          'legend.framealpha'       : 0,
          'legend.frameon'          : False,
          'legend.loc'              : 'upper right',
          'legend.title_fontsize'   : 'medium',
          'lines.linewidth'         : 1.5,
          'lines.markeredgecolor'   : 'black',
          'lines.markeredgewidth'   : 1,
          'lines.markersize'        : 5.0,
          'markers.fillstyle'       : 'none',
          'savefig.format'          : 'png',
          'savefig.transparent'     : True,
          'text.antialiased'        : True,
          'xtick.labelsize'         : 'medium',
          'ytick.labelsize'         : 'medium',
        })
    fig, ax = plt.subplots()
    return fig, ax
def title(fig,TITLE):
    fig.suptitle(TITLE, x=0.01, y=1, ha='left')
    fig.legend(loc='outside upper right',bbox_to_anchor=(0.99,1-1/12))
    return fig
