from django.db import models


    
class CustomerInfo(models.Model):
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255, blank=True)
    name3 = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    zip1  = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
   
    
        
class CustomerDocument(models.Model):
    document = models.FileField(upload_to='documents/')
    
    
    
    
    

    
"""

tinymce.init({
  selector: 'textarea',
  width: 1000,
  height: 800,
  plugins: [
    'advlist autolink link image lists charmap print preview hr anchor pagebreak',
    'searchreplace wordcount visualblocks code fullscreen insertdatetime media nonbreaking',
    'table emoticons template paste help'
  ],
  toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
    'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
    'forecolor backcolor emoticons | help',
  menu: {
    favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
  },
  menubar: 'favs file edit view insert format tools table help',
  content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
});

"""