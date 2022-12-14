from py_aho_corasick import py_aho_corasick

# keywords only
A = py_aho_corasick.Automaton(['cash', 'shew', 'ew'])
text = "cashew"
for idx,k,v in A.get_keywords_found(text):
    assert text[idx:idx+len(k)] == k

# keywords and values
kv = [('cash',1), ('shew',2), ('ew',3)]
A = py_aho_corasick.Automaton(kv)
text = "cashew"
for idx,k,v in A.get_keywords_found(text):
    assert text[idx:idx+len(k)] == k
    assert v == dict(kv)[k]

A = py_aho_corasick.Automaton(['透视眼', '透视', '透视镜'])
text = "透视功能透视镜透视扑透视器透视眼睛透视眼镜"
results = A.get_keywords_found(text)
print(results)
for idx,k,v in results:
    assert text[idx:idx+len(k)] == k