Feature: Home Page
    @home
    Scenario Outline: Home Page 
        When I am in login page with $<userRole> with userName $<userName> and password as $<password>
        Then I am in $<page> page
    Examples:
        |userRole|userName|password|page|
        |AdminUser|9849908466|admin@123|home|
        |NormalUser|7386851479|123456|home|

