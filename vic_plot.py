'''
fix, ax =vic_plot.config(
        title=None,
        x_label=None,
        y_label=None
        )
ax.plot(x_data,y_data,label="Label")
vic_plot.savefig(fig,"Figure.png")
'''
def config(
        title=None,
        x_label=None,
        y_label=None
        ):
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
          'figure.subplot.bottom'   :   16/15*2/6,
          'figure.subplot.left'     :   16/15*3/24,
          'figure.subplot.right'    : 1-16/15*1/3-0.03,
          'figure.subplot.top'      : 1-16/15*5/48,
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
          'savefig.transparent'     : False,
          'text.antialiased'        : True,
          'xtick.labelsize'         : 'medium',
          'ytick.labelsize'         : 'medium',
        })
    fig, ax = plt.subplots()
    fig.suptitle(title, x=0.01, y=0.99, ha='left',va='top')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return fig, ax

def savefig(figure,name):
    import matplotlib.pyplot as plt
    figure.legend(loc='upper left',bbox_to_anchor=(1-16/15*1/3,1-16/15*5/48))
    figure.savefig(name)
    plt.close()

def title(fig,TITLE):
    # Deprecated
    import matplotlib.pyplot as plt
    fig.suptitle(TITLE, x=0.01, y=0.99, ha='left')
    fig.legend(loc='upper left',bbox_to_anchor=(1-16/15*1/3,1-16/15*5/48))
    return fig
