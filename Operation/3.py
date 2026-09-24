import re

# Using a dot (.) to match any character
pattern_dot = r"a.b"
text_dot = "aab, abb, acb, adb, zyacb"

matches_dot = re.findall(pattern_dot, text_dot)
print("Matches with dot:", matches_dot)

# Using backslash (\) to escape special characters
pattern_escape = r"a\*b"
text_escape = "a*b, aab, abb"

matches_escape = re.findall(pattern_escape, text_escape)
print("Matches with escape:", matches_escape)
