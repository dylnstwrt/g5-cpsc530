# cpsc530-g5

Use the package manager pip3 before running:

```bash
pip3 install -r requirements.txt
```
In order to run the program, you must download the password dump, and place the resulting .txt file in src/resources. The password dump can be downloaded from below if you aren't on linux; otherwise ```rockyou.sh``` is included for convenience:

```bash
http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2
```

Following that, simply run main.py. Parameters for the number of passwords to be selected are defined by the get_passlist() function argument.
As it stands, for a run over a majority of the list (~14 million lines); it will take 2.5 - 3 hours on an i7-8086k; and generate a file that is approximately 1.65GB.
Here is a link to an compressed archive of our dataset (330MB) over the entire list:

```bash
https://mega.nz/file/vX4QWT5a#Si_4wKefknbXjpxei996V-5H_1y5Eb20RYWKOrlyl2c
```

Since order of passwords are randomized, future runs are likely to look different with respect to the dataset.
