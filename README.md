# Console Application README Example

## About Me Quiz

Lab:27 -Django Models

*Author: Nebiyu Kifle*

----

## Description
***[Tell me about your application, should be about a paragraph]***
##### create snack_tracker_project project

## Model

- create snacks app
- Add snacks app to project
- create Snack mode
       - make sure it extends from proper base class
       - add name as a CharField with maximum length of 64 characters.
       - add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
           - from django.contrib.auth import get_user_model
- add description TextField

## Views for Snacks App
- create SnackListView
   - extend ListView
   - give a template of snack_list.html
   - associate Snack model
- update url patterns for project
   - empty path should include snacks.urls
- update snacks app urls
   - empty sub-path should be handled by SnackListView
   - Don’t forget to use as_view()
- add detail view
   - link snack_detail.html template
   - associate Snack model
- update app urlpatterns to handle detail view
   - account for primary key in url
   - path would look like localhost:8000/1/ to get to      snack with id of 1

## Templates

- Addtemplates folder in root of project
  - register templates folder in project settings TEMPLATES section
- create base.html ancestor template
  - add main html document
  - use Django Templating Language to allow child templates to insert content
- create snack_list.html template
  - extend base template
  - use Django Templating Language to display each snack’s name
- view home page (aka snack_list) and confirm snacks showing properly
- create snack_detail.html template
  - template should extend base
  - content should display snack’s name, description and purchaser

- add link in snack_list template to related detail page for each snack
- Add a link back to Home (aka snack_list) page from detail page.

---
## User Acceptance Tests

- Test Snack pages
  - NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
  - verify status code
  - verify correct template use
  - use url name instead of hard coded path
    - TIP: django.urls.reverse will help with that.
- We can’t easily test SnackDetailView just yet.
  - Can you figure out why?
  
### Getting Started
Clone this repository to your local machine.

```
$ git clone : https://github.com/neba9/snack_tracker_project.git
```

---

------------------------------
For more information on Markdown: https://github.com/neba9/django-snacks/blob/master/README.md