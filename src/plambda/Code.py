from src.util.StringBuffer import StringBuffer

#may as well retain information gleaned from the parser
#since it will help in the dispatching
class Syntax(object):

    SEQ               = 0
    LET               = 1
    DEFINE            = 2
    LAMBDA            = 3
    INVOKE            = 4
    APPLY             = 5
    PRIMITIVE_DATA_OP = 6
    UNARY_OP          = 7
    BINARY_OP         = 8
    TERNARY_OP        = 9
    AMBI1_OP          = 10
    AMBI2_OP          = 11
    N_ARY_OP          = 12
    TRY               = 13
    FOR               = 14
    QUOTE             = 15
    CATCH             = 16


class SExpression(object):

    def __init__(self, code, spine, filename, lineno):
        self.code = code
        self.spine = spine
        self.filename = filename
        self.lineno = lineno
        self.string = self.toString()


    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}@{1}:{2}'.format(self.string, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.string


    def toString(self):
        sb = StringBuffer()
        first = True
        sb.append('(')
        for c in self.spine:
            if first:
                first = False
            else:
                sb.append(' ')
            sb.append(str(c))
        sb.append(')')
        return str(sb)
    


class Atom(object):

    def __init__(self, uni, filename, lineno):
        self.string = intern(str(uni))
        self.filename = filename
        self.lineno = lineno

    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}@{1}:{2}'.format(self.string, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.string

class StringLiteral(object):

    def __init__(self, uni, filename, lineno):
        self.string = intern(str(uni)[1:-1]) # remove the quotes
        self.filename = filename
        self.lineno = lineno

    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}@{1}:{2}'.format(self.string, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.string

