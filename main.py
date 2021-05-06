from pyswip import Prolog


prolog = Prolog()

prolog.assertz('siblings(X,Y):-child(X,Z), child(Y,Z), X\\==Y')
prolog.assertz('brother(X,Y):-siblings(X,Y), male(X)')
prolog.assertz('sister(X,Y):-siblings(X,Y), female(X)')
prolog.assertz('male(friedrich)')
prolog.assertz('female(margarete)')
prolog.assertz('male(thomas)')
prolog.assertz('female(sandra)')
prolog.assertz('male(beni)')
prolog.assertz('male(giuliano)')
prolog.assertz('female(lucie)')
prolog.assertz('couple(friedrich, margarete)')
prolog.assertz('couple(X,Y):-couple(Y,X)')
prolog.assertz('parent(friedrich, thomas)')
prolog.assertz('parent(margarete, thomas)')
prolog.assertz('parent(thomas,giuliano)')
prolog.assertz('parent(sandra,giuliano)')
prolog.assertz('parent(thomas,beni)')
prolog.assertz('parent(thomas,lucie)')
prolog.assertz('father(X,Y):-parent(X,Y), male(X)')
prolog.assertz('mother(X,Y):-parent(X,Y), female(X)')
prolog.assertz('child(X,Y):-parent(Y,X)')
prolog.assertz('grandparent(X,Z):-parent(X,Y), parent(Y,Z)')
prolog.assertz('grandfather(X,Y):-grandparent(X,Y), male(X)')
prolog.assertz('grandmother(X,Y):-grandparent(X,Y), female(X)')
result = list(prolog.query("parent(thomas,X)")) == [{'X': 'giuliano'}, {'X': 'beni'}]
print(result)
for soln in prolog.query("parent(X,Y)"):
    print(soln["X"], "is the parent of", soln["Y"])
for kid in prolog.query('child(X,Y)'):
    print(kid['X'], 'is the child of', kid['Y'])
for gp in prolog.query('grandparent(X,Y)'):
    print(gp['X'], 'is a grandparent of', gp['Y'])
for gf in prolog.query('grandfather(X,Y)'):
    print(gf['X'], 'is a grandfather of', gf['Y'])
for gm in prolog.query('grandmother(X,Y)'):
    print(gm['X'], 'is a grandmother of', gm['Y'])
for sb in prolog.query('siblings(X,Y)'):
    print(sb['X'], 'is a sibling of', sb['Y'])
for br in prolog.query('brother(X,Y)'):
    print(br['X'], 'is a brother of', br['Y'])
for si in prolog.query('sister(X,Y)'):
    print(si['X'], 'is a sister of', si['Y'])
for cp in (prolog.query('couple(X,Y)')):
    print(f'{cp["X"]} and {cp["Y"]} is a couple.')

for x in prolog.query('parent(X,giuliano)'):
    print(x['X'])
