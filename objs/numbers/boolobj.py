from objs import intobj, pyobj
class boolobj(intobj, pyobj):
    """ A boolean - either True or False. """
    _regex = r'\b([Tt]rue|[Ff]alse)\b'
    _pyobj = bool
    _pyobj_rank = 0

    # @classmethod
    # def fromstr(self: type, data: str, consts: 'constants') -> 'obj':
    #     return data[0] in 'Tt' and True or False