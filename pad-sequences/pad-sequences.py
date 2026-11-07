import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if (len(seqs) == 0):
        padded = np.zeros((0,0))
        return np.array(padded, dtype=int)
        
    if not max_len:
        max_l = 0
        for seq in seqs:
            leg = len(seq)
            if (max_l < leg):
                max_l = leg
    else:
        max_l = max_len
        
    for seq in seqs:
        if max_l < len(seq):
            # Truncate
            while max_l < len(seq):
                i = max_l
                seq.pop(i)
                ++i
        else:
            # Padding
            for i in range(max_l-len(seq)):
                seq.append(pad_value)

    return np.array(seqs)
    pass