# The re module in Python provides support for regular expressions


#Literal characters
import re

pattern = r"sujay"
text = "sujay mondal"

match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")



#Metacharacters
# Special characters with a special meaning, like . (any character),
# ^ (start of string), $ (end of string), * (zero or more occurrences), + (one or more occurrences), ? (zero or one occurrence), etc.

import re

pattern = r"^start.*end$"
text = "start middle end"

match = re.search(pattern, text)

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")



#Quantifiers
#  *, +, and ?: Match zero or more, one or more, and zero or one occurrences, respectively.

import re

pattern = r"\d+"  # Match one or more digits
text = "There are many apples and 456 oranges."

matches = re.findall(pattern, text)
print(matches)


#Character Classes
#[ ]: Match any one of the characters within the brackets.

import re

pattern = r"[aeiou]"
text = "sujay mondal"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)


