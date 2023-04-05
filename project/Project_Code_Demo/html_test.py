# Databricks notebook source
# Load HTML file
with open('/dbfs/FileStore/shared_uploads/rovanelgendy@outlook.com/MonthlyRevenue_Dashboard_Databricks.html', 'r') as file:
    html = file.read()

# Update Git repo with HTML file
!git add /dbfs/FileStore/shared_uploads/rovanelgendy@outlook.com/MonthlyRevenue_Dashboard_Databricks.html
!git commit -m 'Update MonthlyRevenue_Dashboard_Databricks.html'
!git push origin master
