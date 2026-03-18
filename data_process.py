def fft_filter(
    signal      = None,
    sample_rate = None,
    low_filter  = None,
    high_filter = None,
    plot        = False,
    path        = "temp_fft/function",
    label       = "Random wave",
    units       = "Un"
    ):
    import numpy as np
    from scipy.fft import rfft, irfft, rfftfreq

    signal=np.array(signal)
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
    if plot:
        import vic_plot
        vic_plot.fft_plot(
                freqs       = frequencies,
                fft         = signal_fft,
                path        = path,
                label       = label,
                units       = units
                )
    return filtered_signal
