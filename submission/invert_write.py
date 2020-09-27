class BSBIIndex(BSBIIndex):
    def invert_write(self, td_pairs, index):
        """Inverts td_pairs into postings_lists and writes them to the given index
        
        Parameters
        ----------
        td_pairs: List[Tuple[Int, Int]]
            List of termID-docID pairs
        index: InvertedIndexWriter
            Inverted index on disk corresponding to the block       
        """
        ### Begin your code
        td_pairs = sorted(td_pairs, key=lambda x: self.term_id_map[x[0]])
        postings = []
        last_term = ''
        for pair in td_pairs:
            if pair[0] != last_term:
                if last_term != '':
                    index.append(last_term, list(set(postings))) # 保存上一个不同值的结果
                postings = [] # 重新置空
                postings.append(pair[1])
                last_term = pair[0]
            else:
                postings.append(pair[1])
        if last_term:
            index.append(last_term, list(set(postings)))
        ### End your code
