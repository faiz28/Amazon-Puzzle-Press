#include <bits/stdc++.h>
using namespace std;

char puzzle[19][19];
int kkk = 0;

void str_sort(string s[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (s[i].length() > s[j].length())
            {
                swap(s[i], s[j]);
            }
        }
    }
}
int take_pos(int rand_num, int x, int y, string s, int n)
{
    vector<int> vc;
    int i_got_posittion = 2;
    cout << "rand number  =  " << rand_num << ",x = " << x << ",y = " << y << endl;
    if (rand_num == 0)
    {
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
                     cout<<check<<endl;
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
                        for (int i = store_x; i > store_x-cnt; i--)
                        {
                            puzzle[i][store_y] = '#';
                            store_y++;
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = store_x; i > store_x-cnt; i--)
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
    if (rand_num == 1)
    {
        int total_x = x + s.size();
        int total_y = y + s.size();
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_x < n && total_y < n)
        {
            int store_x = x, store_y = y, check = 0, cnt = 0;
            for (int i = x; i < total_x; i++)
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
                     cout<<check<<endl;
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
                        for (int i = x; i < x+cnt; i++)
                        {
                            puzzle[i][store_y] = '#';
                            store_y++;
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = x; i < x+cnt; i++)
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
    if (rand_num == 2)
    {
        int total_x = x + s.size();
        int total_y = y - s.size();
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_x < n && total_y >= 0)
        {
            int store_x = x, store_y = y, check = 0, cnt = 0;
            for (int i = x; i < total_x; i++)
            {
                cout<<puzzle[i][y]<<" "<<s[cnt]<<endl;
                if (puzzle[i][y] == '#' || puzzle[i][y] == s[cnt])
                {
                    if (s[cnt] == puzzle[i][y])
                        vc.push_back(i);
                    puzzle[i][y] = s[cnt];
                    y--;
                    cnt++;
                }
                else
                {
                    check = 1;
                     cout<<check<<endl;
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
                        for (int i = x; i < x+cnt; i++)
                        {
                            puzzle[i][store_y] = '#';
                            store_y--;
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = x; i < x+cnt; i++)
                    {
                        if (i == vc[check])
                        {
                            check++;
                        }
                        else
                        {
                            puzzle[i][store_y] = '#';
                        }
                        store_y--;
                    }
                }
            }
            vc.clear();
        }
        else{
            i_got_posittion = 1;
        }
    }
    if (rand_num == 3)
    {
        int total_x = x - s.size();
        int total_y = y - s.size();
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_x >= 0 && total_y >= 0)
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
                    y--;
                    cnt++;
                }
                else
                {
                    check = 1;
                     cout<<check<<endl;
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
                        for (int i = store_x; i > store_x-cnt; i--)
                        {
                            puzzle[i][store_y] = '#';
                            store_y--;
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = store_x; i > store_x-cnt; i--)
                    {
                        if (i == vc[check])
                        {
                            check++;
                        }
                        else
                        {
                            puzzle[i][store_y] = '#';
                        }
                        store_y--;
                    }
                }
            }
            vc.clear();
        }
        else{
            i_got_posittion = 1;
        }
    }
    if (rand_num == 4)
    {
        int total_x = x - s.size();
        int total_y = y;
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_x >= 0)
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
                    cnt++;
                }
                else
                {
                    check = 1;
                     cout<<check<<endl;
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
                        for (int i = store_x; i > store_x-cnt; i--)
                        {
                            puzzle[i][store_y] = '#';
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = store_x; i > store_x-cnt; i--)
                    {
                        if (i == vc[check])
                        {
                            check++;
                        }
                        else
                        {
                            puzzle[i][store_y] = '#';
                        }
                    }
                }
            }
            vc.clear();
        }
        else{
            i_got_posittion = 1;
        }
    }
    if (rand_num == 5)
    {
        int total_x = x;
        int total_y = y + s.size();
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_y < n)
        {
            int store_x = x, store_y = y, check = 0, cnt = 0;
            for (int i = y; i < total_y; i++)
            {
                cout<<puzzle[i][y]<<" "<<s[cnt]<<endl;
                if (puzzle[x][i] == '#' || puzzle[x][i] == s[cnt])
                {
                    if (s[cnt] == puzzle[x][i])
                        vc.push_back(i);
                    puzzle[x][i] = s[cnt];
                    cnt++;
                }
                else
                {
                    check = 1;
                    cout<<check<<endl;
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
                        for (int i = y; i < y+cnt; i++)
                        {
                            puzzle[x][i] = '#';
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = y; i < y+cnt; i++)
                    {
                        if (i == vc[check])
                        {
                            check++;
                        }
                        else
                        {
                            puzzle[x][i] = '#';
                        }
                    }
                }
            }
            vc.clear();
        }
        else{
            i_got_posittion = 1;
        }
    }
    if (rand_num == 6)
    {
        int total_x = x + s.size();
        int total_y = y + s.size();
        cout<<"total_x = "<<total_x<<" total_y = "<<total_y<<endl;
        if (total_x < n && total_y < n)
        {
            int store_x = x, store_y = y, check = 0, cnt = 0;
            for (int i = x; i < total_x; i++)
            {
                if (s[cnt] == '#' || s[cnt] == puzzle[i][y])
                {
                    if (s[cnt] == puzzle[i][y])
                        vc.push_back(i);
                    puzzle[i][y] = s[cnt];
                    y++;
                    x++;
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
                        for (int i = store_x; i < store_x+cnt; i++)
                        {
                            puzzle[i][store_y] = '#';
                            store_y++;
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = store_x; i < store_x+cnt; i++)
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
    if (rand_num == 7)
    {
        int total_y = y - s.size();
        cout<<" total_y = "<<total_y<<endl;
        if (total_y >= 0)
        {
            int store_y = y, check = 0, cnt = 0;
            for (int i = y; i > total_y; i--)
            {
                cout<<puzzle[i][y]<<" "<<s[cnt]<<endl;
                if (puzzle[x][i] == '#' || puzzle[x][i] == s[cnt])
                {
                    if (s[cnt] == puzzle[x][i])
                        vc.push_back(i);
                    puzzle[x][i] = s[cnt];
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
                        for (int i = y; i > y-cnt; i--)
                        {
                            puzzle[x][i] = '#';
                        }
                    }
                    
                }
                else
                {
                    int check = 0;
                    for (int i = y; i > y-cnt; i--)
                    {
                        if (i == vc[check])
                        {
                            check++;
                        }
                        else
                        {
                            puzzle[x][i] = '#';
                        }
                    }
                }
            }
            vc.clear();
        }
        else{
            i_got_posittion = 1;
        }
    }
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            kkk++;
    return i_got_posittion;
}
void select_pos(int x, int y, string s, int n)
{
    int up_right = 0, right_down = 1, down_left = 2, left_up = 3, upper = 4, right = 5, down = 6, left = 7;
    srand(time(0));
    int rand_num = rand() % 8;
    cout<<"string = "<<s<<",x = "<<x<<",y = "<<y<<",random = "<<rand_num<<endl;
    for (int i = 0; i < 8; i++)
    {
        int result_find = take_pos(rand_num, x, y, s, n);
        rand_num =rand_num % 8;
        rand_num++;
        if(result_find == 2) break;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << puzzle[i][j] << " ";
        }
        cout << endl;
    }
}

void store(string s, int n)
{
    
   
    
}

int main()
{
    int n = 15;

    string str[277] = {"straightenttt", "straighten", "straighten", "straighten","straighten", "straighten", "straighten", "straighten", "straighten", "straighten","straighten", "straighten", "straighten", "straighten", "straighten", "straighten","straighten", "straighten", "straighten", "straighten", "straighten", "straighten","straighten", "straighten", "straighten", "straighten", "straighten", "straighten"};
    int len = 27;

    str_sort(str, len);

    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            puzzle[i][j] = '#';
        }
    }
    // store every character
    // for (int i = 0; i < len; i++)
    // {
    //     store(str[i], n);
    // }

     srand(time(NULL));
    
    int ran_x[len]={0},ran_y[len]={0};
    for(int i=0;i<len;i++){
        ran_x[i]= rand()%n;
        ran_y[i]= rand()%n;
        cout<<"X ========== "<<ran_x[i]<<" Y======= "<<ran_y[i]<<endl;
    }
    
    for(int i=0;i<len;i++) {
        select_pos(ran_x[i], ran_y[i], str[i], n);
    }
    cout << "\n\n\n";
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << puzzle[i][j] << " ";
        }
        cout << endl;
    }

    cout<<kkk<<endl;

    return 0;
}