# Session Utils
# Python module to exploit Django's session utility

def sput(session, key, val):
    # put (key,val) to session data
    session[key] = val
    session.modified = True

def sget(session, key):
    # read from session data
    return session[key]
