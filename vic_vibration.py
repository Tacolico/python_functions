def integrate_rotation(signal,sample_rate):
    integrated=[0 for i in range(len(signal))]
    for i in range(1,len(signal)):
        integrated[i]=(signal[i]+signal[i-1])/2*1/sample_rate+integrated[i-1]
    integrated=fft_lh_filter(integrated,sample_rate,1)
    return integrated

def convert_ACE(ace,sample_rate):
    ace=fft_lh_filter(ace,sample_rate,1)
    vel=integrate_rotation(ace,sample_rate)
    pos=integrate_rotation(vel,sample_rate)
    return [ace,vel*10**3,pos*10**6]

def fft_lh_filter(
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    plot        = False,
    ):
    import numpy as np
    from scipy.fft import rfft, irfft, rfftfreq

    signal_sample = len(signal)
    delta_time    = 1/sample_rate
    duration      = signal_sample * delta_time
    if low_filter is not None:
        lfilter = int(duration * low_filter ) + 1*((duration * low_filter )%1 > 0)
    else:
        lfilter=None
    if high_filter is not None:
        hfilter = int(duration * high_filter) + 1*((duration * high_filter)%1 > 0)
    else:
        hfilter=None
    signal_fft                  = rfft(signal)
    frequencies                 = rfftfreq(signal_sample, d=delta_time)
    filter_fft                  = np.zeros_like(signal_fft)
    filter_fft[lfilter:hfilter] = 1  
    filtered_signal_fft         = signal_fft * filter_fft
    if plot==False:
        return irfft(filtered_signal_fft)
    if plot==True:
        return filtered_signal_fft[lfilter:hfilter],frequencies[lfilter:hfilter]

def fft_lh_plot(
    path        = None,
    name        = "Random wave file",
    label       = "Random wave label",
    units       = "Un",
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    ):
    import matplotlib.pyplot as plt 
    filtered_fft,freq = fft_lh_filter(signal,sample_rate,low_filter,high_filter,True)
    absolute_data    = np.abs(filtered_fft)/len(signal)*2
    top_five_indices = np.argpartition(absolute_data, -5)[-5:]
    # Plot configuration
    import vic_plot
    fig,ax=vic_plot.config()
    # 
    ax.plot(freq,absolute_data,label=label,linewidth=0)
    ax.vlines(freq,[0 for i in freq],absolute_data)
    for index in top_five_indices:
        ax.annotate(f'{freq[index]:.0f}', (freq[index], absolute_data[index]), textcoords="offset points", xytext=(0,5), ha='center')
    vice_plot.title(fig,f"FFT, sample frequency = {sample_rate} Hz") 
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel(f'Amplitude [{units}]')
    if path != None:
        # Navigate folders
        import vic_nav
        #
        vic_nav.new_folder(path)
        fig.savefig(path+"/"+name.lower().replace(" ","_")+'.png')
    if path == None:
        fig.savefig(name.lower().replace(" ","_")+'.png')
    plt.close('all')
    plt.rcdefaults()

