from subprocess import call
import os

url = 'https://pl.crunchyroll.com/evs3/d7039a334d000db5e472162e0fcf2191/assets/973b54d921ebec6f312b6d3924935255_4299351.mp4/index-v1-a1.m3u8?Expires=1662394490&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wbC5jcnVuY2h5cm9sbC5jb20vZXZzMy9kNzAzOWEzMzRkMDAwZGI1ZTQ3MjE2MmUwZmNmMjE5MS9hc3NldHMvOTczYjU0ZDkyMWViZWM2ZjMxMmI2ZDM5MjQ5MzUyNTVfNDI5OTM1MS5tcDQvaW5kZXgtdjEtYTEubTN1OCIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY2MjM5NDQ5MH19fV19&Signature=rR2bncwnMLvDAJpMcrkGtZqGetG~ohxzNqK1DxtJoFwxgnBPaUK4rgTi2ff~MzoQ7K8yNcLcPGDx6ghurGpsOgbUzVRpqn~IxoAmVddRQPehRdj1B7EqoQi6ev0K14ajYaCA2gLFR2iI0GdtBQ6o5MLmSNArj4s0zfBszZaYxFw86LbaTQ8Ji-PcoTlhaVipHGcxhFpxiGGni2uk3ZuA1nFvd7U4T30tLOEq1aqPVKeCLXTxlvDjqQqqfWnOi7L9YiEq2uzcvcsP1uf8wIJVMcAJMAxpp8l9LT9ZKz7n8YyHizJOc8J5S~s-ViI8JbQ66uP25eBzDDWPkptLdWxp9A__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA'


# -allowed_extensions ALL -protocol_whitelist file,http,https,tcp,tls,crypto -i url -c copy -bsf:a aac_adtstoasc video2.mp4  

command = [
    'ffmpeg',
    '-allowed_extensions=ALL',
    '-protocol_whitelist file,http,https,tcp,tls,crypto',
    '-i', url, 
    '-c copy',
    '-bsf:a aac_adtstoasc',
    'video2.mp4'
  
]

file_name = 'kola.mp4'
file_file = 'try.m3u8'
command = ''.join(['ffmpeg -allowed_extensions ALL -protocol_whitelist file,http,https,tcp,tls,crypto -i "', url, '" -c:v copy -c:a copy -f mp4 "out/', file_name, '"'])
# process = call(command, shell=False)
os.system(command)
# process = call(command, shell=False)
