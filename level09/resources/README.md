# Level09 Writeup

## Objective
Gain access to the `flag09` user and retrieve the password for `level10`.

## Steps Taken

1. **Initial Inspection**  
   In the `level09` home directory, I found the following:
   ```
   -rwsr-s--- 1 flag09 level09  xxxx Mar  5  2016 level09
   -rw------- 1 flag09 flag09     26 Mar  5  2016 token
   ```
   The token file contents were:
   ```
   f4kmm6p|=pnDBDu{
   ```
   But this token didn’t work as a password for the `flag09` user.

2. **Binary Behavior Analysis**  
   Executing the binary revealed it required exactly one argument:
   ```bash
   ./level09 token
   ```
   Result:
   ```
   tpmhr
   ```
   Trying simple inputs like `a`, `b`, or `abc` suggested a pattern:
   - Each character is transformed using its index position. For example:
     ```
     input:  abc
     output: ace  # 'a'+0, 'b'+1, 'c'+2
     ```
   So the binary appears to **encrypt input by shifting each character by its position index**.

3. **Reverse Engineering the Encryption**  
   Since the `token` is already encrypted, I wrote a Python script to reverse the transformation:
   ```python
   import sys
   token = sys.argv[1]
   decrypted = ''.join([chr(ord(c)-i) for i, c in enumerate(token)])
   print(decrypted)
   ```

4. **Running the Decryption**  
   I copied the script to the VM and ran:
   ```bash
   python /tmp/decrypt.py $(cat token)
   ```
   Output:
   ```
   f3iji1ju5yuevaus41q1afiuq
   ```

5. **Login and Flag Retrieval**  
   Used the decrypted string to switch to `flag09`:
   ```bash
   su flag09
   ```
   Then ran:
   ```bash
   getflag
   ```
   Which returned:
   ```
   Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
   ```

## Result
Successfully retrieved the password for `level10`:  
```
s5cAJpM8ev6XHw998pRWG728z
```
