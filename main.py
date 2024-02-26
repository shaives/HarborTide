# File: main.py
# -*- coding: utf-8 -*-
#
# Authors:  Brenner, John
#           Stone,Thomas
#           Urban, Conrad
#
# FinalProject Comp Methods II
# Project group: HarboTide



#Docstring examples

    #for functions
"""
    Returns the sum of two decimal numbers in binary digits.

            Parameters:
                        a (int): A decimal integer
                        b (int): Another decimal integer

            Returns:
                        binary_sum (str): Binary string of the sum of a and b
    """

    #for classes
"""
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

# import statements first

# import files

from functions_tide import *

def main():

    """
    Starts the programm.

            Parameters:
                        None

            Returns:
                        Hello World!
    """
    
    # dummy list of US states
    #state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

    #east_coast = ["Alabama", "Connecticut", "Delaware", "Florida", "Georgia", "Louisiana", "Massachusetts", "Maryland", "Maine", "Minnesota", "Mississippi", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New York", "Oklahoma", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "Texas", "Virginia", "Virgin Islands"]
    west_coast = ["Alaska", "California", "Guam", "Hawaii", "Oregon", "Washington"]

    bases_df = data_import_bases(west_coast)

    tide_sensors, tide_data = data_import_tidel_sensors()

    create_map(bases_df)


# main routine
if __name__ == '__main__':

    """
    Starts the programm.

    """
    
    main()