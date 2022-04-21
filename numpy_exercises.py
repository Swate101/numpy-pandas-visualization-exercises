{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "73817802",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fed69a83",
   "metadata": {},
   "outputs": [],
   "source": [
    "z = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a691b09c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# how many neg numbers are avaliable #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f39197db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([False, False, False, False,  True,  True, False, False, False,\n",
       "        True, False,  True])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z<0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "57975e1d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z<0].size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8fb0ee69",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4,)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z<0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "29da15fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-2, -1, -6, -7])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z<0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8803434",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now we will count the positive numbers avaliable #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1f2686db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ True,  True,  True,  True, False, False, False, False, False,\n",
       "       False,  True, False])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z>0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ace1f0d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z>0].size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2db17255",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5,)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z>0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "44df4a2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4, 10, 12, 23,  3])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[z>0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10b044c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find how many positive even numbers there are # "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "72cd10e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 4, 10, 12])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[(z % 2 == 0) & (z > 0)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2c245c65",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3,)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[(z % 2 == 0) & (z > 0)].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9ee23a4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z[(z % 2 == 0) & (z > 0)].size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "847aac7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now we will add three to each data point of Z , How many positve values of Z are there ? # "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "72880b00",
   "metadata": {},
   "outputs": [],
   "source": [
    "plus_three = z + 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d7319de4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 7, 13, 15, 26,  1,  2,  3,  3,  3, -3,  6, -4])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plus_three"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1f424557",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 7, 13, 15, 26,  1,  2,  3,  3,  3,  6])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " plus_three[plus_three > 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ee4234ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# this string bring up the positive entrys of z  and toss out all the negs #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "a466625a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10,)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " plus_three[plus_three > 0].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "320c43e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " plus_three[plus_three > 0].size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8b340c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# -------------------------------------------------------------------------------------- #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "211e88cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# what is the diffrence between .SIZE // .SHAPE // .LEN ??? # // NOT PART OF THE LESSON //  #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "5a54a6c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = np.array([[1, 2, 3], [4, 5, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e6f37ed1",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = np.array([[1, 2, 3], [4, 5, 6]]).shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2a18fff7",
   "metadata": {},
   "outputs": [],
   "source": [
    "p = np.array([[1, 2, 3], [4, 5, 6]]).size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3dcdd11a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "8ed37797",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45d3af35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# .SHAPE still gives the same value it just seems to be three diminsional #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "1d4f2d0b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(p) # length gives you the outer most layer of an array #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdc3db9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ------------------------------------------------------------------------------------------ #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1698e8ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "# with a ** # what would you get for the mean and std # "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d7b29c2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "z = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "6ed71995",
   "metadata": {},
   "outputs": [],
   "source": [
    "squared = z ** 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3d4ea279",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squared"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c3adca97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "74.0"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squared.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3b67664f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "144.0243035046516"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squared.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "db2ffdc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "center = z - z.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "6753683f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,\n",
       "       -10.])"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "center"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "c6a3551f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "center.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "0d41c860",
   "metadata": {},
   "outputs": [],
   "source": [
    "Zs = (z - z.mean()) / z.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "1d077a98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0.,\n",
       "       -10.])"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "z - z.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "fc42e94f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,\n",
       "       -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,\n",
       "        0.        , -1.24034735])"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Zs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c9be906",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ----------------------------------------------------------------------------------- #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "32849769",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "# Use python's built in functionality/operators to determine the following:\n",
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "\n",
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "\n",
    "# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list\n",
    "\n",
    "# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list\n",
    "\n",
    "# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together\n",
    "\n",
    "# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n",
    "\n",
    "# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers\n",
    "\n",
    "# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "26165b46",
   "metadata": {},
   "outputs": [],
   "source": [
    "SUM_of_A = sum(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "47995f93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "SUM_of_A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fa4e4933",
   "metadata": {},
   "outputs": [],
   "source": [
    "MIN_OF_A = min(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "b188f027",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "0162a74f",
   "metadata": {},
   "outputs": [],
   "source": [
    "Max_OF_A = max(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "3247b5b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Max_OF_A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "898357c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_of_a = sum(a) / len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "b8972b66",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "e7e699eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "c5a00a3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "55/10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "ebba784d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "9b08c7e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(a) / len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "9785a7c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "product_of_a = 1\n",
    "for p in a:\n",
    "    product_of_a = product_of_a * p\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "973180ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3628800"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "f106b412",
   "metadata": {},
   "outputs": [],
   "source": [
    "squares_of_A = [p ** 2 for p in a]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "c290fb5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares_of_A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "e69fd416",
   "metadata": {},
   "outputs": [],
   "source": [
    "odds_in_A = [p for p in a if p % 2 != 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "e41afc2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "49d05832",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 5, 7, 9]"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odds_in_A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "a880f98e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c65eaa8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# we do the same thing just reversed != // == #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "5f6c305e",
   "metadata": {},
   "outputs": [],
   "source": [
    "evens_in_A = [p for p in a if p % 2 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "f28e57b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 6, 8, 10]"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evens_in_A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf368af4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# SET UP 2 -------------------------------------------------------------- #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "273e28a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = [\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "1301bb29",
   "metadata": {},
   "outputs": [],
   "source": [
    "b = np.array(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "31245d52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5],\n",
       "       [6, 7, 8]])"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "630cf8c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "8ce76ee0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "e5a19d27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "199103ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function ndarray.mean>"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "13675384",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "caee0ca0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20160"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "d4e45e3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 9, 16, 25],\n",
       "       [36, 49, 64]])"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "c30e1785",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 5, 7])"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b[b % 2 == 1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "4a3a0ef0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 6, 8])"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b[b % 2 == 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "96918e83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "36988995",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5],\n",
       "       [6, 7, 8]])"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "f7006b99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 6],\n",
       "       [4, 7],\n",
       "       [5, 8]])"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "71f9d918",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function ndarray.flatten>"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.flatten"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "d4c1dd7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([3, 4, 5, 6, 7, 8])"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.flatten()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "0a973e03",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5, 6, 7, 8]])"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.reshape(1, 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "71691e2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup 3 --------------------------------------------------------------------------- #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "11c7bf02",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "c = np.array(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "7c0b479f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "1feb8993",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3, 4, 5, 6, 7, 8, 9])"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.flatten()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "46a2e617",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function ndarray.sum>"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "bb55fa04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "73a7cddc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "fde28b64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "8d0995c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "362880"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "d4d6e3e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  4,  9],\n",
       "       [16, 25, 36],\n",
       "       [49, 64, 81]])"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c ** 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "94ba8f10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function ndarray.std>"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.std"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "2f6ba5d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.581988897471611"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "4e6a01bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.666666666666667"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.var()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "c8d21328",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "f4c10fa7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "13ffbeb4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.transpose(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "9faaef82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 30,  36,  42],\n",
       "       [ 66,  81,  96],\n",
       "       [102, 126, 150]])"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.dot(c, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "83c28a51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "261"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(c * c.T).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "8c7d58e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  8, 21],\n",
       "       [ 8, 25, 48],\n",
       "       [21, 48, 81]])"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c * c.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "d8a5b827",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([12, 15, 18])"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "1dfa599f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "261"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(c * c.T).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "1b686d97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "131681894400"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(c * c.T).prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "10f200e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "131681894400"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(c * c).prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8dd7c4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# why would we transpose it ??? # "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0adfe791",
   "metadata": {},
   "outputs": [],
   "source": [
    "# exercise 4 -------------------------------------------------------------- #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "f2cb319c",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = [\n",
    "    [90, 30, 45, 0, 120, 180],\n",
    "    [45, -90, -30, 270, 90, 0],\n",
    "    [60, 45, -45, 90, -45, 180]\n",
    "]\n",
    "\n",
    "d = np.array(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "b8a316e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30,  45,   0, 120, 180],\n",
       "       [ 45, -90, -30, 270,  90,   0],\n",
       "       [ 60,  45, -45,  90, -45, 180]])"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "b826104d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  45,  60],\n",
       "       [ 30, -90,  45],\n",
       "       [ 45, -30, -45],\n",
       "       [  0, 270,  90],\n",
       "       [120,  90, -45],\n",
       "       [180,   0, 180]])"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "df5e01ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45,   0, 120, 180,  45, -90, -30, 270,  90,   0,  60,\n",
       "        45, -45,  90, -45, 180])"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.flatten()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "08354d11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,\n",
       "        -0.80115264],\n",
       "       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,\n",
       "         0.        ],\n",
       "       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,\n",
       "        -0.80115264]])"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.sin(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "96934153",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,\n",
       "        -0.59846007],\n",
       "       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,\n",
       "         1.        ],\n",
       "       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,\n",
       "        -0.59846007]])"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cos(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "2e57dc52",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,\n",
       "         1.33869021],\n",
       "       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,\n",
       "         0.        ],\n",
       "       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,\n",
       "         1.33869021]])"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.tan(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "9fce2b68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  0, -90, -30,   0, -45, -45])"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[d <= 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "51aa6a5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -30, -45, -45])"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[d < 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "9ad62881",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45,   0, 120, 180,  45, 270,  90,   0,  60,  45,  90,\n",
       "       180])"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[d >= 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "406c12cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])"
      ]
     },
     "execution_count": 150,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d[d > 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "591b4160",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "8334cd31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "bd49af43",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "c4ac9992",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 6)"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "f7eaa75c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "bf6dd46d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  45,  60],\n",
       "       [ 30, -90,  45],\n",
       "       [ 45, -30, -45],\n",
       "       [  0, 270,  90],\n",
       "       [120,  90, -45],\n",
       "       [180,   0, 180]])"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e43a0bcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# the top couple i was just seeing how the minpulated data looked #"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "a7b2f6b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.unique(d).size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "959d29cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6, 3)"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.T.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "1e239e64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30],\n",
       "       [ 45,   0],\n",
       "       [120, 180],\n",
       "       [ 45, -90],\n",
       "       [-30, 270],\n",
       "       [ 90,   0],\n",
       "       [ 60,  45],\n",
       "       [-45,  90],\n",
       "       [-45, 180]])"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.reshape(9, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "14a6a737",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90],\n",
       "       [ 30],\n",
       "       [ 45],\n",
       "       [  0],\n",
       "       [120],\n",
       "       [180],\n",
       "       [ 45],\n",
       "       [-90],\n",
       "       [-30],\n",
       "       [270],\n",
       "       [ 90],\n",
       "       [  0],\n",
       "       [ 60],\n",
       "       [ 45],\n",
       "       [-45],\n",
       "       [ 90],\n",
       "       [-45],\n",
       "       [180]])"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d.reshape(18, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "615770b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
