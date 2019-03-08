from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'ignoreerrors':True,
    'format': 'bestaudio/best',
    'ignore'
	'outtmpl':'%(title)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)


with open('links','r') as flinks:

	try:	

		ydl.download(flinks.readlines())

	except:

		pass
