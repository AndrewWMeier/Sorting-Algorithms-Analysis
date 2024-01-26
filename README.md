# Sorting-Algorithms-Analysis
A simple Tkinter interface to help with the empirical analysis of the merge sort algorithm. Here are some example plots made with the interface:


![image](https://github.com/AndrewWMeier/Sorting-Algorithms-Analysis/assets/123119277/fcfac86e-4076-4931-97a4-f5ff28c2dbf7)

![image](https://github.com/AndrewWMeier/Sorting-Algorithms-Analysis/assets/123119277/06f77594-ca91-4f14-ad17-bdaf34b64e2f)

![image](https://github.com/AndrewWMeier/Sorting-Algorithms-Analysis/assets/123119277/b72de785-7ad2-4d8f-b7d8-a63c0c65ac66)


# How to use
### 1. Install Dependencies
```bash
pip install numpy
pip install matplotlib
```

### 2. Run the program
run the file interface.py this loads up the user interface to decide what to plot. This will bring up a screen like the following: 
![interfaceimg](https://github.com/AndrewWMeier/Sorting-Algorithms-Analysis/assets/123119277/14d410ba-1dbb-4a4c-a058-38225be11b34)



### 3. Using the program

- **Array Sizes:** This represents the size of the arrays at each data point to be sorted. Recommended values include 100, 200, 300, 400, 500. Larger arrays take longer to sort, but yield more accurate results.

- **Number Of Arrays:** This is the number of arrays at each data point to be sorted. Choosing 30 means sorting 30 arrays of size 100, 30 arrays of size 200, and so on.

- **Integer Range:** The numbers in the arrays to be sorted range from 0 to n. This is the choice of your n value.

- **Plot Type:** Different plot options are available:
  - *Average:* The average time to sort the arrays vs. the array size.
  - *Median:* The median time to sort the arrays vs. the array size.
  - *Comparisons:* The average number of comparisons made during sorting vs. the array size.
  - *Max/Min:* The maximum and minimum time to sort at each array size.

# References:
Khanna, M. (2023, November 28). Merge sort - data structure and algorithms tutorials. GeeksforGeeks. 
  https://www.geeksforgeeks.org/merge-sort/ 

Alam, M., & Chugh, A. (2014, March 2). Sorting algorithm: An empirical analysis - ijesit.com. Sorting Algorithm: An Empirical Analysis. 
  https://www.ijesit.com/Volume%203/Issue%202/IJESIT201402_16.pdf 

GeeksforGeeks. (2023, April 26). Timeit in python with examples. GeeksforGeeks.
   https://www.geeksforgeeks.org/timeit-python-examples/ 

Visualization with python. Matplotlib. (n.d.).
    https://matplotlib.org/ 

Chat with us on OpenAI. (n.d.). OpenAI.
https://chat.openai.com/share/ed40b149-01f8-42b1-adac-db726e19463f
