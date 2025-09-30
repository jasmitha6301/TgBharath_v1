Feature: Login Page
    @login1
    Scenario Outline: Admin/Noraml User Login with roles
        When I am in login page with $<userRole> with userName $<userName> and password as $<password>
        Then I login to home page

    Examples:
        |userRole|userName|password|
        |AdminUser|9849908466|admin@123|
        |NormalUser|7386851479|123456|

    @login2
    Scenario Outline: Admin/Noraml User login page basic content check
        When I am in login page with $<userRole> with userName $<userName> and password as $<password>
        Then I am in $<page> page with content $<content>

    Examples:
        |userRole|userName|password|page|content|
        |AdminUser|9849908466|admin@123|login|Admin Login,Sign in to your admin account,Mobile Number (Admin User),Password,Download Our Mobile App,Available on Google Play,Download Our Mobile App,Download TGBharath Android App| 
        |NormalUser|7386851479|123456|login|User Login,Sign in to your account to access services,Mobile Number,Password,Sign In,Forgot Password?,Don't have an account? Sign up here,Download Our Mobile App,Download TGBharath Android App|
        
        
    