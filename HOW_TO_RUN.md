# How to run these scripts

You can run the scripts in this lab under either CPython 2.7, available
[here][CPython download], or Jython 2.7, avaliable [here][Jython download].

The scripts should run identically on both interpreters, but one or the other
might be easier to install on your system. CPython 2.7 is deprecated but
mature; Jython 2.7 is maintained but finicky&mdash;pick your poison.

[CPython download]: https://www.python.org/downloads/release/python-2718/
[Jython download]: https://www.jython.org/download

Several of these scripts take command-line arguments, so you probably want to
run them on the terminal rather than through an IDE. You can invoke the scripts
as follows:

## `vigenere.py`

`vigenere.py` encrypts and decrypts text with the Vigen&egrave;re cypher. It's
useful for sending and receiving encrypted texts, but it's less useful for
breaking encryptions. You can run it like this:

```sh
jython vigenere.py
```

You'll be prompted for whether you want to encrypt or decrypt; what key to use;
and what text to encrypt/decrypt.

## `plaintext_checker.py`

`plaintext_checker.py` tries to decrypt several files at once with a given key.
However, it can also be used to check if several files start with a given
fragment of plaintext. It's useful if you have a lot of ciphertext files, and
you want to check if any of them start with a certain common phrase (say, the
start of Alice in Wonderland, or the lyrics to "Never Gonna Give You Up"). You
can run the it like this:

```sh
jython plaintext_checker.py -p plaintext ciphertext_file [ciphertext_file...]
```

For example,

```sh
jython plaintext_checker.py \
  -p 'Alice was beginning to get very tired of' \
  ciphertexts/*.txt
```

## `word_checker.py`

`word_checker.py` takes a given plaintext fragment and checks it against every
substring of a ciphertext. It's useful if you suspect that a word occurs in
the ciphertext, but you don't know where. (We mostly used it for breaking the
running-key cipher.) You can run it like this:

```sh
jython word_checker.py -k fragment ciphertext_file
```

For example,

```sh
jython word_checker.py -k 'cryptology' ciphertexts/running-key-ciphertext.txt
```

***

In our log, we also included several snippets from the Jython REPL or the
shell. We included these to help illustrate how we solved the problem, but you
may or may not be able to replicate them on your system. Sorry about that!
¯\\\_(ツ)\_/¯

A few times in the lab, we used the default Unix word list found at
`/usr/share/dict/words`. You can find the full list online [here][words].

[words]: https://gist.github.com/sdao/12ccaf20722a61d401e2ff284b5a28a2