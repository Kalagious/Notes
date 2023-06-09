<h1>---------General---------</h1>
<h3>Hostname: PC</h3>
<h3>IP: 10.10.11.214</h3>

<br>
<h1>---------Nmap---------</h1>
Ports 22 and 50051 Open


<br>
<h1>---------Web---------</h1>
<h3>URL:</h3>
<h3>Files:</h3>
<h3>Directories:</h3>


<br>
<h1>---------Vectors---------</h1>
! 50051 gRPC --> Found gRPC(Go Remote Procedural Call), Main Vector, do some research on how to interact with a gRPC server
<br>

Was able to list methods on gRPC and found SimpleApp:
```bash
┌──(kali㉿kali)-[~]
└─$ grpcurl -plaintext $IP:50051 list
SimpleApp*
```


List then revealed some methods in SimpleApp:
```bash
┌──(kali㉿kali)-[~]
└─$ grpcurl -plaintext $IP:50051 list SimpleApp
SimpleApp.LoginUser
SimpleApp.RegisterUser
SimpleApp.getInfo
```

Was able to register a test user with RegisterUser
```bash
┌──(kali㉿kali)-[~]
└─$ grpcurl -plaintext -connect-timeout 4 -d '{"username":"test","password":"password"}' $IP:50051 SimpleApp/RegisterUser
{
  "message": "Account created for user test!"
}

```
There is an admin user on the service
```bash
┌──(kali㉿kali)-[~/Notes/Boxes/HTB/PC]
└─$ grpcurl -plaintext -connect-timeout 4 -d '{"username":"admin","password":"password"}' $IP:50051 SimpleApp/RegisterUser
{
  "message": "User Already Exists!!"
}
```
Was able to login with admin admin
```bash
┌──(kali㉿kali)-[~/Notes/Boxes/HTB/PC]
└─$ grpcurl -plaintext -connect-timeout 4 -d '{"username":"admin","password":"admin"}' $IP:50051 SimpleApp/LoginUser
{
  "message": "Your id is 703."
}

```

Look into grpcui to proxy through burp suite
<br>
22 SSH


<br>
<h1>---------Credentials---------</h1>
<h3>Users:</h3>
<h3>Passwords:</h3>
<h3>Hashes:</h3>