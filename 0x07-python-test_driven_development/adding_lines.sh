#!/bin/bash
cat list | while read line; do echo "if _name_ == \"_main_\":" >> $line; done;
cat list | while read line; do echo -e "\timport doctest" >> $line; done;
cat list | while read line; do echo -e "\tdoctest.testfile(\"example.txt\")" >> $line; done;
