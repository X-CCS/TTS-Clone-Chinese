import numpy as np
np_path='/media/psdz/data3/data/aidatatang_200zh/SV2TTS/synthesizer/embeds/embed-T0055G7072S0215.wav_00.npy'
test = np.load(np_path,encoding = "latin1")
doc = open('1.txt','a')
print(test,file=doc)


