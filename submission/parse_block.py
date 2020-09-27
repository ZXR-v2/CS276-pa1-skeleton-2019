class BSBIIndex(BSBIIndex):            
    def parse_block(self, block_dir_relative):
        """Parses a tokenized text file into termID-docID pairs
        
        Parameters
        ----------
        block_dir_relative : str
            Relative Path to the directory that contains the files for the block
        
        Returns
        -------
        List[Tuple[Int, Int]]
            Returns all the td_pairs extracted from the block
        
        Should use self.term_id_map and self.doc_id_map to get termIDs and docIDs.
        These persist across calls to parse_block
        """
        ### Begin your code
        dir_path = os.path.join(self.data_dir, block_dir_relative)
        td_pairs = []
        for doc_name in os.listdir(dir_path):
            with open(os.path.join(dir_path, doc_name), 'r') as f:
                for line in f.readlines():
                    tokens = line.split(' ')
                    for token in tokens:
                        term_id = self.term_id_map[token.strip()]
                        doc_id = self.doc_id_map[os.path.join(block_dir_relative, doc_name)]
                        td_pairs.append((term_id, doc_id))
        return td_pairs
        ### End your code
