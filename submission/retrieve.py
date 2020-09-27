class BSBIIndex(BSBIIndex):
    def retrieve(self, query):
        """Retrieves the documents corresponding to the conjunctive query
        
        Parameters
        ----------
        query: str
            Space separated list of query tokens
            
        Result
        ------
        List[str]
            Sorted list of documents which contains each of the query tokens. 
            Should be empty if no documents are found.
        
        Should NOT throw errors for terms not in corpus
        """
        if len(self.term_id_map) == 0 or len(self.doc_id_map) == 0:
            self.load()

        ### Begin your code
        query_list = [token.strip() for token in query.split(' ')]
        heap = []
        with InvertedIndexMapper(self.index_name, directory=self.output_dir, postings_encoding=
                                 self.postings_encoding) as mapper:
            for token in query_list:
                postings = mapper[self.term_id_map[token]]
                heapq.heappush(heap, (len(postings),postings))
            while len(heap)>1:
                list1 = heapq.heappop(heap)[1]
                list2 = heapq.heappop(heap)[1]
                tmp = sorted_intersect(list1, list2)
                heapq.heappush(heap, (len(tmp), tmp))
        result = [self.doc_id_map[doc_id] for doc_id in heap[0][1]]
        return result
        ### End your code
