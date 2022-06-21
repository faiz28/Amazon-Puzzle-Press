from django.db import models

# Create your models here.

class inner_page(models.Model):
    # header section
    header_fonts = models.CharField(max_length=150, default="Helvetica-Bold")
    header_up_down = models.FloatField(default=0.0)
    header_left_right = models.FloatField( default=0)
    font_inc_dec = models.FloatField(default=0)
    
    # number section
    digit_number_font = models.CharField(max_length=150, default="Helvetica-Bold")
    numbering_font_size = models.FloatField(default=10.0)
    numbering_up_down = models.FloatField(default=0.0)
    numbering_left_right = models.FloatField(default=0.0)
    number_on_off = models.IntegerField(default=1)
    #digit section
    digit_font_size = models.FloatField(default=16.0)
    digit_left_right = models.FloatField(default=0.0)
    digit_up_down = models.FloatField(default=0.0)
    digit_space = models.FloatField(default=0.0)
    front_inc = models.FloatField(default=0.0)
    prob_per_row = models.IntegerField(default=0)
    prob_per_col = models.IntegerField(default=0)
    length_of_digit = models.IntegerField(default=1)
    
    #rectangle section
    ractangle_up_down = models.FloatField(default=0.0)
    ractangle_left_right = models.FloatField(default=0.0)
    rec_l_r_inc = models.FloatField(default=0.0)
    rec_u_d_inc = models.FloatField(default=0.0)
    rec_on_off = models.IntegerField(default=1)
    line_inc = models.FloatField(default=0.0)
    line_up_down = models.FloatField(default=0.0)
    line_left_right = models.FloatField(default=0.0)
    ineer_space = models.FloatField(default=0.0)
    
    
    

    def __str__(self):
        return str(self.length_of_digit)
