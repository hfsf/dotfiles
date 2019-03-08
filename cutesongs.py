# https://github.com/jiaaro/pydub
# Based on the gist: https://bit.ly/2VFiYgG

from pydub import AudioSegment
 
import sys

mp3_file = 'jorge_ben_tabua_esmeralda.mp3'

song_names = ["Os alquimistas estão chegando","O homem da gravata florida","Herrare, humanun est","Menina mulher da pele preta","Eu vou torcer","Magnólia","Minha teimosia, uma arma pra te conquistar","Zumbi","Brother","O namorado da viúva","Hermes Trismegisto e sua celeste tábua de esmeralda","Cinco minutos﻿"]
 
song_start_end = [[ [0.,0.] , [3,12] ],
                  [ [3.,14.] ,[6,18] ],
                  [ [6,20.] , [11,8] ],
                  [ [11,10] , [14,6] ],
                  [ [14,8] ,  [17,21] ],
                  [ [17,23] , [20,36] ],
                  [ [20,38] , [23,17] ],
                  [ [23,19] , [26,47] ],
                  [ [26,49] , [29,42] ],
                  [ [29,44] , [31,45] ],
                  [ [31,47] , [37,15] ],
                  [ [37,17] , [40,15] ]]

for i, song_i in enumerate(song_names):
 
        #Convert from min:sec to milisecs

        startTime = song_start_end[i][0][0]*60*1000 + song_start_end[i][0][1]*1000
 
        endTime = song_start_end[i][1][0]*60*1000 + song_start_end[i][1][1]*1000

        print("\nExtracting {} from {} [{}--{} msec]".format(song_i,mp3_file,startTime,endTime))

        song = AudioSegment.from_mp3(mp3_file)

        extract = song[startTime:endTime]

        extract.export(song_i+'.mp3',format="mp3")