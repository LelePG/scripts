#!/bin/bash

pasta_principal="$PWD"

mogrify -format jpg $pasta_principal/*.png && rm *.png
