text = "Hello, world!"
# Encode the string to bytes using a specific encoding (e.g., UTF-8)
encoded_bytes = text.encode("utf-8")
print(encoded_bytes)

# Decode the bytes back to a string
decoded_text = encoded_bytes.decode("utf-8")
print(decoded_text)
