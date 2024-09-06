from django.db import models

class PersonalInfo(models.Model):
    """
    Model to store personal information of the user.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    profile_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Education(models.Model):
    """
    Model to store educational qualifications.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class WorkExperience(models.Model):
    """
    Model to store work experience details.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='work_experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Skill(models.Model):
    """
    Model to store skills.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ], default='Beginner')

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


class Certification(models.Model):
    """
    Model to store certifications.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_obtained = models.DateField()
    valid_until = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Model to store project details.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.CharField(max_length=300)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    """
    Model to store languages known by the user.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=20, choices=[
        ('Basic', 'Basic'),
        ('Conversational', 'Conversational'),
        ('Fluent', 'Fluent'),
        ('Native', 'Native')
    ], default='Basic')

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


class Interest(models.Model):
    """
    Model to store personal interests.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reference(models.Model):
    """
    Model to store references.
    """
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position} at {self.company}"
