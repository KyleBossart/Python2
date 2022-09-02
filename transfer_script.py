    # Fitness for $10
# Member Transfer Script

# This is a Python 2 script for processing Transfers.
# When entering club and location info, please use the format [423x in City Name].
# Club Numbers and Cities: 4234 - Prescott, 4235 - Prescott Valley, 4236 - Downtown Prescott.
# -*- coding: utf-8 -*-

name = raw_input("What is the members first and last name?:")
agr_num = raw_input("What is the members agreement number?:")
from_club = raw_input("What club number is the member transferring from and what city is it located in?:")
to_club = raw_input("What club number is the member transferring to and what city is it located in?:")
if len(name) and len(agr_num) and len(from_club) and len(to_club) > 0:
    print """Please transfer member, %s(Primary) - %s, from club %s to club %s. We are also Datatrax clients.

Kyle Bossart. 

Fitness For $10, AZ

928-xxx-xxxx""" % (name, agr_num, from_club, to_club)

else:
    print "Please enter valid information."
