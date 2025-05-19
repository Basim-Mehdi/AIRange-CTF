# XOR-decode a binary file and save the real executable

input_file = "rev_it"
output_file = "rev_it_decoded"

with open(input_file, "rb") as f:
    data = f.read()

for key in range(256):
    decoded = bytes([b ^ key for b in data])
    if b"flag{" in decoded or b"ctf{" in decoded:
        print(f"[+] Key found: {key}")
        print("[+] Writing decoded file to:", output_file)
        
        # Save the decoded binary to disk
        with open(output_file, "wb") as out:
            out.write(decoded)
        break
