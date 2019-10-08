def split_tokens(texts):
    import string
    """Split strings into tokens by white space"""
    tokens = [word.split() for word in texts]
    return tokens

def clean_punctuation(texts):
    """Remove punctuation from strings"""
    import string
    cleaned_tokens = [[word.strip(string.punctuation) for word in sentence] for sentence in texts]
    return cleaned_tokens

def represent_references(reference1, reference2, candidate_sentences):
    """Represent references to pass to corpus_bleu"""
    refs = [reference1[:] + reference2[:]] * candidate_sentences
    return refs