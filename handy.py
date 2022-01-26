def yesNo(ink, good=('yes', 'y', 'no', 'n')):
    """
    A little tool for checking if user-input is yes or no (or y/n)
    The purpose of this is hard to explain, see doThis() for an example
    you can override what is considered a valid answer by using the good keyword
    """
    return ink.lower() not in good
    
def doThis(prompt="Continue?"):
    """
    Prompts the user (in the terminal) a yes or no question.
    Will loop until they say either yes or no (y/n is also fine)
    prompt:  what to say in the prompt
    returns True if they said yes, False if they said no
    """
    ink = ""
    while yesNo(ink):
        ink = input(prompt + " ").lower()
    return ink=='yes' or ink=='y'