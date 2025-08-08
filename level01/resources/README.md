# Level01 Writeup

## Objective
Gain access to the `flag01` user and retrieve the password for `level02`.

## Steps Taken

1. **Noticed Suspicious Entry in `/etc/passwd`**  
   While checking for the first flag, I noticed that the `/etc/passwd` file had a unique entry for the `flag01` user:
   ```
   flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
   ```
   The presence of the hashed password in the second field indicated that it might be crackable.

2. **Attempted Direct Login**  
   I initially tried to use the string `42hDRfypTqqnw` as the password via `su flag01`, but it didn’t work.

3. **Used John the Ripper for Cracking**  
   I downloaded **John the Ripper** using `wget` into the `/tmp` folder:
   ```bash
   wget --no-check-certificate https://www.openwall.com/john/k/john-1.9.0.tar.xz
   ```

4. **Built the Tool**  
   After extracting the archive, I compiled it using:
   ```bash
   make clean generic
   ```

5. **Prepared Input for Cracking**  
   I created a file containing only the hash:
   ```
   42hDRfypTqqnw
   ```

6. **Ran John the Ripper**  
   I executed John on the file, and it successfully cracked the hash, giving the password:
   ```
   abcdefg
   ```

7. **Login to `flag01`**  
   I switched to the `flag01` user using:
   ```bash
   su flag01
   ```
   And entered the password:
   ```
   abcdefg
   ```

8. **Retrieved the Flag**  
   Once logged in, I ran the `getflag` command:
   ```bash
   getflag
   ```
   This returned the flag (password for the next level):
   ```
   f2av5il02puano7naaf6adaaf
   ```

## Result
Successfully retrieved the password for `level02`.
