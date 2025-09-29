Feature: Login Page
    @login
    Scenario Outline: Admin/Noraml User Login
        When I am in login page with $<userRole> with userName $<userName> and password as $<password>

    Examples:
        |userRole|userName|password|
        |AdminUser|9849908466|admin@123|
        |NormalUser|7386851479|123456|

