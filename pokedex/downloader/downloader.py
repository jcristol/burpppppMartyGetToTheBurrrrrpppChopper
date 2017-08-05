import gevent, urllib2, os, errno, shutil, base64
import json
from gevent import monkey

#Globals

base_dir = 'data'

#Functions

"""
Try and make a directory
failure(exists) : delete and remake
failure(other) : probably a thread exception just raise the error
"""
def make_dir(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        else:
            shutil.rmtree(directory)
            make_dir(directory)

def download_image(src, dest):
    resource = urllib2.urlopen(src)
    output = open(dest,"wb")
    output.write(resource.read())
    output.close()

def process_morty(morty):
    name = morty['title'].replace(" ", "_")
    mortyDir = base_dir + '/' + name
    #make this morty's base directory
    make_dir(mortyDir)
    #record json in a info.json
    jFile = open(mortyDir + "/info.json","w+")
    jFile.write(json.dumps(morty))
    #something is wrong with my strings
    # download_image(morty["big_image"]["src"], mortyDir + "/big_image.png")
    # #download full image
    import code
    code.interact(local=locals())
    # urllib.urlretrieve(morty["big_image"]["src"], mortyDir + "/big_image.png")
    # #download icon
    # urllib.urlretrieve(morty["lil_icon"]["src"], mortyDir + "/icon.png")
    # #download type picture
    # urllib.urlretrieve(morty['basic_info']['type_info']['src'], mortyDir + "/type.png")







#Main Code

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

#json objects
mortys = json.loads(open('morty_info.json', 'r').read())
sounds = json.loads(open('sounds.json', 'r').read())

#make a data directory this is the deliverable

make_dir(base_dir)
jobs = [gevent.spawn(process_morty, morty) for morty in mortys]
gevent.joinall(jobs)
print("all done")
