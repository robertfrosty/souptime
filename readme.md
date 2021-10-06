# Nautical Escapes 2021

***https://whoaitssouptime.ca***

Base Website Design For WhoaIt'sSoupTime, with any sensitive information removed. This website is written in HTML/CSS and mainly vanilla Javascript (specific libraries like leaflet.js and dragscroll.js are used), and hosted using a nginx & uWSGI web server that serves python web applications, all built on linux (of course), and provided by DigitalOcean.

***Homepage Production Version***

Soup Bowl Version
![screenshot of whoaitssouptime.ca homepage](./screenshots/whoaitssouptime.ca_.png)

Text-Only Version
![screenshot of whoaitsosuptime.ca homepage, text-only](./screenshots/whoaitssouptime.ca_text.png)

-Screenshots taken with Google Chrome Inspector Commands-

***Personal Thoughts***

This was my first large-scale project where I was completely in charge of developing all aspects of the website, and in addition I had moderately strict time requirements to uphold, so I felt a lot of pressure going into this project. Looking back would have done many things differently, however, I'm proud of the unique system that I created to receive and format information directly from the client, which will save the client a ton of time in the future. I'm very happy with the asthetic of the website, and when I have more time I have plans to go back and add in the animations that I have created all over the website.

***Server Side Flow Of Information/Data***
![diagram showing flow of information from 'nginx' to 'uWSGI' to 'python web frameworks' and then to other services on linux server](./screenshots/diag.png)

Documentation / Blogs : 
https://uwsgi-docs.readthedocs.io/en/latest/ (Official uWSGI docs)

https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/ (Official nginx docs)

https://www.ultravioletsoftware.com/single-post/2017/03/23/An-introduction-into-the-WSGI-ecosystem (A helpful blog-post breaking down the different parts of the WSGI ecosystem)

https://goutomroy.medium.com/request-and-response-cycle-in-django-338518096640 (Request and response life cycle in Django, I found helpful for understanding the flow of information)

***Google Inspector Lighthouse Results***

![screenshot of google chrome inspector lighthouse results for nauticalescapes2021.com](./screenshots/lighthouse.PNG)

