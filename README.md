# dogbiteapp

The purpose of this deployment was to deploy your own app on the ELB using all the information and classwork projects. My app utilized a python script with requests library to pull json data from NYC OPEN Data project, then run the data through functions to create a sorted data of dog bites based on location and gender. This data would then be deployed onto server/app using Flask and ELB for hosting.
Currently, the data functions are working properly, however, there is issue with attempting to print out the data on to the flask subdirectory pages.

I've made past attempted to utilized sqlite3 and import the data, but that was met with a lot of difficulties, so I am pulling data live from the database in realtime and processing during deployment. I also ran into a lot of issues in VScode with Pylance not being able to import the modules, so I had to spend 3 days troubleshooting this issue, including reinstalling interpreters, changing Environment paths, and settting up virutal environments and switching IDEs until I nuked my entire development environment.
