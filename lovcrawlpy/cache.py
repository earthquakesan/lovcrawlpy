import os.path
import requests
import cPickle as pickle

from cfg import rootFolder

class Cache(object):
    cacheFolder = os.path.join(rootFolder, "cache/")
    vocabulariesFolder = os.path.join(rootFolder, "vocabularies/")
    lovDownloadLink = "https://dl.dropboxusercontent.com/u/4882345/lov-dumps/lov-last.rdf"

    def __init__(self):
        pass

    def updateLovDataset(self):
        r = requests.get(self.lovDownloadLink)
        with open(self.getLovPath(), "wb+") as fd:
            for chunk in r.iter_content(512):
                fd.write(chunk)

    def getLovPath(self):
        return os.path.join(self.cacheFolder, "lov.rdf")

    def getFile(self, filename, filetype=None):
        if(filetype is None):
            filepath = os.path.join(self.cacheFolder, filename)
        elif(filetype == "vocabulary"):
            filepath = os.path.join(self.vocabulariesFolder, filename)

        if(os.path.exists(filepath)):
            return pickle.load(open(filepath, 'rU'))
        else:
            return False

    def setFile(self, obj, filename, filetype=None):
        if(filetype is None):
            filepath = os.path.join(self.cacheFolder, filename)
        elif(filetype == "vocabulary"):
            filepath = os.path.join(self.vocabulariesFolder, filename)
        pickle.dump(obj, open(filepath, 'wb+'), -1)


if __name__ == "__main__":
    cache = Cache()
    import ipdb; ipdb.set_trace()
