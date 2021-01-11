# Election-Analysis
Analysis of an election audit for congressional election at the Colorado Board of Elections.

## Overview of Election Audit
This project is all about helping Tom, an employee of Colorado Board of Elections, to complete the election audit. In this audit we are going to calculate the following:
1. Total number of votes cast
2. Total number of votes for each candidate
3. The percentage of vote for each candidate
4. Winner of the election based on the popular votes

This task is usually done on Excel but Tom's Manager wants to know if there is an automated process using Python to complete the task. Once, the process is automated, it could not only be used for the audit of other congressional districts's elections but also for senatorial elections as well as local elections.

## Election Audit Results

* Total 369,711 votes were cast in this congressional election

* Breakdown of the number of votes and the percentage of total votes for each county
 **County          Votes      Percentage**
  * Jefferson --  38,855 --     10.5%
  * Denver    -- 306,055 --     82.8%
  * Arapahoe  --  24,801 --     6.7%

* **Denver** county had the largest number of votes

* Breakdown of the number of votes and the percentage of total votes for each candidate
 **Candidate                Percentage     Votes**
  * Charles Casper Stockham    23.0%      (85,213)
  * Diana DeGette              73.8%     (272,892)
  * Raymon Anthony Doane        3.1%      (11,606)

* The candidate who won the election is **Diana DeGette**. The total vote count she got is 
  272,892 and the percentage of total votes is 73.8%

* The link of the result screenshot is provided for your reference.

## Election Audit Summary

This automated script is working perfect and can be used for other election audits as well after modifying some part of code. For example if we want to use it for Federal Congressional Elections,then, we just need to change the county list to the State list.