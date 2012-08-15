#!/usr/bin/env python

from gedcom import *

g = Gedcom('zappala.ged')

# set print_type to 'gedcom' to print the relevant gedcom information
# print_type = 'gedcom'
print_type = 'names'

print "======================================================================"
print " Zappala "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.surname_match("Zap"):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Maria "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.given_match("Maria"):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Born 1857 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.birth_year_match(1857):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Born 1800 - 1810 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.birth_range_match(1800,1810):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Died 1857 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.death_year_match(1857):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Died 1850 - 1860 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.death_range_match(1850,1860):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Married 1857 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.marriage_year_match(1857):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Married 1850 - 1860 "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.marriage_range_match(1850,1860):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Family of Maria Nicotra "
print "======================================================================"
for e in g.element_list():
    if e.individual():
        if e.surname_match('Nicotra') and e.given_match('Maria'):
            for f in e.families():
                print f.get_family()

print "======================================================================"
print " Criteria Matching "
print "======================================================================"
criteria = "surname=Zappala:birthrange=1820-1840:deathrange=1900-1910"
for e in g.element_list():
    if e.individual():
        if e.criteria_match(criteria):
            if print_type == 'names':
                print e.name()
            elif print_type == 'gedcom':
                print e.get_individual()

print "======================================================================"
print " Missing Pointer "
print " (Tells you if any records are missing from your Gedcom file) "
print "======================================================================"
for e in g.element_list():
    if e.value().startswith('@'):
        f = g.element_dict().get(e.value(),None)
        if f == None:
            print e.value()

for e in g.element_list():
    if e.pointer() == "@I99@":
        print e.name()

# The following two functions are what I use to find a person matching
# given criteria and all the families a given person belongs to

def gedcom_criteria(criteria):
    print "looking with",criteria
    # find all the matching results
    result = ''
    for e in g.element_list():
        if e.individual():
            if e.criteria_match(criteria):
                result += e.get_individual() + '\n'

    if result == '':
        return None
    return result
                    
def gedcom_family(id):
    families = ''
    for e in g.element_list():
        if e.individual():
            if e.pointer() == id:
                for f in e.families():
                    families += f.get_family() + '\n'
    return families

print "======================================================================"
print " Find people matching a given criteria "
print "======================================================================"
print gedcom_criteria(criteria)

print "======================================================================"
print " Find families a person belongs to "
print "======================================================================"
print gedcom_family("@I16@")
