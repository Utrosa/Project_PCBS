###################################################################
#
# Create a tone for the Shams illusion: WORK IN PROGRESS !!
#
###################################################################

# 1. Import packages.

import librosa
import matplotlib.pyplot as plt

# 2. Specify tone properties such as as frequency and duration.

TONE_FREQUENCY = 3500 # Hz
TONE_DURATION = 7 # ms

# 3. Create the tone.

TONE = librosa.tone(frequency=TONE_FREQUENCY, duration=TONE_DURATION)

# 4. Plot the spectrogram.

fig, ax = plt.subplots()
S = librosa.feature.melspectrogram(y=TONE)
librosa.display.specshow(librosa.power_to_db(S, ref=np.max),
                         x_axis='time', y_axis='mel', ax=ax)
plt.show()

# 5. Save the tone as wav.

librosa.output.write_wav(path="C:/Users/monik/Documents/Paris/M1 - S2/PROG 201/myproject/tone.wav", y, sr, norm=False)