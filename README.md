
<h1 align="center">Payment Processor</h1>

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## LIVE

<https://midware.herokuapp.com/api/v1/>

### Stripe Payments

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/stripe.png" alt="drawing" width="1920"/>

### Browsable Request API

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/request.png" alt="drawing" width="1920"/>

### Admin Interface

- user: admin
- password: admin

<img src="https://github.com/gurupratap-matharu/midware/blob/master/staticfiles/img/admin.png" alt="drawing" width="1920"/>

## Motivation 🎯

- App suggestion based on interview assignment
- Deployment with docker on heroku
- Working with tools that are free for open source
- Working with payment methods like stripe and REST apis

## Features ✨

- Logs Requests and responses using logging module
- Save Requests and responses to database for persistency
- Connects with Stripe payments to creates a payment upon POST
- Versioning of api possible see `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability

## Development setup 🛠

Steps to locally setup development after cloning the project.

`docker-compose up -d --build`
or simple
`make build` ;)
