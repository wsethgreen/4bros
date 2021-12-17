

def _reformat_column_name(word: str) -> str:
    new_word: str = word.replace(' ', '_').replace('.', '').replace('-', '_').replace('+', '_plus').replace('#', 'number').replace('20', 'twenty').replace("'", '').lower()
    return new_word


def _reformat_table_name(word: str) -> str:
    new_word: str = word.replace(' ', '_').replace('/', '_').lower()
    return new_word