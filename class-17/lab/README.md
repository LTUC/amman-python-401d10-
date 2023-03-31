# Lab: Web Scraping

## Overview

It's wonderful when someone has gone to the effort to expose their site's data through an API.

But not everyone can (or wants to) do that.

No problem. Let's code up a web scraper that can automate the process of manually using the site.

## Feature Tasks and Requirements

- Scrape a Wikipedia page of your choosing and record which passages need citations.
  - E.g. [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico){:target="_blank"} has a few "citations needed".
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for "lorem spam and impsum eggs"
  - Consider the "relevant passage" to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

- Module must be named **scraper.py**
- Create function named **get_citations_needed_count**
  - takes in a url string and returns an integer.
- Create function named **get_citations_needed_report**
  - takes in a url string and returns a report string
  - the string should be formatted with each citation listed in the order found.
  - For example:

```text
The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.

The Mexica people arrived in the Valley of Mexico in 1248 AD. They had migrated from the deserts north of the Rio Grande[citation needed] over a period traditionally said to have been 100 years. They may have thought of themselves as the heirs to the prestigious civilizations that had preceded them.[citation needed] What the Aztec initially lacked in political power, they made up for with ambition and military skill. In 1325, they established the biggest city in the world at that time, Tenochtitlan.

etc.
```

## Stretch Goals

- Organize the needed citations by section (i.e. the parent heading tag)
  - Name additional function **get_citations_needed_by_section**
- Automatically do a citation scan for any links from the main section of wikipedia page.

## Configuration

Create a project named `web-scraper`.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
