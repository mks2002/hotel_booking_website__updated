from django.db import models

# Create your models here.


class Paymentdetail(models.Model):
    # this details are bydefault provide by me ..
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    order_no = models.IntegerField()
    total_cost = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=50, default='paid')
    # this are the form inputs...
    email = models.CharField(max_length=50)
    card_no = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    expiry_date = models.CharField(max_length=5)



#   {% if messages %}
#             {% for message in messages %}
          

#             <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
#               <strong>{{ message }}</strong>
#               <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
#             </div>


#             {% endfor %}
#             {% endif %}