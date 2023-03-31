# Lab: Putting it All Together

## Overview

It's time to show off your skills by bringing "Vanilla" Django and Django Rest Framework together in the same project.

You'll build out a Restful API as well as a user facing site.

Along the way you'll see how easy Django makes it to move to a remote database.

The project will be an old favorite with a Python twist - a Cookie Stand management site.

## Feature Tasks and Requirements

You've got two choices for this lab:

### Choice 1: Use your own Template/s

- If you've built a template repository for your Django sites, or APIs, or both - now's the time to put them to work.
- See what it would take to combine the two approaches into one starter kit to rule them all.

### Choice 2: Use API Quick Start Template

The [API Quick Start](https://github.com/codefellows/python-401-api-quickstart){:target="_blank"} is a built out skeleton project with lots of the tools we've been using in class. Check it out. If you like it, use it. But better yet, use it as an inspiration to build your own that's a perfect fit.

**WARNING:** There is no guarantee that the `API Quick Start` is a perfect fit for your needs, is bug free, etc. It's a great jumping off point though. And if you spot any bugs or have ideas for improvements make a PR!

- Modify your application paying close attention to the instructions in README.md found in root of repository.
  - Install from requirements.txt.
  - Export (aka freeze) requirements.
  - Change `things` app folder to be `cookie_stands`
  - Go through code base looking for `Thing`,`thing` and `things` change to cookie-stand related names.
  - E.g. `Thing` model becomes `CookieStand`
  - E.g. `ThingList` becomes `CookieStandList`
- Pro Tip: Do a global text search looking for `thing`
  - Search should be case insensitive.
  - **WARNING:** Do NOT just cut and paste. Think through each change carefully.
- Create/rename `.env` using `.env.sample` as starting point.
  - Here's a handy way to generate a secret key
    - > python -c "import secrets; print(secrets.token_urlsafe())"

## CookieStand Model Details

- The `CookieStand` model must contain

```python
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location

```

- Notice the use of [JSONField](https://docs.djangoproject.com/en/4.0/ref/models/fields/#jsonfield){:target="_blank"}.
- Once changes are complete make migrations, migrate, and test locally.

### Database Deployment Requirements

- Host your Database at [ElephantSQL](https://www.elephantsql.com/){:target="_blank"}

### Site Deployment Requirements

- We'll handle deployment a little later. For now run your site locally, but the Database should be remote.

### Stretch Goals

- Add functionality so that when a JSON array of hourly_sales is not provided at creation time it will be generated with random numbers based on minimum/maximum customers per hour and average cookies per sale.

### Implementation Notes

- Name your repo `cookie-stand-api`
- Site must use environment variables.

### Useful Terminal Commands

- `docker compose up --build`
- `docker compose down`
- `docker compose restart`
- `docker compose run web python manage.py migrate`
- `docker compose run web python manage.py collectstatic`

## User Acceptance Tests

- Add Unit Tests to `cookie_stands/tests.py`
- Manually confirm API using API Tester, Postman or HTTPie.

## Submission Requirements

- Make sure a user exists in Database
  - E.g. `createsuperuser` has been run
- Provide username and password in Canvas submission
- Rename .env contents or provide in Canvas submission
- Include GitHub repo in Canvas submission

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
