import matplotlib.pyplot as plt
from audio_helpers import load, save

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
squeaky_data = data[::2]


number_of_samples = len(squeaky_data)
length_of_selection = number_of_samples / rate
print(f'The squeaky audio has {number_of_samples} samples.')
print(f'The squeaky audio is {length_of_selection:.3f} seconds long.')
time_axis = [x / rate for x in range(0, number_of_samples)]

plt.plot(time_axis, squeaky_data)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file}, with every other sample removed')
plt.show()

filename_clipped = wav_file[:-4] + '_squeaky' + wav_file[-4:]
save(filename_clipped, rate, squeaky_data)
