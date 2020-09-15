from sly import Parser
from cicom_lexer import CicomLexer

class CicomParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CicomLexer.tokens

    # Grammar rules and actions
    @_('')
    def exp(self, p):
        pass

    @_('term binopexps')
    def exp(self, p):
        return ('init_exp', p.term, p.binopexps)

    @_('IF exp THEN exp ELSE exp')
    def exp(self, p):
        return ('if_exp', p.exp0, ('branch', p.exp1, p.exp2))

    @_('LET defs IN exp')
    def exp(self, p):
        return ('let_exp', p.defs, p.exp)

    @_('MAP idlist TO exp')
    def exp(self, p):
        return ('map_exp', p.idlist, p.exp)

    @_('binopexp binopexp')
    def binopexps(self, p):
        return ('binop_exps', p.binopexp, p.binopexp)

    @_('binopexp')
    def binopexps(self, p):
        return p.binopexp

    @_('binop exp')
    def binopexp(self, p):
        return ('binop_exp', p.binop, p.exp)

    @_('adef adef')
    def defs(self, p):
        return ('defs', p.adef0, p.adef1)

    @_('adef')
    def defs(self, p):
        return p.adef

    @_('ID ISEQUAL exp ";"')
    def adef(self, p):
        return ('def', p.ID, p.exp)

    @_('unop term')
    def term(self, p):
        return ('unop_term', p.unop, p.term)
    
    @_('factor delimexplists')
    def term(self, p):
        return ('factor_term', p.factor, p.explist)

    @_('factor')
    def term(self, p):
        return p.factor 

    @_('EMPTY')
    def term(self, p):
        return p.EMPTY
    
    @_('INT')
    def term(self, p):
        return p.INT 

    @_('BOOL')
    def term(self, p):
        return p.BOOL

    @_('"(" exp ")"')
    def factor(self, p):
        return p.exp

    @_('PRIM')
    def factor(self, p):
        return p.PRIM

    @_('ID')
    def factor(self, p):
        return p.ID

    @_('delimexplist delimexplist')
    def delimexplists(self, p):
        return ('delimexplists', p.delimexplist0, p.delimexplist1)

    @_('delimexplist')
    def delimexplists(self, p):
        return p.explist

    @_('"(" explist ")"')
    def delimexplist(self, p):
        return p.explist

    @_('propexplists')
    def explist(self, p):
        return p.propexplists

    @_('')
    def explist(self, p):
        return 'EMPTY'

    @_('propexplists propexplists')
    def propexplists(self, p):
        return ('propexplists', p.propexplists0, p.propexplists1)

    @_('propexplist')
    def propexplists(self, p):
        return p.propexplist

    @_('exp "," propexplist')
    def propexplist(self, p):
        return ('prop_exp_list', p.exp, p.propexplist)

    @_('exp')
    def propexplist(self, p):
        return p.exp

    @_('propidlists')
    def idlist(self, p):
        return p.propidlists

    @_('')
    def idlist(self, p):
        return 'EMPTY'

    @_('propidlists propidlists')
    def propidlists(self, p):
        return ('prop_id_lists', p.propidlists0, p.propidlists1)

    @_('propidlist')
    def propidlists(self, p):
        return p.propidlist

    @_('ID "," propidlist')
    def propidlist(self, p):
        return ('prop_id_list', p.ID, p.propidlist)

    @_('ID')
    def propidlist(self, p):
        return p.ID

    @_('PLUS')
    def factor(self, p):
        return p.PLUS

    @_('sign')
    def unop(self, p):
        return p.sign

    @_('TILDE')
    def unop(self, p):
        return p.TILDE

    @_('sign')
    def binop(self, p):
        return p.sign

    @_("STAR")
    def binop(self, p):
        return p.STAR

    @_("SLASH")
    def binop(self, p):
        return p.SLASH

    @_("EQUAL")
    def binop(self, p):
        return p.EQUAL

    @_("NEQUAL")
    def binop(self, p):
        return p.NEQUAL

    @_("LTHAN")
    def binop(self, p):
        return p.LTHAN

    @_("GTHAN")
    def binop(self, p):
        return p.GTHAN

    @_("LETHAN")
    def binop(self, p):
        return p.LETHAN

    @_("GETHAN")
    def binop(self, p):
        return p.GETHAN

    @_("AMPERSAND")
    def binop(self, p):
        return p.AMPERSAND

    @_("BAR")
    def binop(self, p):
        return p.BAR

    @_("PLUS")
    def sign(self, p):
        return p.PLUS

    @_("MINUS")
    def sign(self, p):
        return p.MINUS

if __name__ == '__main__':
    lexer = CicomLexer()
    parser = CicomParser()
    f = open("test.txt", "r")
    data = f.read()
    
    print (parser.parse(lexer.tokenize(data)))