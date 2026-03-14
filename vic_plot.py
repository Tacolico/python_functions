'''
fig, ax =vic_plot.config(
        title=None,
        x_label=None,
        y_label=None
        )
ax.plot(x_data,y_data,label="Label")
vic_plot.savefig(fig,"Figure")
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
          'figure.subplot.bottom'   :   16/15*1/6,
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
    import navigation
    name=name+".png"
    figure.legend(loc='upper left',bbox_to_anchor=(1-16/15*1/3,1-16/15*5/48))
    navigation.check_path(name)
    figure.savefig(name)
    plt.close()

def pareto_plot(
        INDEX,  # Failure names
        DATA,   # Failure data
        y_label,# data_units
        PATH,   # File path
        ):
    import pandas as pd
    name=PATH.split("/")[-1]
    df=pd.DataFrame()
    df["INDEX"] = INDEX
    df["DATA"] = DATA
    df.sort_values(by='DATA', ascending=False,inplace=True)
    df['Cumulative Sum'] = df['DATA'].cumsum()
    pareto=df["DATA"].sum()*0.8
    df=df[df["Cumulative Sum"]<=pareto]
    df=df.drop(columns="Cumulative Sum").reset_index(drop=True)
    import vic_plot
    fig, ax =vic_plot.config(
        title=f"80% = {pareto:.1f} {y_label}"+(" | "+str(name))*(name!=None),
        y_label=y_label
        )
    for i,row in df.iterrows():
        ax.bar(row.iloc[0],row.iloc[1],label=row.iloc[0])
    y_max = -(-pareto // 1)
    y_ticks = [ y_max//4*i for i in range(1,5)]
    y_ticks.append(y_max)
    ax.set_yticks(y_ticks)
    ax.set_xticks([])
    vic_plot.savefig(fig,PATH)


