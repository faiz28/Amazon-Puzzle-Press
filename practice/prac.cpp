#include <bits/stdc++.h>
using namespace std;
char puzzle[17][17];
void func(string s,int x,int y,int n)
{
    vector<int>vc;
    int i_got_posittion = 0;
    int total_x = x - s.size();
    int total_y = y + s.size();
    cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
    if (total_x >= 0 && total_y < n)
    {
        int store_x = x, store_y = y, check = 0, cnt = 0;
        for (int i = x; i > total_x; i--)
        {
            
            cout<<puzzle[i][y]<<" "<<s[cnt]<<endl;
            if (puzzle[i][y] == '#' || puzzle[i][y] == s[cnt])
            {
                if (s[cnt] == puzzle[i][y])
                    vc.push_back(i);
                puzzle[i][y] = s[cnt];
                y++;
                cnt++;
            }
            else
            {
                check = 1;
                i_got_posittion = 1;
                break;
            }
        }
        if (check == 1)
        {
            if (vc.size() == 0)
            {
                if(cnt>0)
                {
                    for (int i = store_x; i > total_x+cnt; i--)
                    {
                        puzzle[i][store_y] = '#';
                        store_y++;
                    }
                }
                
            }
            else
            {
                int check = 0;
                for (int i = store_x; i > total_x+cnt; i--)
                {
                    if (i == vc[check])
                    {
                        check++;
                    }
                    else
                    {
                        puzzle[i][store_y] = '#';
                    }
                    store_y++;
                }
            }
        }
        vc.clear();
    }
    else{
        i_got_posittion = 1;
    }
}
int main()
{
for(int i=0;i<15;i++)
    for(int j=0;j<15;j++)
        puzzle[i][j] = '#';
srand(time(0));
int ran_x = rand()%15;
int ran_y = rand()%15;

cout<<ran_x<<" "<<ran_y<<endl;
string str[5]={"faiz","amhed","chandina"};


for(int i=0;i<2;i++)
    func(str[i],ran_x,ran_y,15);

for(int i=0;i<15;i++)
{
    for(int j=0;j<15;j++)
    {
        cout<<puzzle[i][j]<<" ";
    }
    cout<<endl;
        
}
    

}