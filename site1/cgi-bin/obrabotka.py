#!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage()

in_name = our_form.getfirst("in_name", "Имя не задано")
in_com = our_form.getfirst("in_com", "Коммент не задан")

print("Content-type: text/html")
print()
print(in_name)
print (in_com)
