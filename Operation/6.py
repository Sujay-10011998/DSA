import textwrap

# Sample text
sample_text = "This is a sample text that we want to wrap to fit within a specified width."

# Wrap the text to fit within a specified width (e.g., 20 characters)
wrapped_text = textwrap.wrap(sample_text, width=20)

# Print the wrapped text
for line in wrapped_text:
    print(line)
