
import heapq
class BSBIIndex(BSBIIndex):
    def merge(self, indices, merged_index):
        """Merges multiple inverted indices into a single index
        
        Parameters
        ----------
        indices: List[InvertedIndexIterator]
            A list of InvertedIndexIterator objects, each representing an
            iterable inverted index for a block
        merged_index: InvertedIndexWriter
            An instance of InvertedIndexWriter object into which each merged 
            postings list is written out one at a time
        """
        ### Begin your code
        last_term = ''
        last_postings = []
        for term_id, postings in heapq.merge(*indices, key=lambda x: self.term_id_map[x[0]]):
            if term_id != last_term:
                if last_term != '':
                    merged_index.append(last_term, last_postings)
                last_term = term_id
                last_postings = postings
            else:
                i, j = 0, 0
                new_postings = []
                while i<len(postings) and j<len(last_postings):
                    if postings[i]<last_postings[j]:
                        new_postings.append(postings[i])
                        i += 1
                    elif postings[i]>last_postings[j]:
                        new_postings.append(last_postings[j])
                        j += 1
                    else:
                        new_postings.append(postings[i])
                        i += 1
                        j += 1
                if i < len(postings):
                    new_postings.extend(postings[i:len(postings)])
                elif j < len(last_postings):
                    new_postings.extend(postings[j:len(last_postings)])
                last_postings = new_postings
                del new_postings
        if last_term:
            merged_index.append(last_term, last_postings)
        ### End your code
