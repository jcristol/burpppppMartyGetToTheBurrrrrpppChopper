import urllib, os, errno, shutil, base64
import json

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

def process_morty(morty):
    name = morty['article']['title'].replace(" ", "_")
    mortyDir = base_dir + '/' + name
    #make this morty's base directory
    make_dir(mortyDir)
    morty['error'] = []
    #record json in a info.json
    try:
        print "Downloading big image for %s" % name
        # #download full image
        urllib.urlretrieve(morty["big_image"]["src"], mortyDir + "/big_image.png")
    except:
        print "Error downloading big image for %s" % name
        morty['error'].append({'big_image' : True})
    try:
        print "Downloading icon image for %s" % name
        urllib.urlretrieve(morty["lil_icon"]["src"], mortyDir + "/icon.png")
    except:
        print "Error downloading icon image for %s" % name
        morty['error'].append({'icon' : True})
    try:
        print "Downloading type image for %s" % name
        urllib.urlretrieve(morty['basic_info']['type_info']['src'], mortyDir + "/type.png")
    except:
        print "Error downloading type image for %s" % name
        morty['error'].append({'type' : True})

    #record json in a info.json
    jFile = open(mortyDir + "/info.json","w+")
    jFile.write(json.dumps(morty))

#json objects
mortys = json.loads(open('morty_info.json', 'r').read())
sounds = json.loads(open('sounds.json', 'r').read()
#fetch all the wiki morty information
make_dir(base_dir)
[process_morty(morty) for morty in mortys]
print("all done")
