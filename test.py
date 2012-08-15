#!/usr/bin/env python

# This file is part of the Python GEDCOM Parser

# Copyright (C) 2012 Daniel Zappala (daniel.zappala [at] gmail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Global imports
import optparse

# Local imports
import gedcom

class Test:
    """Test driver for the Gedcom parser."""

    def __init__(self):
        """ Initialize test class."""
        self.parse_options()
        self.filename = self.options.filename
        self.g = gedcom.Gedcom(self.filename)
        self.info = 'names'

    def parse_options(self):
        """ Parse command-line options."""
        parser = optparse.OptionParser(usage = "%prog [options]",
                                       version = "%prog 0.1")

        parser.add_option("-f","--file",type="string",dest="filename",
                          default='test.ged',
                          help="gedcom file name")

        (self.options,self.args) = parser.parse_args()

    def run(self,info='names',surname='A',given='Maria',
            birth=1857,birth_start=1850,birth_end=1860,
            death=1857,death_start=1850,death_end=1860,
            marriage=1857,marriage_start=1850,marriage_end=1860,
            family_surname='Nicotra',family_given='Maria',
            criteria='surname=N:birthrange=1820-1840:deathrange=1900-1910'):
        """Run a standard series of tests.
        
        Keyword arguments:
        info -- The type of information to print. Use 'name' will print
                the matching names and 'gedcom' to print all of the gedcom 
                information for the matching records.
  
        ** The following keyword arguments are used to show matching records
        in the gedcom file. ***

        surname -- A surname substring (default Zap)
        given -- A given name substring (default Maria)
        birth -- A birth year (default 1857)
        death -- A death year (default 1857)
        marriage -- A marriage year (default 1857)
        birth_start -- The start of a birth year range (default 1850)
        birth_end -- The end of a birth year range (default 1860)
        death_start -- The start of a death year range (default 1850)
        death_end -- The end of a end year range (default 1860)
        marriage_start -- The start of a marriage year range (default 1850)
        marriage_end -- The end of a marriage year range (default 1860)
        family_surname -- A surname substring (default Nicotra)
        family_given -- A given name substring (default Maria)
        criteria -- A complete criteria for matching, see below for format.

        """
        self.info = info
        self.surname(surname)
        self.given(given)
        self.birth(birth)
        self.birth_range(birth_start,birth_end)
        self.death(death)
        self.death_range(death_start,death_end)
        self.marriage(marriage)
        self.marriage_range(marriage_start,marriage_end)
        self.family_of(family_surname,family_given)
        self.criteria_match(criteria)
        self.missing()

    def print_header(self,header):
        """Print a header."""
        print
        print "="*70        
        print header
        print "="*70

    def print_record(self,e):
        """Print an element."""
        if self.info == 'names':
            (first,last) = e.name()
            print first, last
        elif self.info == 'gedcom':
            print e.get_individual()
        

    def surname(self,match):
        """Show matching records for a surname substring."""
        self.print_header('Surname - %s' % (match))
        for e in self.g.element_list():
            if e.individual():
                if e.surname_match(match):
                    self.print_record(e)

    def given(self,match):
        """Show matching records for a given name substring."""
        self.print_header('Given - %s' % (match))
        for e in self.g.element_list():
            if e.individual():
                if e.given_match(match):
                    self.print_record(e)

    def birth(self,year):
        """Show matching records for a birth year."""
        self.print_header('Born %d' % (year))
        for e in self.g.element_list():
            if e.individual():
                if e.birth_year_match(year):
                    self.print_record(e)

    def birth_range(self,year1,year2):
        """Show matching records for a birth year range."""
        self.print_header('Born %d - %d' % (year1,year2))
        for e in self.g.element_list():
            if e.individual():
                if e.birth_range_match(year1,year2):
                    self.print_record(e)

    def death(self,year):
        """Show matching records for a death year."""
        self.print_header('Died %d' %(year))
        for e in self.g.element_list():
            if e.individual():
                if e.death_year_match(year):
                    self.print_record(e)

    def death_range(self,year1,year2):
        """Show matching records for a death year range."""
        self.print_header('Died %d - %d' % (year1,year2))
        for e in self.g.element_list():
            if e.individual():
                if e.death_range_match(year1,year2):
                    self.print_record(e)

    def marriage(self,year):
        """Show matching records for a marriage year."""
        self.print_header('Married %d' % (year))
        for e in self.g.element_list():
            if e.individual():
                if e.marriage_year_match(year):
                    self.print_record(e)

    def marriage_range(self,year1,year2):
        """Show matching records for a marriage year range."""
        self.print_header('Married %d - %d' % (year1,year2))
        for e in self.g.element_list():
            if e.individual():
                if e.marriage_range_match(year1,year2):
                    self.print_record(e)

    def family_of(self,surname,given):
        """Show matching records sharing a family with a person who matches
        the surname and given name substrings.

        """
        self.print_header('Family of %s %s' % (given,surname))
        for e in self.g.element_list():
            if e.individual():
                if e.surname_match(surname) and e.given_match(given):
                    for f in e.families():
                        for e in f.get_family():
                            self.print_record(e)

    def criteria_match(self,criteria):
        """Show matching records using a general criteria. The format
        is [field1]=[value2]:[field2]=[value2]...

        Valid fields are:

        surname, name, birth, birthrange, death, deathrange, marriage,
        marriagerange

        """
        self.print_header('Criteria Matching: %s' % (criteria))
        for e in self.g.element_list():
            if e.individual():
                if e.criteria_match(criteria):
                    self.print_record(e)

    def missing(self):
        """Show GEDCOM pointers for that are used in the file but are
        missing.

        """
        self.print_header('Missing Records')
        for e in self.g.element_list():
            if e.value().startswith('@'):
                f = self.g.element_dict().get(e.value(),None)
                if f == None:
                    print e.value()

if __name__ == "__main__":
    t = Test()
    t.run()
