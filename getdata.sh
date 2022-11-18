#!/bin/bash

imagenames=$(paste -sd ';' metadata/filesubset.txt)  # assign output of command to variable, could also use backtics

echo "files to be downloaded:"
echo $imagenames

#download
./azcopy cp \
    "https://lilablobssc.blob.core.windows.net/wellington-unzipped/images/" \
    test_data/ \
    --include-path "$imagenames"
