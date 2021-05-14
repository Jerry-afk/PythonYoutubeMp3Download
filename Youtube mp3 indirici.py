from pytube import YouTube
link= input("Link giriniz  ")
YouTube(link).streams.get_audio_only().download()


