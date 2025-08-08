# Level00 Writeup

## Objective
Gain access to the `flag00` user and retrieve the password for `level01`.

## Steps Taken

1. **Locate Files Owned by `flag00`**  
   I used the following `find` command to search for any files owned by the `flag00` user:
   ```bash
   find / -user flag00 2>/dev/null
   ```

2. **Discovery**  
   This command revealed a file named `john` located in:
   ```
   /usr/sbin/john
   ```

3. **Inspect the File**  
   I viewed the contents of the file using:
   ```bash
   cat /usr/sbin/john
   ```
   The output was:
   ```
   cdiiddwpgswtgt
   ```

4. **Cipher Identification**  
   I first attempted using the string directly as a password/flag, but it didn't work.  
   Then, I used the [dCode Cipher Identifier](https://www.dcode.fr/cipher-identifier) to analyze the string.

5. **Decryption**  
   dCode suggested several possible ciphers.  
   I tried a few and eventually found that the string was encrypted using **Caesar cipher with a shift of 15**.  
   Decrypting `cdiiddwpgswtgt` with Caesar-15 gave me:
   ```
   nottoohardhere
   ```

6. **Switch User to `flag00`**  
   I used the `su` command:
   ```bash
   su flag00
   ```
   When prompted, I entered the decrypted password:
   ```
   nottoohardhere
   ```

7. **Success**  
   After logging in as `flag00`, I was shown the password for `level01`:
   ```
   x24ti5gi3x0ol2eh4esiuxias
   ```

## Result
Successfully retrieved the password for `level01`.
