from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    book = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

def __str__(self):
    return f"{self.name, self.date_of_birth, self.book, self.pub_date}"

class Genre(models.Model):
        name = models.CharField(max_length = 200)

def __str__(self):
    return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    summary = models.TextField()
    ISBN = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    language = models.CharField(max_length = 100)

def __str__(self):
    return f"{self.title, self.summary, self.ISBN, self.genre, self.language}"

class Bookinstance(models.Model):
    due_back = models.DateTimeField()
    status = models.CharField(max_length = 50)
    book = models.CharField(max_length = 200)
    borrower = models.CharField(max_length = 200)    

def __str__(self):
    return f"{self.due_date, self.status, self.book, self.borrower}" 

