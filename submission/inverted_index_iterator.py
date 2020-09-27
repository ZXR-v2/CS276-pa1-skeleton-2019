class InvertedIndexIterator(InvertedIndex):
    """"""
    def __enter__(self):
        """Adds an initialization_hook to the __enter__ function of super class
        """
        super().__enter__()
        self._initialization_hook()
        return self

    def _initialization_hook(self):
        """Use this function to initialize the iterator
        """
        ### Begin your code
        self.start = 0
        self.num = len(self.postings_dict.keys())
        ### End your code

    def __iter__(self): 
        return self
    
    def __next__(self):
        """Returns the next (term, postings_list) pair in the index.
        
        Note: This function should only read a small amount of data from the 
        index file. In particular, you should not try to maintain the full 
        index file in memory.
        """
        ### Begin your code
        if self.start < self.num:
            term_id = self.term_iter.__next__()
            postings_start, postings_num, postings_bytes = self.postings_dict[term_id]
            self.index_file.seek(0, 1) # 第二个参数是whence，代表0是从文件头开始， 1是从现在位置， 2是从最后开始读。连续读写效率高，故whence为1
            postings_bin = self.index_file.read(postings_bytes)
            postings = self.postings_encoding.decode(postings_bin)
            self.start += 1
            return (term_id, postings)
        else:
            raise StopIteration
        ### End your code

    def delete_from_disk(self):
        """Marks the index for deletion upon exit. Useful for temporary indices
        """
        self.delete_upon_exit = True

    def __exit__(self, exception_type, exception_value, traceback):
        """Delete the index file upon exiting the context along with the
        functions of the super class __exit__ function"""
        self.index_file.close()
        if hasattr(self, 'delete_upon_exit') and self.delete_upon_exit:
            os.remove(self.index_file_path)
            os.remove(self.metadata_file_path)
        else:
            with open(self.metadata_file_path, 'wb') as f:
                pkl.dump([self.postings_dict, self.terms], f)
