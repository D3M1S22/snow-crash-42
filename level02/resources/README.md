# Level02 Writeup

## Objective
Gain access to the `flag02` user and retrieve the password for `level03`.

## Steps Taken

1. **Login and File Discovery**  
   After logging in as `flag02`, I ran:
   ```bash
   ls
   ```
   This revealed a `.pcap` file present in the home directory.

2. **Understanding the `.pcap` File**  
   A `.pcap` (Packet Capture) file stores network traffic data. It is commonly analyzed using tools like `tcpdump` or `Wireshark`.

3. **Downloaded the File for Analysis**  
   I transferred the `.pcap` file to my local machine for better inspection using:
   ```bash
   scp flag02@machine:/home/flag02/capture.pcap .
   ```

4. **Analyzed the File with Wireshark**  
   I opened the `.pcap` file in Wireshark and inspected the packets.
   - I followed the TCP stream of an HTTP conversation.
   - Inside one of the payloads, I found what appeared to be a chat message or transmission containing the password.

5. **Extracted the Password**  
   The password for `level03` was found in cleartext within the TCP stream:
   ```
   qi0maab88jeaj46qoumi7maus
   ```

6. **Logged into `flag03`**  
   I switched to the next user using:
   ```bash
   su flag03
   ```
   And entered the extracted password.

## Result
Successfully retrieved the password for `level03`:  
```
qi0maab88jeaj46qoumi7maus
```
