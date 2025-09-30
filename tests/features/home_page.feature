Feature: Home Page
    @home
    Scenario Outline: Home Page 
        When I am in login page with $<userRole> with userName $<userName> and password as $<password>
        Then I login to home page
        Then I am in $<page> page with content $<content>
       
    Examples:
        |userRole|userName|password|page|content|
        |AdminUser|9849908466|admin@123|home|Admin Dashboard,Manage and monitor all citizen service requests,Manage Polls,View Analytics,Service Requests|
        |AdminUser|9849908466|admin@123|home|Created,Assigned,In Progres,Pending,Comple,Resolved,Closed,Rejected,Service Requests|
        |NormalUser|7386851479|123456|home|Select Complaint Type,Sanitation,Roads,Property Tax Issues,Water Supply Issues,Health & Hygiene|

