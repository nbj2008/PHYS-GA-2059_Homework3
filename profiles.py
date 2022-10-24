from Model import Signal, TwoSignal, AmpSignal, TwoAmpSignal
from scipy import optimize as opt
from matplotlib import pyplot as plt
import numpy as np

   
def amplitude_profile(sig: Signal, ax=None):
    amp = AmpSignal.from_signal(sig)
    amp_min = calc if (calc:= sig.amplitude - 50*np.abs(sig.analytic_amplitude_error)) > 0 else 0
    xs = np.linspace(amp_min, sig.amplitude + 50*np.abs(sig.analytic_amplitude_error), num = 100)
    ys = []
    for x in xs:
        amp.Amp = x
        _ = opt.minimize(amp.fit, amp.params)
        ys.append(-amp.negloglike())
    _ = ax.plot(xs, ys) if ax else plt.plot(xs, ys)
    _ = ax.axvline(x=sig.amplitude, color='r', linestyle=":") if ax else plt.axvline(x=sig.amplitude, color='r', linestyle=":")

def two_amplitude_profile(sig: TwoSignal, ax=None):
    amp = TwoAmpSignal.from_signal(sig)
    amp_min = calc if (calc:= sig.amplitude[0] - 50*np.abs(sig.analytic_amplitude_error[0])) > 0 else 0
    xs = np.linspace(amp_min, sig.amplitude[0] + 50*np.abs(sig.analytic_amplitude_error[0]), num = 100)
    ys = []
    for i, x in enumerate(xs):
        amp = TwoAmpSignal.from_signal(sig)
        amp.Amp1 = x
        temp, _ = amp.analytic_params()
        amp.params[0] = temp[0]
        amp.params[2] = temp[1]
        amp.params[3] = temp[2]
        _ = opt.minimize(amp.fit, amp.params)
        ys.append(-amp.negloglike())
    _ = ax.plot(xs, ys) if ax else plt.plot(xs, ys)
    _ = ax.axvline(x=sig.amplitude[0], color='r', linestyle=":") if ax else plt.axvline(x=sig.amplitude[0], color='r', linestyle=":")