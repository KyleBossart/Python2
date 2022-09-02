# Fitness for $10
# Cancellation Script
# This is a Python 2 script for processing Cancellations.
# Please use date format xx/xx/xx.
# -*- coding: utf-8 -*-

received = raw_input("When did the member fill out the cancel request?:")
last_due = raw_input("When is the members last payment due?:")
final_access = raw_input("When is the last day the member has access to the club?:")
if len(received) and len(last_due) and len(final_access) > 0:
    print "PER KYLE, CANCEL REQUEST RECEIVED AT CLUB ON %s MEMBER IS AWARE OF FINAL DRAFT ON %s CANCEL MEMBERSHIP EFFECTIVE %s NO EARLY CANCEL FEE. KB" % (
    received, last_due, final_access)
else:
    print "Please enter valid dates."
    
