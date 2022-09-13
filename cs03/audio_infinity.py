import matplotlib.pyplot as plt
from audio_helpers import load, save

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
infinite_amplitude = [100000 * x for x in data]
clipped_amplitude = [32767 if x > 32767 else -32768 if x < -32768 else x for x in infinite_amplitude]
max_value = max(clipped_amplitude)
min_value = min(clipped_amplitude)
print(f'The clipped range is ({min_value}, {max_value}).')

number_of_samples = len(clipped_amplitude)
time_axis = [x / rate for x in range(0, number_of_samples)]

plt.plot(time_axis, clipped_amplitude)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file} with infinite amplitude, clipped')
plt.show()

filename_clipped = wav_file[:-4] + '_infinity' + wav_file[-4:]
save(filename_clipped, rate, clipped_amplitude)
