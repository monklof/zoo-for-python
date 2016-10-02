Usage:

```python
from maillib import MailBox, Email

# init a mailbox
mailbox = MailBox("smtp.gmail.com", 587, auth=("USERNAME", "PASSWORD"))
mailbox.start()
# write a email
mail = Email("from@gmail.com", ["to@gmail.com"], subject="mail title",
             content="<h1></h1>", content_type="html")
# send it
mail.send_mail(mail)

```
