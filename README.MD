Author: Michael Hopkins
Email: mbh4480@rit.edu
Date: 1/16/2022

Requirements:
    Python version: 3.7.1 (This is the minimum for Pandas according to their documentation)
                          (My usage of list before zip requires a python 3 version to work correctly)
    Plotly version: 4.8 (This version adds easy support for multiple y values in a line graph)
    Dash version: 2.0 (earlier dash versions used deprecated packages)
    Pandas version: 1.3.5
Usage: Run main.py and navigate to http://127.0.0.1:8050/ to see the dashboard.
       Please change line 45 in main.py (app.run_server(host='127.0.0.1' , port=8050) if this port and host is not
                          available on your system.
File Structure of Dashboard Folder:
    main.py: Main program to run the dashboard which launches the dashboard and constructs the graph, table, 
                          and structure of the dashboard
    MovingAverageChart: Contains the StockChart class which reads the csv using pandas, calculates the moving average, 
                          and constructs the new graph using numpy and zip
    data.csv: csv file with data collected from yahoo finance that the dashboard and average is generated from.
    dataWithAnswers.csv: csv file with data collected from yahoo finance that the dashboard and average is generated from
                          ,but has an extra column to check answers against (NOTE: The answers are 
                          rounded to the 3rd decimal place and the chart does not do this)
