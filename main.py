import random
import re


RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
max_nonterminals = 10
max_expansion_trials = 100
log = True
max_number = 20



Grammar1 = {
    "<start>":
        ["ABaC"],

    "<Ba>":
        ["aaB"],

    "<BC>":
        ["DC", "E"],
    "<aD>":
        ["Da"],
    "<AD>":
        ["AB"],
    "<aE>":
        ["Ea"],
    "<AE>":
        ["m"]


}
Grammar = {
    "<start>":
        ["a <A> b","a<B>b"],

    "<A>":
        ["m", "n"],

    "<B>":
        ["p", "q"]


}

Grammar2 = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}


Start_symbol = "<start>"

def nonterminals(expansion):
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return RE_NONTERMINAL.findall(expansion)


check_number = 0
mylist = []

def simple_grammar_fuzzer(grammar,start_symbol, max_nonterminals,max_expansion_trials,log):
    global used_number
    global term
    global mylist
    for i in grammar.keys():
        a = i.replace("<","",1)
        b = a.replace(">","",1)
        mylist.append(b)
    term.append(start_symbol)
    expansion_trials = 0
    search_project(used_number,grammar)

    return 0


used_number = 0
term = []
result = []
count_number = 0
count_number1 = 0
mysentence = ''
def search_project(used_number,grammar):
  global count_number
  global count_number1
  global log
  global term
  global result
  count_number = count_number + 1
  if count_number == 30:
      count_number = count_number - 1
      return 0
  if log:
    a = 0
    for i in nonterminals(term[used_number]):
        if a == 0:
            mysentence = term[used_number]
        a = a+1
        symbol_to_expand = i
        expansions = grammar[symbol_to_expand]

        for d in expansions:
            if log:
             search1(d,symbol_to_expand,grammar,mysentence)
  count_number = count_number - 1
  return 0



def search1(d,symbol_to_expand,grammar,mysentence):
    expansion = d
    global count_number
    global count_number1
    global used_number
    global log
    global mylist
    new_term = mysentence.replace(symbol_to_expand, expansion, 1)
    for i in mylist:
        a = new_term.find(i)
        if a == 0:
            b = "<"+i+">"
            new_term = new_term.replace(i,b,1)
        elif a > 0:
            if new_term[a-1] == "<":
                continue
            else:
                c = "<" + i + ">"
                new_term = new_term.replace(i,c,1)



    print(count_number)
    if count_number1 == 4:
        log = False
        return 0


    if len(nonterminals(new_term)) == 0:
        result.append(new_term)
        count_number1 = count_number1 + 1
        return 0

    if len(nonterminals(new_term)) < max_nonterminals:
        used_number = used_number + 1
        term.append(new_term)
        if log:
            print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
        expansion_trials = 0
        search_project(used_number, grammar)
        return 0
    return 0
if __name__=="__main__":
    simple_grammar_fuzzer(Grammar1,Start_symbol,max_nonterminals,max_expansion_trials,log)
    print(result)