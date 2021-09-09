# dogbiteapp

The purpose of this deployment was to deploy your own app on the ELB using all the information and classwork projects. My app utilized a python script with requests library to pull json data from NYC OPEN Data project, then run the data through functions to create a sorted data of dog bites based on location and gender. This data would then be deployed onto server/app using Flask and ELB for hosting.
Currently, the data functions are working properly, however, there is issue with attempting to print out the data on to the flask subdirectory pages.

<h2>Coding and local testing</h2>
I've made past attempted to utilized sqlite3 and import the data, but that was met with a lot of difficulties, so I am pulling data live from the database in realtime and processing during deployment. I also ran into a lot of issues in VScode with Pylance not being able to import the modules, so I had to spend 3 days troubleshooting this issue, including reinstalling interpreters, changing Environment paths, and settting up virutal environments and switching IDEs until I nuked my entire development environment.

<h2>Deployment</h2>
During deployment, EBS was degrading at every point. I found that the pip freeze was pushing into the requirements older packages, some of which were not compatible with Python 3. I had to manually adjust for that since even setting up a venv did not fix the issue. It turns out one of the issues was the json api requests. The list comphresion used to output data in real time caused the requests to 400 and 500 out during the build phase in EBS. I set the number to 100 as a test and it worked out within a matter of minutes.


TLDR:
Problems:
Could not get data to print to screen - Added return statements in the functions and it fixed that.
Unable to pull requirements that met Python3 language due to pip used being python2- Manually adjusted requirements and may have been able to also create venv that was python3 based as venv made was python2 based.
Could not deploy on EBS without issues. - Had to lower api pull requests during list during build phase. This requires a more permanent solution, which may be solved using a sql database and some list check functions.

Things to add in future:
HTML page with more UI.
