from django.db import models

# Create your models here.
class wordsearch_inner_page(models.Model):
    # word section
    font = models.CharField(max_length=150, default="Helvetica-Bold")
    word_font_size = models.FloatField(default=13.7)
    word_up_down = models.FloatField(default=5.0)
    word_left_right = models.FloatField( default=1.8)
    word_left_right_space = models.FloatField( default=2)
    word_up_down_space = models.FloatField( default=0)
    
    # alphabat      e section
    alphabate_font_size = models.FloatField(default=18.5)
    alphabate_up_down = models.FloatField(default=0.0)
    alphabate_left_right = models.FloatField(default=0.0)
    alphabate_left_right_space = models.FloatField( default=0.4)
    alphabate_up_down_space = models.FloatField( default=0.4)
    row = models.IntegerField(default=10)
    column = models.IntegerField(default=10)
    
    
    # rectangle section
    rectangle_l_r = models.FloatField(default=-0.09)
    rectangle_u_d = models.FloatField(default=0.05)
    rectangle_l_r_i = models.FloatField(default=0.0)
    rectangle_u_d_i = models.FloatField(default=0.0)
    
    #puzzle numbering
    numbering_font_size = models.FloatField(default=18.5)
    numbering_left_right = models.FloatField(default=3.84)
    numbering_up_down = models.FloatField(default=10.12)
    number_show = models.IntegerField(default=2)
    line_left_right = models.FloatField(default=-0.14)
    line_up_down = models.FloatField(default=-0.05)
    text_left_right = models.FloatField(default=0.0)
    text_up_down = models.FloatField(default=0.0)
    right_puzzle = models.FloatField(default=4)
    
    # down puzzle possition
    puzzle_up_down = models.FloatField(default=-5.0)
    # problem per page
    problem_per_page = models.IntegerField(default=1)   
    def __str__(self):
        return str(self.problem_per_page)

class puzzleoption(models.Model):
    choose_option = models.IntegerField(default = 1)
    def __str__(self):
        return str(self.choose_option)