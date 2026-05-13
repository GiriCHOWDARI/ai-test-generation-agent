from sentence_transformers import SentenceTransformer, util
from typing import List
from schemas import GeneratedTest

model = SentenceTransformer('all-MiniLM-L6-v2')

def remove_duplicates(tests: List[GeneratedTest], threshold: float = 0.95) -> List[GeneratedTest]:
    if not tests:
        return []
    codes = [t.code for t in tests]
    embeddings = model.encode(codes, convert_to_tensor=True)
    keep = []
    for i, test in enumerate(tests):
        dup = False
        for j in keep:
            sim = util.cos_sim(embeddings[i], embeddings[j]).item()
            if sim > threshold:
                dup = True
                break
        if not dup:
            keep.append(i)
    return [tests[i] for i in keep]