=========
udemy POC
=========
go to http://www.udemy.com
click "Browse courses"
In the side menu select "development" -> "Web development"
In the search box "selenium"
check the "free" check box.
Verify we get at least 2 and no more than 10 courses
Verify all courses are marked "Free"
Verify at least one course has the word "Selenium" in it's title.

Requirements
------------
Download latest selenium-server-standalone jar and run::

   $ java -jar selenium-server-standalone-2.48.2.jar -ensureCleanSession -trustAllSSLCertificates &


Install
-------
To run main test run installation, use virtualenvwrapper recommended
After install and configure virtualenvwrapper run::

   $ mkvirtualenv env1
   $ pip install --upgrade pip
   $ pip install -r requirements.txt
   $ python setup.py install


Run Test
--------
- Test configurations are listed in tests/test_flow1.py
- The test assuming using selenium-server-standalone described in section "Requirements".
- Tested on Firefox only.

Run ::
   $ py.test -m testme


TODO
----
- Fix locators to make sure test is persistant as possible
