"""
jwt web token is for transmitting the information of a http request in a secure way as JSON format.
the information is represented as name(string) - value(arbitary value) pair.
the information is digitally signed with a message authentication code which can also be encrypted.

types in jwt-
JWS- the content is given a digital signature to make sure the info is not tampered during transmission, contents are readable,
    must not be used to transfer sensitive data, gives integrity to contents.
JWT- the content is encrypted , gives integrity and also hides the content.

JWT structure-
3 parts seperated by(.) - header,payload,signature

header - type of token, signing algorithm 
payload - contain the information passed, the info is called as claims
signature - encoded header + "." + encoded payload + secret 

how jwt works-
- client sends credentials to login, if authntication is successfull the server sends a jwt token back
- clients sends the jwt token in next request to access any resources from server
- server looks for the valid jwt in header if it is present then server gives access to the resources
- the jwt recieved by server contains the info of user and their previleges so it grants them accordingly
- the jwt contains a secret in signature which is known to server, if anyone tampers with request by editing the token when request is sent
    as server gets the token it calculates and as the one tampering doesnt have secret, the request verification by server fails.


library used - 
for different languages there are different libraries.

djangorestframework-simplejwt   is used.
