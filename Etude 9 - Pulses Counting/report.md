COSC 326 Etude 9: Pulses Counting
Trent Lim & Harry Pittar

In this etude, we have a main function that opens a file using the Python command line argument. Each line in the input is added to an array called data. The array is then passed onto *get_peaks*, which returns the positions and height of each peak. Finally, *plot_data* plots all the values in the data, along with the position of each peak, shown with a red dot.

## get_peaks
This function uses the scipy function *find_peaks*, which finds every local maxima by simply comparing with neighboring values. *find_peaks* uses multiple parameters in finding local maximas, and the correct parameters were determined using trial and error. After some testing, we found parameters that worked for all datasets. 

In this process, peaks that were either the first or last value of the dataset would not be recognized as a peak by *find_peaks*. So we made the function create a temporary array identical to the original one, and add the mean value of the dataset to the start and the end of the array. This allowed *find_peaks* to recognize these values as peaks by comparing with their neighbors.

From the find_peaks function, we create arrays which store the heights and position of each peak, and store it in the variables *heights* and *peak_positions*

## plot_data
This function plots the data as a line graph along with the peaks, or pulses. It creates an array called indexes which stores the index for each datapoint to use when plotting the line graph. It then plots the data with indexes on the x axis, and the value for each datapoint on the y axis. The function also indicates the position of each peak to the graph as a red dot.