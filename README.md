# WEALTHAPP

# Task

1) Maintain account of 4-5 users. They do a fixed deposit every time they want. ( just for use case simulation)
2) For users depositing more than 100 rupees , the interest rate is 0.5 % every hour.
3) For users depositing more than 50 rupees, the interest rate is 0.4% every hour.
4) Anything less than 40 is 0.3% per hour.
5) Run a cron job to calculate the actual balance. You should be able to display a last settlement time stamp. The cron job should be run   at a scheduled time interval of say 2 hours. 

# Tech stack used:

1) Python -server side.
2) MySQL
3) Cloud End Point - AWS Lamda.

# Steps performed to complete the task:

1) Created an AWS Lambda function, 
2) Created a Database instance,
3) Deployed API -post method for insertion of data into database through AWS Lambda function,
4) Used S3 to store HTML pages, 
5) a Cloudwatch event as a trigger to AWS Lambda function (Used for Cron Job).
