
string_char="hello00099pythono98989"
filter_char = filter (lambda x: not x.isdigit(),string_char)
filter_string="".join(filter_char)
print(filter_string)