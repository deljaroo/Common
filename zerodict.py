class ZeroDict:
    """
    This is a class that mimics the behavior of a dictionary, but instead of
    giving key errors or name errors when accessing parts of the dictionary
    that has yet to be setup, it instead sets that up and defaults the value
    to zero, ergo the name
    """
    def __init__(self):
        """
        Creation method.
        Very simple, it just makes a dictionary for the object
        """
        self._dict = {} # here is that dictionary
    def __setitem__(self, which, to_what):
        """
        This lets the object use square brace notation for setting
        """
        self._dict[which] = to_what
    def __getitem__(self, which):
        """
        This lets the object use square brace notation for requesting values
        out of the dictionary.
        This is the main idea of this class.  When requesting values that don't
        exist, it will make them exist and then set them to start at zero.
        """
        try:
            work = self._dict[which] # attempt normal dictionary behavior
        except (KeyError, NameError): # if that fails...
            self._dict[which] = 0 # ...make an entry
            work = 0
        return work
    def __str__(self):
        """
        Adds compatibility to these objects to be cast to strings
        """
        return(str(self._dict))
    def __iter__(self):
        """
        Adds compatibility to these objects to be iterated on. 
        """
        return iter(self._dict)
    def __contains__(self, what):
        """
        Used to check if a key has been made yet.
        """
        return what in self._dict