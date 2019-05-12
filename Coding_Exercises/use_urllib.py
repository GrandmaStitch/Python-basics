import urllib.request
from urllib.parse import urlparse, parse_qs, quote, quote_plus, unquote

# urllib.request
connection = urllib.request.urlopen('https://stackoverflow.com/')

output = connection.read()

print(type(output))

output = str(output, 'iso-8859-1')
output = output.rstrip('\r\n')

print(output)

connection.close()


# urlparse
o = urlparse('https://docs.python.org/3/library/urllib.parse.html')

print('urlparse: {}'.format(o))
print('urlparse.scheme: {}'.format(o.scheme))
print('urlparse.port: {}'.format(o.port))
print('urlparse.geturl: {}'.format(o.geturl()))


# parse_qs
q = parse_qs('q=abc&r=hi')

print('parse_qs: {}'.format(q))


# urlparse, parse_qs
address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)

print(parts)

query = parse_qs(parts.query)

print(query)


# quote, quote_plus
# The URL quoting functions focus on taking program data 
# and making it safe for use as URL components by quoting special characters 
# and appropriately encoding non-ASCII text. 
# They also support reversing these operations to recreate the original data 
# from the contents of a URL component 
# if that task isn’t already covered by the URL parsing functions above.
quote1 = quote('a = Amy Money')

print('quote: {}'.format(quote1))

quote2 = quote_plus('a = Amy Money')

print('quote plus: {}'.format(quote2))


# unquote
unquote = unquote(quote1)

print('unquote: {}'.format(unquote))





