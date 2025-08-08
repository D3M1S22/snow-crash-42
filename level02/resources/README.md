# Level02 Writeup

## Objective
Gain access to the `flag02` user and retrieve the password for `level03`.

## Steps Taken

1. **Initial Discovery**  
   After logging into the `flag02` account, I ran:
   ```bash
   ls
   ```
   This revealed a `.pcap` file named `level02.pcap` in the home directory.

2. **Analyzing the PCAP File**  
   I began analyzing the packet capture file to understand what kind of network activity it recorded.  
   Using a combination of manual binary parsing and custom Python scripts, I examined Telnet-based traffic between the IPs `59.233.235.218` and `59.233.235.223`, where the server was listening on port `12121`.

3. **Telnet Interaction**  
   The PCAP contained a Telnet session negotiation, login prompt, and a failed login attempt. The server sent the prompt:
   ```
   wwwbugs login:
   ```
   The username entered by the client was reconstructed from multiple TCP segments and found to be:
   ```
   levelX
   ```

4. **Extracting the Password**  
   After the username, the server prompted:
   ```
   Password:
   ```
   I analyzed the client-to-server payloads after this point, filtering out Telnet negotiation bytes and handling backspace characters.

   The password was typed in several keystrokes, including some backspaces to correct mistakes. The corrected and final password entered was:
   ```
   ft_waNDReL0L
   ```

5. **Login as `flag02`**  
   Using the `su` command:
   ```bash
   su flag02
   ```
   I entered the password:
   ```
   ft_waNDReL0L
   ```
   Successfully logging in.

6. **Retrieve the Flag**  
   Once logged in, I executed:
   ```bash
   getflag
   ```
   This revealed the password for the next level:
   ```
   kooda2puivaav1idi4f57q8iq
   ```

## Result
Successfully retrieved the password for `level03`:  
```
kooda2puivaav1idi4f57q8iq
```
