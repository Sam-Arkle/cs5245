import cs04
from audio_helpers import load, save

rate, data = load('speech.wav')
time_list = cs04.get_times(len(data), 0, rate)
zoomed_time_list, zoomed_audio_data = cs04.zoom(time_list, data, 87300, 87300 + 150)
scaled_audio = cs04.scale(zoomed_audio_data, 5)
clipped_audio = cs04.clip(scaled_audio)
save('wash.wav', rate, clipped_audio)
rate, data = load('wash.wav')
plt = cs04.plot_audio(zoomed_time_list, data, 'wash')
