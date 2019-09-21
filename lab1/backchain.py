from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES
import string
# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.
rule1=(
    IF( AND( '(?x) has (?y)',
            '(?x) has (?z)' ),
        THEN( '(?x) has (?y) and (?z)' ) ),
    IF(AND('(?x) has rhythm and music'),
            THEN( '(?x) could not ask for anything more' ) ),
    )
ARBITRARY_EXP = (
    IF( AND( 'a (?x)',
             'b (?x)' ),
        THEN( 'c d' '(?x) e' )),
    IF( OR( '(?y) f e',
            '(?y) g' ),
        THEN( 'h (?y) j' )),
    IF( AND( 'h c d j',
             'h i j' ),
        THEN( 'zot' )),
    IF( '(?z) i',
        THEN( 'i (?z)' ))
    )
antelist=list()
liste=list()
def myfunc3(rule,deneme):
    eleman=AND()
    for liste in populate(rule.antecedent(),deneme):
        if not liste in antelist:
            antelist.append(liste)
            eleman.append(liste)
    return eleman
def myfunc2(rule,rules,hypothesis,deneme):
    yedek=OR()
    for rule in rules:
        for cons in rule.consequent():
            #print(cons)
            if match(cons,hypothesis):
                deneme=match(cons,hypothesis)
                #print(rule.antecedent())
                antelist.append(hypothesis)
                yedek.append(hypothesis)
                gelendeger=myfunc(rule,rules,deneme,hypothesis)
                if gelendeger!=OR():
                    yedek.append(gelendeger)
                else:
                    yedek.append(populate(rule.antecedent(),deneme))
                
               
    #print(simplify(yedek))
    return  yedek

def myfunc(rule,rules,deneme,hypothesis):
    yedek=OR()

    for ante in rule.antecedent():
        deger=myfunc2(rule,rules,populate(ante,deneme),deneme)
        #print(deger)
        if deger!=OR() and deger!=rule.antecedent():
            yedek.append(deger)
            #print(yedek)
    #print(populate(ante,deneme))
    #print(simplify(yedek))
    if yedek==OR():
        return OR()
    #return AND(yedek,populate(ante,deneme))
    if type(rule.antecedent())==OR:
        return OR(yedek,myfunc3(rule,deneme))
    return AND(yedek,myfunc3(rule,deneme))
# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.
def backchain_to_goal_tree(rules, hypothesis):
    i=0
    tree=OR()
    
    for rule in rules:
        #for ante in rule.antecedent():
                #if i>=1 and i<len(rule.antecedent()):
                    #birsey.append(ante)
                #i+=1  
        for cons in rule.consequent():
           if match(cons,hypothesis) or hypothesis==cons:
               deneme=match(cons,hypothesis)
               #bakalim=(backchain_to_goal_tree,populate(rule.antecedent(),deneme),rules)
               #print(rule) 
               tree.append(OR(hypothesis,myfunc(rule,rules,deneme,hypothesis)))
    if tree ==OR():
        return ['stuff']
    antelist.clear()
    return simplify(tree)
# Here's an example of running the backward chainer - uncomment
# it to see it work:
#print (backchain_to_goal_tree(ZOOKEEPER_RULES, 'geoff is a giraffe'))
#print (backchain_to_goal_tree(rule1,'gershwin could not ask for anything more'))
#print (backchain_to_goal_tree(ARBITRARY_EXP,'zot'))



