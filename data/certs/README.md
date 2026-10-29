# Extra CA certificates

`incommon-rsa-server-ca2.pem` is the InCommon RSA Server CA 2 intermediate,
downloaded from the URL in ORACC's certificate (Authority Information Access:
http://crt.sectigo.com/InCommonRSAServerCA2.crt). It is signed by USERTrust RSA.

oracc.museum.upenn.edu does not send this intermediate, so TLS verification
fails without it. Fetch scripts append it to the system CA bundle. They never
disable verification.
