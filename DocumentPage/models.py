from django.db import models

# Create your models here.
class Document(models.Model):
    number = models.CharField(max_length=100)
    published_date = models.DateField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    subject = models.TextField()
    attachments = models.ManyToManyField('Attachment')
    signed_by = models.CharField(max_length=100)

    def __str__(self):
        return self.number
    
class DocumentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=200)
    tax_id = models.CharField(max_length=50)  # IČO
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
 

    def __str__(self):
        return f"{self.file.name}"
