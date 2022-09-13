import matplotlib.pyplot as plt
from audio_helpers import load, save

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
lowered_data = [x for y in zip (data, data) for x in y]

number_of_samples = len(lowered_data)
length_of_selection = number_of_samples / rate
print(f'The low audio has {number_of_samples} samples.')
print(f'The low audio is {length_of_selection:.3f} seconds long.')
time_axis = [x / rate for x in range(0, number_of_samples)]

plt.plot(time_axis, lowered_data)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file}, with every sample duplicated')
plt.show()

filename_clipped = wav_file[:-4] + '_low' + wav_file[-4:]
save(filename_clipped, rate, lowered_data)
