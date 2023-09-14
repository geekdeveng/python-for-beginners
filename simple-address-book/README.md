# simple address book


***

### How to proceed
```text
The detailed procedure is as follows.
```
1. Read the domain requirements and check what needs to be done.
2. Please check the technical requirements to see what technical considerations need to be taken during implementation.
3. Fork from the assignment repository to your own github.
4. The task is to develop DB, model design, and API.
5. When the work is completed, please reply to the email with a link to your personal repository.

***
### Domain Requirements

```text
Please implement address book and contact details.
It may be easier to understand if you refer to Google's address book (https://contacts.google.com).
```
- address book
   - List
     - The fields that will be displayed in the list are as follows.
       - Profile picture
       - name
       - email
       - phone number
       - Company (position)
       - label
     - Sort
       - The default output is sorted in registration order.
       - You can sort by name, email, or phone number.
       - Sorting is in ascending/descending/off order.
     - Paging
       - Enable scroll paging processing.
   - Contact information (view/enter details)
     - The input/output fields are as follows.
       - Profile photo: URL input method
       - name
       - email
       - phone number
       - company
       - position
       - memo
       - label
         - Custom labels
         - Multiple labels can be linked to one contact
       - Add other items
         - address
         - birthday
         - Website

***
### Technical Requirements
```text
Technical requirements are as follows:
```
- environment
   - python: 3.9.3
   - django: 3.2.20
   -django-rest-framework: 3.14.0
   - MySQL or SQLite (Choose 1)
   - Other required packages can be used and added to `requirements.txt`
-Backend
   - Please use the django ORM model.
   - Please configure the directory structure according to your best practices.
   - Please design the API to be **RESTfull**.
-Database
   - Please use MySQL or SQLite as the DB.
   - Please define the designed schema and data in the `/db` directory.
     - schema.sql: Please create the DB schema using the CREATE statement.
     - data.sql: If you need basic data, enter it with an INSERT statement.
   - If you have an ERD you designed, it would be helpful if you added it to the `/db` directory. (`Optional`)
- Other (`Optional`)
   - It is only checked if it is optional.
     - swagger
     -test code