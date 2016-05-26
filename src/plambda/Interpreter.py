from Code import SExpression, Atom, Syntax
from SymbolTable import SymbolTable

"""
Current bugs:
(int None)
(boolean None)
(float None)



"""


class Interpreter(object):

    def __init__(self):
        self.definitions = {}
        self.modules = {}


    def evaluate(self, exp):
        if isinstance(exp, Atom):
            return self.lookup(exp)
        elif isinstance(exp, SExpression):
            return self.evalSExpression(exp)
        else:
            raise Exception("huh?")

    def lookup(self, leaf):
        return True


    def evalSExpression(self, sexp):
        code = sexp.code
        if code == Syntax.SEQ:
            print 'SEQ: coming soon to an interpreter near you!'
        elif code == Syntax.LET:
            print 'LET: coming soon to an interpreter near you!'
        elif code == Syntax.DEFINE:
            print 'DEFINE: coming soon to an interpreter near you!'
        elif code == Syntax.LAMBDA:
            print 'LAMBDA: coming soon to an interpreter near you!'
        elif code == Syntax.INVOKE:
            print 'INVOKE: coming soon to an interpreter near you!'
        elif code == Syntax.APPLY:
            print 'APPLY: coming soon to an interpreter near you!'
        elif code == Syntax.PRIMITIVE_DATA_OP :
            return self.evalPrimitiveDataOp(sexp)
        elif code == Syntax.UNARY_OP:
            return self.evalUnaryOp(sexp)
            print 'UNARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.BINARY_OP:
            print 'BINARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.TERNARY_OP:
            print 'TERNARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.AMBI1_OP:
            print ': coming soon to an interpreter near you!'
        elif code == Syntax.AMBI2_OP:
            print 'AMBI2_OP: coming soon to an interpreter near you!'
        elif code == Syntax.N_ARY_OP:
            print 'N_ARY_OP: coming soon to an interpreter near you!'
        elif code == Syntax.TRY:
            print 'TRY: coming soon to an interpreter near you!'
        elif code == Syntax.FOR:
            print 'FOR: coming soon to an interpreter near you!'
        elif code == Syntax.QUOTE:
            print 'QUOTE: coming soon to an interpreter near you!'
        else:
            raise Exception("huh?")

    def evalPrimitiveDataOp(self, sexp):
        (a0, a1) = sexp.spine
        assert isinstance(a0, Atom)
        assert isinstance(a1, Atom)
        op = a0.string
        data = a1.string
        if op is SymbolTable.INT:
            return int(data)
        elif op is SymbolTable.FLOAT:
            return float(data)
        else:
            return True if data.lower() == 'true' else False
        
        
    def evalUnaryOp(self, sexp):
        (uop, arg) =  sexp.spine
        assert isinstance(uop, Atom)
        op = uop.string
        val = self.evaluate(arg)
        print "op = {0}".format(op)
        if  op is SymbolTable.LOAD:
            pass
        elif op is SymbolTable.IMPORT:
            pass
        elif op is SymbolTable.ISNONE:
            pass
        elif op is SymbolTable.ISOBJECT:
            pass
        elif op is SymbolTable.QUOTE:
            pass
        elif op is SymbolTable.THROW:
            pass
        elif op is SymbolTable.NOT:
            pass
        else:
            raise Exception("huh?")
        print 'UNARY_OP {0}: coming soon to an interpreter near you!'.format(op)
        return True
