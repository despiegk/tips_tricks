
to install on osx
- https://gpgtools.org/
- as key server use: hkp://pgp.uni-mainz.de

```
#list my keys, check the nr
gpg -K
gpg --send-keys --keyserver pgp.mit.edu 57685726
gpg --send-keys --keyserver pgp.uni-mainz.de 57685726
gpg --send-keys --keyserver hkps.pool.sks-keyservers.net 57685726
```
