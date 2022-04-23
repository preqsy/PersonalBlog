from django.db import models


class PostComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class HeadlineComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class BusinessComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class CultureComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class TrendComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class LifestyleComments(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


# Create your models here.
