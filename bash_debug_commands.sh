#!/bin/bash
mkdir -p /Users/dayanahfranklin/python/datasets/world_cities
mkdir -p /Users/dayanahfranklin/data_cleaning_project/data

Last login: Mon Mar 16 08:42:51 on ttys001
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % mkdir -p ~/python/datasets/world_cities
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % mv ~/Downloads/worldcities.csv ~/python/datasets/world_cities/worldcities.csv
mv ~/Downloads/movies.csv ~/python/datasets/movies.csv
mv ~/Downloads/Airbnb_Open_Data.csv ~/python/datasets/airbnb_open_data.csv
mv ~/Downloads/university_towns.txt ~/python/datasets/university_towns.txt
mv: /Users/dayanahfranklin/Downloads/worldcities.csv: No such file or directory
mv: rename /Users/dayanahfranklin/Downloads/movies.csv to /Users/dayanahfranklin/python/datasets/movies.csv: No such file or directory
mv: rename /Users/dayanahfranklin/Downloads/Airbnb_Open_Data.csv to /Users/dayanahfranklin/python/datasets/airbnb_open_data.csv: No such file or directory
mv: rename /Users/dayanahfranklin/Downloads/university_towns.txt to /Users/dayanahfranklin/python/datasets/university_towns.txt: No such file or directory
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % ls -la ~/python/datasets
ls -la ~/python/datasets/world_cities
total 0
drwxr-xr-x  3 dayanahfranklin  staff  96 Mar 16 05:44 .
drwxr-xr-x  3 dayanahfranklin  staff  96 Jan 11 21:27 ..
drwxr-xr-x  3 dayanahfranklin  staff  96 Jan 11 21:31 world_cities
total 9960
drwxr-xr-x  3 dayanahfranklin  staff       96 Jan 11 21:31 .
drwxr-xr-x  3 dayanahfranklin  staff       96 Mar 16 05:44 ..
-rw-r--r--  1 dayanahfranklin  staff  5097979 May 25  2025 worldcities.csv
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % find ~/Downloads -type f -iname "*.csv"
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % find ~ -type f -iname "*.csv"
/Users/dayanahfranklin/python/datasets/world_cities/worldcities.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-log2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arcsinh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arctanh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-sin.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-cos.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-cbrt.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arctan.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-cosh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-expm1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-sinh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-tanh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-log10.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arcsin.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arccos.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-log1p.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-log.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-exp2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-arccosh.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-tan.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/_core/tests/data/umath-validation-set-exp.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/philox-testset-1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/philox-testset-2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/sfc64-testset-1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/sfc64-testset-2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/mt19937-testset-2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/mt19937-testset-1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/pcg64-testset-1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/pcg64-testset-2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/pcg64dxsm-testset-1.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/numpy/random/tests/data/pcg64dxsm-testset-2.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/tornado/test/csv_translations/fr_FR.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/matplotlib/mpl-data/sample_data/msft.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/matplotlib/mpl-data/sample_data/data_x_x2_x3.csv
/Users/dayanahfranklin/Library/spyder-6/envs/spyder-runtime/lib/python3.12/site-packages/matplotlib/mpl-data/sample_data/Stocks.csv
/Users/dayanahfranklin/data_cleaning_project/data/Airbnb_Open_Data.csv
/Users/dayanahfranklin/data_cleaning_project/data/movies.csv
/Users/dayanahfranklin/data_cleaning_project/data/university_towns_cleaned.csv
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % mkdir -p ~/python/datasets/world_cities
cp /Users/dayanahfranklin/data_cleaning_project/data/Airbnb_Open_Data.csv ~/python/datasets/airbnb_open_data.csv
cp /Users/dayanahfranklin/data_cleaning_project/data/movies.csv ~/python/datasets/movies.csv
cp /Users/dayanahfranklin/data_cleaning_project/data/university_towns_cleaned.csv ~/python/datasets/university_towns.txt
cp /Users/dayanahfranklin/python/datasets/world_cities/worldcities.csv ~/python/datasets/world_cities/worldcities.csv
cp: /Users/dayanahfranklin/python/datasets/world_cities/worldcities.csv and /Users/dayanahfranklin/python/datasets/world_cities/worldcities.csv are identical (not copied).
(base) dayanahfranklin@Dayanahs-MacBook-Pro ~ % 

