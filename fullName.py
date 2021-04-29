def full_name(fname, lname):
    if (type(fname) is not str or type(lname) is not str):
        return "Strings only"

    full = fname + " " + lname
    return full