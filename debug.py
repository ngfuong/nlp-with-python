def get_last(text_list, word, index, prev_index) -> int:
    if index == 0:
        prev_index = index
        index = text_list.index(word, index)
    else:
        prev_index = index
        try:
            index = text_list.index(word, index+1)
        except ValueError:
            return prev_index
    return get_last(text_list, word, index, prev_index)
    
sent3_list = \
['In',
 'the',
 'beginning',
 'God',
 'created',
 'the',
 'heaven',
 'and',
 'the',
 'earth',
 '.']
print(get_last(sent3_list, 'the', 0, None))

