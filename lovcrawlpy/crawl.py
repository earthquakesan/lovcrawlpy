import RDF
from cache import Cache

class LovCrawler(object):
    def __init__(self):
        self.cache = Cache()
        self.lovModel = self.getLovModel()
        pass

    def getLovModel(self):
        lovPath = self.cache.getLovPath()
        parser = RDF.Parser()
        storage = RDF.HashStorage("abc", options="hash-type='memory'")
        model = RDF.Model(storage)
        parser.parse_into_model(model, "file:"+lovPath)
        return model

    def getVocabularyUris(self):
        vocabularyUrisCacheFile = "vocabularyUris.cache"
        vocabularyUris = self.cache.getFile(vocabularyUrisCacheFile)
        if(not vocabularyUris):
            vocabularyUris = {}
            query = RDF.Query("SELECT DISTINCT ?s ?o WHERE {?s <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> ?o.}")
            for result in query.execute(self.lovModel):
                vocabularyId = str(result['s'])
                vocabularyUri = str(result['o'])
                vocabularyUris[vocabularyId] = vocabularyUri
            self.cache.setFile(vocabularyUris, vocabularyUrisCacheFile)
        return vocabularyUris

    def downloadVocabularies(self):
        vocabularies = self.getVocabularyUris()
        for vocabulary in vocabularies:
            print vocabularies[vocabulary]
            extension = vocabularies[vocabulary].split('.')[-1]
            print extension

if __name__ == "__main__":
    crawler = LovCrawler()
    vu = crawler.downloadVocabularies()
    import ipdb; ipdb.set_trace()
