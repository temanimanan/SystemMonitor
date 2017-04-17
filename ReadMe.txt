MANAN TEMANI

System Monitoring
Step1: The python script generates randomly a Text File with "ALERT" / "OK" data in the /var/log/status.txt file
Step2: index.html plots a line graph using CanvasJS across Alert VS Time
Step3: index.html updates the graph continuously by reading the values from the Status File and plots the graph evry second

Status OK is represented by value 1 on Y-Axis
Status ALERT is represented by 2 on Y-Axis

The plot can be seen using the Python Simple Http Server