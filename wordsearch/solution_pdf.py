import random,string
from reportlab.lib.units import inch
def draw_line(solution_pdf,x,y,x1,y1,rem_x,rem_y):
            solution_pdf.line((rem_x +(y*0.2)+0.05)*inch,(rem_y-(x*0.2)+ 0.05)*inch,(rem_x +((y1*0.2))+0.05)*inch,(rem_y-(x1*0.2)+0.05)*inch)
class solution_design:
    def solution_func(solution_pdf,final_word,puzzle,store_all,row,col,x,y,step,c):
        REM_X =x
        REM_Y = y
        solution_pdf.setFont("Helvetica", 18)
        solution_pdf.drawString((x)*inch,(y+0.35)*inch,"solution #%d"%(step+1))
        solution_pdf.line(x*inch,(y+0.25)*inch,(x+c-0.4)*inch,(y+0.25)*inch)
        
        # print(step,new,y)
        solution_pdf.setFont("Helvetica", 12)
        
        for i in range(row):
            for j in range(col):
                solution_pdf.drawString(x*inch,y*inch, puzzle[i][j])
                x+=0.2
            y-=0.2
            x = REM_X
        
        # print(store_all)
        for info in store_all:
            x,y,new_x,new_y,direction = store_all[info]
            # print(REM_X +(x*0.2),(REM_Y+(y*0.2)),REM_X +(new_x*0.2),(REM_Y+(new_y*0.2)),REM_X,REM_Y)
            draw_line(solution_pdf,x,y,new_x,new_y,REM_X,REM_Y)

            
