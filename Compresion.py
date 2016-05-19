import  wave
import pyaudio
import  math
import tkFileDialog
from scipy.io.wavfile import read
import struct


class Compresion:

    def __init__(self, wav,threshold,n,Ratio,aframes):
            self.wav = wav
            self.threshold=threshold
            self.n=n
            self.Ratio=Ratio
            self.aframes=aframes




    def compre(self,):

        nuevo=[]
        for i in range (0,len(self.wav)):#Comparacion de valores para hacer la compresion
            if  self.wav[i]>self.threshold:
                if i<self.aframes:
                    compresion=(self.wav[i]/(self.n[i]))
                if i>self.aframes:
                    compresion=self.wav[i]/self.Ratio
                #nuevo.append(compresion)

            elif  self.wav[i]<(-1*self.threshold):
                if i<self.aframes:
                    compresion=(self.wav[i]/(self.n[i]))
                if i>self.aframes:
                    compresion=self.wav[i]/self.Ratio
                #nuevo.append(compresion)

            else:
                compresion=self.wav[i]
                #nuevo.append(compresion)
            nuevo.append(compresion)
        print 'Archivo',self.wav
        print 'Compresion',nuevo

        output = wave.open("CompressorTp1.wav", 'w')
        Set_Bits = 16/8
        output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))

        values = []
        for i in range(0, len(nuevo)):

                packed_value = struct.pack('<h', nuevo[i])

                values.append(packed_value)

        value_str = ''.join(values)
        output.writeframes(value_str)
        output.close()

        return nuevo




    def tipo2(self,):
        nuevo1=[]



        for i in range(0,len(self.wav)):

            if  self.wav[i]>self.threshold:
                if i<self.aframes:
                    compresion=((self.wav[i])-self.threshold)/self.n[i]
                    compresion1= compresion+self.threshold
                if i>self.aframes:

                    compresion=((self.wav[i])-self.threshold)/self.Ratio
                    compresion1= compresion+self.threshold


            elif  self.wav[i]<(-1*self.threshold):
                if i<self.aframes:
                    compresion=((self.wav[i])-self.threshold)/self.n[i]
                    compresion1= compresion+self.threshold
                if i>self.aframes:

                    compresion=((self.wav[i])-self.threshold)/self.Ratio
                    compresion1= compresion+self.threshold
                #nuevo.append(compresion)

            else:
                compresion1=self.wav[i]
                #nuevo.append(compresion)
            nuevo1.append(compresion1)

        output = wave.open("CompressorTp2.wav", 'w')
        Set_Bits = 16/8
        output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))

        values = []
        for i in range(0, len(nuevo1)):

                packed_value = struct.pack('<h', nuevo1[i])

                values.append(packed_value)

        value_str = ''.join(values)
        output.writeframes(value_str)
        output.close()
        print 'array del attack',self.n

        return nuevo1

    def closed(self):

        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()