Exploiting XSS and multitenancy

Lots of servers, like http://student.agh.edu.pl are multi-tenant environments
that allow each user to run own php application in a server path subdirectory.
This way one user can have his own script at
http://student.agh.edu.pl/~average-joe/ while other can run one at
http://student.agh.edu.pl/~mr-hacker/. These two applications are completely
separate but they share the same domain which has far reaching consequences.

Chrome browser when performing password autocomplete only compares the
domain name part of the url. This means that if Average Joe used the
remember password feature on http//student.agh.edu.pl/~average-joe/.
Mr. Hacker can use a specially crafted form on his website to trick
Chrome into filling it out with Joe's credentials. The only requirement
this form must meet is to have inputs with same names as on Joe's site.

After the fields are filled out it's trivial to read their values and
send their to Mr. Hacker's server using AJAX.

This application allows you to replicate this flow. It's source code is
hosted at http://github.com/karolmajta/xss-multitenancy

To run it after cloning the repo, and cd into it, to:

    $ pip install -r requirements.txt
    $ python app.py
