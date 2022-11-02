# cipher function

def cipher(text, shift, encrypt=True):
    '''
    Encrypts or decrypt the text
    ----------
    text: str
        Input string to be encrypted or decrypted.
    shift: int
        Integer value for shifting.
    encrypt: bool
        A boolean to determine if encryption is required.
    Returns
    -------
    new_text: str
        The encrypted or decrypted text. 
    Examples
    --------
    >>> from cipher_cy2617 import cipher
    >>> text = str('Ag')
    >>> shift = int(1)
    >>> encrypt = False
    >>> cipher_cy2617.cipher('Ag', 1, False)
        'Bh'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
