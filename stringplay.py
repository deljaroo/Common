
def join(list_, with_=''):
    """
    A replacment for the str method 'join'
    This is just a better looking way of doing it
    list_: a list that you want joined together
    with_: what to put between each item in the list
        e.g. join([1, 2, 3], '+') would make "1+2+3"
        excluding this will give you a joined list, but will convert all the
        items to strings first
    """
    return with_.join(list_)

def charToHex(what):
    """
    Converts a character to a string that has the hex of its "ASCII encoding"
    ord turns it into the dec of the ascii encoding
    hex turns it into the hex of the ascii encoding,
        but this is the python number type and not a string
    str turns it into a string, but with 0x before it
    [2:] remove the first two characters from a string
    upper() makes it uppercase as is typically expected
    """
    return str(hex(ord(what)))[2:].upper()

default_allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~/"
def desymbol(what, allowed=default_allowed):
    """
    Used to remove symbols from a string and replace them with url style
        replacements i.e. %20 replaces space, %25 replaces %, %2B replaces +
    By default, only URL 'allowed' characters are not encoded (letter, numbers,
        hyphen, period, underscore and tilde) and everything else is changed
    what:  the string that needs to be desymboled
    allowed:  override to change what characters are allowable
    """
    what = str(what)
    work = list(what)
    for i in range(len(work)):
        if work[i] not in allowed:
            n = charToHex(work[i])
            work[i] = "%" + n
    return join(work)