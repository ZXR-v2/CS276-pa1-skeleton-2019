class CompressedPostings:
    #If you need any extra helper methods you can add them here 
    ### Begin your code
    @staticmethod
    def vbencode_number(n):
        byte = []
        while True:
            byte.append(n%128)
            if n < 128:
                break
            n = n // 128
        byte[0] += 128
        byte = list(reversed(byte))
        return byte
    ### End your code
    
    @staticmethod
    def encode(postings_list):
        """Encodes `postings_list` using gap encoding with variable byte 
        encoding for each gap
        
        Parameters
        ----------
        postings_list: List[int]
            The postings list to be encoded
        
        Returns
        -------
        bytes: 
            Bytes reprsentation of the compressed postings list 
            (as produced by `array.tobytes` function)
        """
        ### Begin your code
        bytestream = []
        last = 0
        for posting in postings_list:
            gap = posting - last
            last = posting
            byte = CompressedPostings.vbencode_number(gap)
            bytestream.extend(byte)
        return array.array('B', bytestream).tobytes()
        ### End your code

        
    @staticmethod
    def decode(encoded_postings_list):
        """Decodes a byte representation of compressed postings list
        
        Parameters
        ----------
        encoded_postings_list: bytes
            Bytes representation as produced by `CompressedPostings.encode` 
            
        Returns
        -------
        List[int]
            Decoded postings list (each posting is a docIds)
        """
        ### Begin your code
        decoded_postings_list = array.array('B')
        decoded_postings_list.frombytes(encoded_postings_list)
        numbers = []
        n = 0
        for i, byte in enumerate(decoded_postings_list):
            if byte < 128:
                n = 128*n + byte
            else:
                n = 128*n + byte-128
                numbers.append(n)
                n = 0
        prefix_sum = 0
        res = []
        for num in numbers:
            prefix_sum += num
            res.append(prefix_sum)
        return res
        ### End your code
