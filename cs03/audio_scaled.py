from audio_helpers import load, save
import matplotlib.pyplot as plt

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
max_value = max(data)
min_value = min(data)
print(f'The original range is ({min_value}, {max_value}).')
twice_amplitude = [2 * x for x in data]
max_value = max(twice_amplitude)
min_value = min(twice_amplitude)
print(f'The new range is ({min_value}, {max_value}).')
number_of_samples = len(twice_amplitude)
time_axis = [x / rate for x in range(0, number_of_samples)]
plt.plot(time_axis, twice_amplitude)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file} with twice amplitude')
plt.show()
