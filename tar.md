## How to Create .tgz File

Command:

`tar -cvzf [file-name].tgz [file or directory to be archived]`

Options:

- `-c` create a new archive
- `-v` verbosely list files processed
- `-z` create tar file using gzip
- `-f` create archive named "file-name"

Example:

Run  `tar -cvzf test.tgz .` to create a new archive called test.tgz using gzip in the current directory.



## How to Unzip .tzg File

Command:

`tar -zxvf file-name.tgz`

Options:

- `-x` extract files from an archive
