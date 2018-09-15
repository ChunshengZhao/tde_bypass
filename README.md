# tde_bypass
Bypass Transparent Data Encryption.

Use "pyinstaller" to make the whitelist program "ftp_server.exe" and the blacklist program "notepad.exe".

Note: The program in the blacklist performs the decryption operation when reading the file, and performs the encryption operation when writing the file; the program reading and writing in the whitelist is not limited.

Check if the blacklist program can be decrypted normally:
![Screenshots](https://raw.githubusercontent.com/ChunshengZhao/tde_bypass/master/check.png)

Transfer the decrypted file and change the file extension.
![Screenshots](https://raw.githubusercontent.com/ChunshengZhao/tde_bypass/master/bypass_1.png)
![Screenshots](https://raw.githubusercontent.com/ChunshengZhao/tde_bypass/master/bypass_2.png)

Good Luck!
