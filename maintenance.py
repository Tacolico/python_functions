# Returns operative reliability and plot
def weibull_reliability(
        x_data      = None,
        x_unit      = None,
        reliability = None,
        plot        = True,
        name        = None,
        failure     = None,
        path        = None,
        ):
    from scipy.stats import kstest, weibull_min
    import numpy as np
    from math import e,log10,ceil
    import vic_plot

    # Weibull fit
    shape, loc, scale = weibull_min.fit(x_data, floc=0)
    ks_stat, ks_pvalue = kstest(x_data, 'weibull_min', args=(shape, loc, scale))
    
    # Histogram data
    n_bins=ceil(1+3.3*log10(len(x_data)))
    x_fit = np.linspace(min(x_data)+max(x_data)/n_bins/2, max(x_data)-max(x_data)/n_bins/2, n_bins)
    y_fit = shape/scale*pow((x_fit-loc)/scale,shape-1)*pow(e,-pow((x_fit-loc)/scale,shape))

    # Reliability 
    x = np.linspace(min(x_data), max(x_data), 100)
    rel= pow(e,-pow((x-loc)/scale,shape))

    # Plot
    if plot==True:
        plot_name=(" | "+str(name))*(name!=None)+(" | "+str(failure))*(failure!=None)
        fig,ax=vic_plot.config(
                title="Reliability"+plot_name,
                x_label=("Work done"+(" "+str(x_unit))*(x_unit!=None)),
                y_label="Probability",
                )
        ax.plot(x,rel,label=f'Weibull 1-CDF',markersize=0,linewidth=3)
        ax2 = ax.twinx()
        ax2.hist(x_data,bins=n_bins, density=True)
        ax2.hist(x_data,bins=n_bins, density=True,label="Histogram data")
        ax2.plot(x_fit, y_fit, label=f'Fitted Weibull\nK-S = {ks_stat:.4f}\nP = {ks_pvalue:.4f}\nShape = {shape:.2f}\nScale = {scale:.0f}\nLoc = {loc:.0f}')
        ax2.tick_params(axis='y', right=False, labelright=False)
        ax.set_zorder(1)
        ax2.set_zorder(0)
        ax.patch.set_alpha(0)  
        if reliability != None:
            op=weibull_min.ppf(1-reliability, shape, loc=loc, scale=scale)
            ax.annotate(f'{reliability:.2f}', xy=(op, reliability), 
                        xytext=(0 , reliability),
                        arrowprops=dict( linestyle='--', arrowstyle='-'),
                        ha='left', va='center' )
            ax.annotate(f'{op:.0f}', xy=(op, reliability), 
                        xytext=(op , 0),
                        arrowprops=dict( linestyle='--', arrowstyle='-'),
                        ha='center', va='bottom' )
        plot_name="Reliability"+plot_name.replace(" | ","_").replace(" ","_")+"_Weibull.png"
        if path != None:
            import navigation
            navigation.new_folder(path)
            vic_plot.savefig(fig,path+"/"+plot_name)
        if path == None:
            vic_plot.savefig(fig,plot_name)
    return op


if __name__ =="__main__":
    import pandas as pd
    from io import StringIO

    data_str = """Sample,Work done [km]
1,13100
2,29200
3,13200
4,10000
5,21400
6,14500
7,12600
8,27400
9,35500
10,15100
"""
    df = pd.read_csv(StringIO(data_str))
    weibull_reliability(
            x_data=df['Work done [km]'].values,
            x_unit="[km]",
            reliability=0.8,
            plot=True,
            name="Machine 123-456",
            failure="broken theet",
            path="lol"
            )
    data_str = """Efecto de la falla,TFS (Horas),Número de fallas,Semana 29 [hr],TFS acumulado (horas),Porcentaje,Porcentaje acumulado,,,
Cable de carga,0.3,6,1.8,,,,,,
Drive Gear D,1,2,2,,,,,,
Filtro de ozono,0.5,8,4,,,,,,
Filtro del Tóner,0.3,6,1.8,,,,,,
Filtro para polvo,0.5,6,3,,,,,,
Ganchos de rodillos superiores,2,5,10,,,,,,
"""
    df = pd.read_csv(StringIO(data_str))
import vic_plot
vic_plot.pareto_plot(
    INDEX=df["Efecto de la falla"],
    DATA=df['Semana 29 [hr]'],
    y_label="[hr]",
    PATH="FFF/lol2",
        )
