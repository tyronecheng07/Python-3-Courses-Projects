# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(word, email):
  if word in email:
    email.replace(word, 'x')
  return email

print(censor("learning algorithms", email_one))

def censor_phrases(lst, email):
  for string in lst:
    if string in email:
      email.replace(string, 'x')
  return email

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

print(censor_phrases(proprietary_terms, email_two))

def censor_negative(lst, email):
  for string in lst:
    if email.count(string) == 2:
      censor_phrases(proprietary_terms, email)
      email.replace(string, 'x')
  return email

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

print(censor_negative(negative_words, email_three))

def censor_all(lst, email):
  if email == email_four:
    censor_phrases(proprietary_terms, email)
    censor_phrases(negative_words, email)
    for character in email:
      lst.replace(character, "")
  return email
