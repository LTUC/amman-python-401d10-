# Lab: React IV - Deployment

## Overview

It's time to go live with your Cookie Stand front and back ends!

There are a lot of great (and cheap) deployment options. One of the easiest to use is [Vercel](https://vercel.com/){:target="_blank"}.

In fact, we can use it for both our client and server applications.

## Feature Tasks and Requirements

### API

- Create a new Vercel project by importing your `cookie-stand-api` project from GitHub.
    - **Note:** The project name `cookie-stand-api` will likely be taken so choose something sensible like `cookie-stand-api-awesome-dev`.
    - Set the Environment Variables.
        - **TIP:** paste the contents of your `.env` file.
    - Don't forget to include `vercel.json` and update `wsgi.py`. See the demo for examples.
    - Manually test Django Admin panel.
    - Manually test api routes.

### Front End

- Create a new Vercel project by importing your `cookie-stand-admin` project from GitHub.
    - **Note:** The project name `cookie-stand-admin` will likely be taken so choose something sensible like `cookie-stand-admin-awesome-dev`.
    - Set the Environment Variables.
        - **TIP:** paste the contents of your `.env.local` file.
        - **TIP:** check that locally running front end works with deployed API prior to deploying front end.


## Implementation Notes

- You'll need a Vercel account and to authorize it with Github.
  - The Deployment instructions above will walk you through it.

### Stretch Goals

- Deploy a preview build (include URL in README)
- Use a competing host (e.g. AWS, Digital Ocean, Netlify, etc.)

### User Acceptance Tests

No automated testing today.

## Configuration

- Customize README.md for your apps.
  - Include deployed URL in README files.
