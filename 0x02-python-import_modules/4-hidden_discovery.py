#!/usr/bin/python3

if __name__ == "__main__":
    '''
    Print names from a hidden module
    '''
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
