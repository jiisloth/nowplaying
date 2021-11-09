import subprocess
from time import sleep


with open('templates/nowplaying.html', 'r') as nowplaying:
    template = nowplaying.readlines()

while True:
    with open('out.txt', 'w+') as fout:
        with open('err.txt', 'w+') as ferr:
            out = subprocess.call(["rhythmbox-client", '--print-playing'], stdout=fout, stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            output = fout.read()
            # reset file to read from it
            ferr.seek(0)
            # save errors (if any) in variable
            errors = ferr.read()

    with open('output/nowplaying.html', 'w') as nowplaying:
        for line in template:
            formated = line.replace("{{ nowplaying }}", output)
            nowplaying.write(formated)
    sleep(1)