class InvertedIndexMapper(InvertedIndex):
    def __getitem__(self, key):
        return self._get_postings_list(key)
    
    def _get_postings_list(self, term):
        """Gets a postings list (of docIds) for `term`.
        
        This function should not iterate through the index file.
        I.e., it should only have to read the bytes from the index file
        corresponding to the postings list for the requested term.
        """
        ### Begin your code
        postings_start, postings_num, postings_bytes = self.postings_dict[term]
        self.index_file.seek(postings_start, 0)
        postings_bin = self.index_file.read(postings_bytes)
        postings = self.postings_encoding.decode(postings_bin)
        return postings
        ### End your code
