#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015
    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it


PROVINCIAL_TAX = 0.05
FEDERAL_TAX = 0.025

def bill_of_sale(purchase):

    def calculate_provincial_tax():
        return purchase * PROVINCIAL_TAX

    def calculate_federal_tax():
        return purchase * FEDERAL_TAX

    file_name = "bill_of_sale.txt"

    with open(file_name, 'w') as output_file:
        output_file.write("Amount of purchase: {0:.2f}\n".format(purchase))
        output_file.write("Provincial tax: {0:.2f}\n".format(calculate_provincial_tax()))
        output_file.write("Federal tax: {0:.2f}\n".format(calculate_federal_tax()))
        output_file.write("Total tax: {0:.2f}\n".format(purchase * .075))
        output_file.write("Total sale: {0:.2f}".format(purchase * 1.075))

bill_of_sale(100)