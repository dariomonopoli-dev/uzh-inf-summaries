def where_is_waldo(names):
    if not 'Waldo' in names:
        return None
    else:
        return names.index('Waldo')

