import matplotlib.pyplot as plt
from audio_helpers import load, save

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
zoomed_data = data[79000:97000]
max_value = max(zoomed_data)
min_value = min(zoomed_data)
print(f'The selected range is ({min_value}, {max_value}).')

number_of_samples = len(zoomed_data)
length_of_selection = number_of_samples / rate
selection_start_time = len(data[:79000]) / rate
selection_end_time = length_of_selection + selection_start_time
print(f'The selection has {number_of_samples} samples.')
print(f'The selection is {length_of_selection:.3f} seconds long.')
print(f'The selection starts at {selection_start_time:.3f} and ends at {selection_end_time:.3f}.')
time_axis = [selection_start_time + (x / rate) for x in range(0, number_of_samples)]

plt.plot(time_axis, zoomed_data)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file}, zoomed in from {selection_start_time:.3f} to {selection_end_time:.3f}')
plt.show()

filename_clipped = wav_file[:-4] + '_zoom' + wav_file[-4:]
save(filename_clipped, rate, zoomed_data)
