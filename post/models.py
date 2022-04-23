from django.db import models


class Post(models.Model):
    SPORT = 'Sport'
    BUSINESS = 'Business'
    MARKETING = 'Marketing'
    TECH = 'Tech'
    FOOD = 'Food'
    CULTURE = 'Culture'
    DESIGN = 'Design'
    TRAVEL = 'Travel'
    CATEGORY_CHOICES = (
        (SPORT, 'Sport'),
        (BUSINESS, 'Business'),
        (MARKETING, 'Marketing'),
        (TECH, 'Tech'),
        (FOOD, 'Food'),
        (CULTURE, 'Culture'),
        (DESIGN, 'Design'),
        (TRAVEL, 'Travel'),
    )
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )

    categories = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Post1(models.Model):
    SPORT = 'Sport'
    BUSINESS = 'Business'
    MARKETING = 'Marketing'
    TECH = 'Tech'
    FOOD = 'Food'
    CULTURE = 'Culture'
    DESIGN = 'Design'
    TRAVEL = 'Travel'
    CATEGORY_CHOICES = (
        (SPORT, 'Sport'),
        (BUSINESS, 'Business'),
        (MARKETING, 'Marketing'),
        (TECH, 'Tech'),
        (FOOD, 'Food'),
        (CULTURE, 'Culture'),
        (DESIGN, 'Design'),
        (TRAVEL, 'Travel'),
    )
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )

    categories = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    authors = models.CharField(max_length=30, choices=AUTHOR_CHOICE, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Trending(models.Model):
    SPORT = 'Sport'
    BUSINESS = 'Business'
    MARKETING = 'Marketing'
    TECH = 'Tech'
    FOOD = 'Food'
    CULTURE = 'Culture'
    DESIGN = 'Design'
    TRAVEL = 'Travel'
    CATEGORY_CHOICES = (
        (SPORT, 'Sport'),
        (BUSINESS, 'Business'),
        (MARKETING, 'Marketing'),
        (TECH, 'Tech'),
        (FOOD, 'Food'),
        (CULTURE, 'Culture'),
        (DESIGN, 'Design'),
        (TRAVEL, 'Travel'),
    )

    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )

    title = models.CharField(max_length=1000)
    body = models.TextField(null=True, blank=True)
    categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    authors = models.CharField(max_length=50, choices=AUTHOR_CHOICE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Headline(models.Model):
    SPORT = 'Sport'
    BUSINESS = 'Business'
    MARKETING = 'Marketing'
    TECH = 'Tech'
    FOOD = 'Food'
    CULTURE = 'Culture'
    DESIGN = 'Design'
    TRAVEL = 'Travel'
    CATEGORY_CHOICES = (
        (SPORT, 'Sport'),
        (BUSINESS, 'Business'),
        (MARKETING, 'Marketing'),
        (TECH, 'Tech'),
        (FOOD, 'Food'),
        (CULTURE, 'Culture'),
        (DESIGN, 'Design'),
        (TRAVEL, 'Travel'),
    )
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    title = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    overview = models.CharField(max_length=500)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICE)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Culture(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    title = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, default='Culture')
    overview = models.CharField(max_length=500)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICE)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Business(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    title = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, default='Business')
    overview = models.CharField(max_length=500)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICE)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class LifeStyle(models.Model):
    PRECIOUS_OBINNA = 'Precious Obinna'
    OHANYERE_PRECIOUS = 'Ohanyere Precious'
    JUDE_OHANYERE = 'Jude Ohanyere'

    AUTHOR_CHOICE = (
        (PRECIOUS_OBINNA, 'Precious Obinna'),
        (OHANYERE_PRECIOUS, 'Ohanyere Precious'),
        (JUDE_OHANYERE, 'Jude Ohanyere')

    )
    title = models.CharField(max_length=100)
    categories = models.CharField(max_length=50, default='Lifestyle')
    overview = models.CharField(max_length=500)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, choices=AUTHOR_CHOICE)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
