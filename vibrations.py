'''
def fft_lh_plot(
    path        = "Random wave file",
    label       = "Random wave label",
    units       = "Un",
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    )

y_data=fft_lh_filter(
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    )
x_data=[i*sample_rate for i in range(len(y_data))]
'''
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
    signal_fft    = rfft(signal)
    frequencies   = rfftfreq(signal_sample, d=delta_time)

    filter_mask = np.ones_like(signal_fft, dtype=float)
    if low_filter is not None:
        filter_mask[frequencies <= low_filter] = 0
    if high_filter is not None:
        filter_mask[frequencies >= high_filter] = 0
    filtered_fft  = signal_fft * filter_mask
    filtered_freq = frequencies * filter_mask
    filtered_signal = irfft(filtered_fft)
    if plot==False:
        return filtered_signal
    if plot==True:
        return [signal_fft,frequencies,filtered_signal]

    '''
    duration      = signal_sample * delta_time
    if low_filter is not None:
        lfilter = int(duration * low_filter ) + 1*((duration * low_filter )%1 > 0)
    else:
        lfilter=None
    if high_filter is not None:
        hfilter = int(duration * high_filter) + 1*((duration * high_filter)%1 > 0)
    else:
        hfilter=None
    filter_fft                  = np.zeros_like(signal_fft)
    filter_fft[lfilter:hfilter] = 1  
    filtered_signal_fft         = signal_fft * filter_fft
    if plot==False:
        return irfft(filtered_signal_fft)
    if plot==True:
        return filtered_signal_fft[lfilter:hfilter],frequencies[lfilter:hfilter],irfft(filtered_signal_fft)
    '''

def fft_lh_plot(
    path        = "lol/Random wave file",
    label       = "Random wave label",
    units       = "Un",
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    ):
    import matplotlib.pyplot as plt 
    import numpy as np
    import vic_plot
    [filtered_fft,freq,sig] = fft_lh_filter(signal,sample_rate,low_filter,high_filter,True)
    absolute_data    = np.abs(filtered_fft)/len(signal)*2
    top_five_indices = np.argpartition(absolute_data, -5)[-5:]
    
    fig,ax=vic_plot.config(
    title=f"FFT, sample frequency = {sample_rate} Hz",
    x_label='Frequency [Hz]',
    y_label=f'Amplitude [{units}]'
            )
    ax.plot(freq,absolute_data,label=label,linewidth=0)
    ax.vlines(freq,[0 for i in freq],absolute_data)
    for index in top_five_indices:
        ax.annotate(f'{freq[index]:.0f}', (freq[index], absolute_data[index]), textcoords="offset points", xytext=(0,5), ha='center')
    vic_plot.savefig(fig,path+'.png')
    plt.close('all')
    plt.rcdefaults()
    return sig

